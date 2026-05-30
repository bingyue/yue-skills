#!/usr/bin/env python3
"""
即梦 VOD 媒体上传工具
支持: video, audio, image

用法:
  python upload.py <file_path> [--type video|audio|image]

输出 JSON:
  {"ok": true, "vid": "...", "uri": "...", "meta": {...}}
  {"ok": false, "error": "...", "step": "..."}
"""

import sys
import os
import json
import hashlib
import hmac
import datetime
import zlib
import argparse
import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, '..', 'cookies.json')

CHUNK_SIZE = 4 * 1024 * 1024  # 4MB

# VOD API 的 FileType 只接受 video 和 image
# 音频文件也用 FileType=video 上传，VOD 会自动识别实际格式
EXT_TO_TYPE = {
    '.mp4': 'video', '.mov': 'video', '.avi': 'video', '.mkv': 'video',
    '.webm': 'video', '.flv': 'video', '.wmv': 'video', '.m4v': 'video',
    '.mp3': 'video', '.wav': 'video', '.aac': 'video', '.flac': 'video',
    '.ogg': 'video', '.m4a': 'video', '.wma': 'video',
    '.jpg': 'image', '.jpeg': 'image', '.png': 'image', '.gif': 'image',
    '.webp': 'image', '.bmp': 'image', '.svg': 'image',
}

# 记录实际媒体类型，用于返回结果
EXT_TO_MEDIA = {
    '.mp4': 'video', '.mov': 'video', '.avi': 'video', '.mkv': 'video',
    '.webm': 'video', '.flv': 'video', '.wmv': 'video', '.m4v': 'video',
    '.mp3': 'audio', '.wav': 'audio', '.aac': 'audio', '.flac': 'audio',
    '.ogg': 'audio', '.m4a': 'audio', '.wma': 'audio',
    '.jpg': 'image', '.jpeg': 'image', '.png': 'image', '.gif': 'image',
    '.webp': 'image', '.bmp': 'image', '.svg': 'image',
}


def fail(error, step='unknown'):
    print(json.dumps({"ok": False, "error": error, "step": step}))
    sys.exit(1)


def log(msg):
    print(msg, file=sys.stderr)


# ── AWS4-HMAC-SHA256 签名 ──────────────────────────────────

def _sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()


def _signing_key(secret, date_stamp, region, service):
    k = _sign(('AWS4' + secret).encode('utf-8'), date_stamp)
    k = _sign(k, region)
    k = _sign(k, service)
    return _sign(k, 'aws4_request')


def aws4_auth(method, url, body, ak, sk, token, region='cn-north-1', service='vod'):
    from urllib.parse import urlparse, parse_qs

    parsed = urlparse(url)
    uri = parsed.path or '/'
    qs = '&'.join(f'{k}={v[0]}' for k, v in sorted(parse_qs(parsed.query, keep_blank_values=True).items()))

    now = datetime.datetime.utcnow()
    amz_date = now.strftime('%Y%m%dT%H%M%SZ')
    date_stamp = now.strftime('%Y%m%d')

    raw = body.encode('utf-8') if isinstance(body, str) else (body or b'')
    payload_hash = hashlib.sha256(raw).hexdigest()

    headers = {
        'host': parsed.hostname,
        'x-amz-content-sha256': payload_hash,
        'x-amz-date': amz_date,
        'x-amz-security-token': token,
    }
    signed_keys = sorted(headers)
    canonical = (
        f"{method}\n{uri}\n{qs}\n"
        + ''.join(f'{k}:{headers[k]}\n' for k in signed_keys)
        + f"\n{';'.join(signed_keys)}\n{payload_hash}"
    )
    scope = f'{date_stamp}/{region}/{service}/aws4_request'
    sts = f"AWS4-HMAC-SHA256\n{amz_date}\n{scope}\n{hashlib.sha256(canonical.encode()).hexdigest()}"
    sig = hmac.new(_signing_key(sk, date_stamp, region, service), sts.encode(), hashlib.sha256).hexdigest()

    return {
        'authorization': f"AWS4-HMAC-SHA256 Credential={ak}/{scope}, SignedHeaders={';'.join(signed_keys)}, Signature={sig}",
        'x-amz-date': amz_date,
        'x-amz-content-sha256': payload_hash,
        'x-amz-security-token': token,
    }


# ── 上传四步流水线 ─────────────────────────────────────────

def load_cookies():
    if not os.path.exists(CONFIG_PATH):
        fail(f"Cookie 配置不存在: {CONFIG_PATH}。请先创建 cookies.json", 'config')
    with open(CONFIG_PATH) as f:
        return json.load(f)


def step1_get_token(cookies):
    """获取 STS 临时凭证"""
    log('[Step 1] 获取上传凭证...')
    resp = requests.post(
        'https://jimeng.jianying.com/mweb/v1/get_upload_token',
        params={'aid': '513695', 'web_version': '7.5.0', 'da_version': '3.3.9', 'aigc_features': 'app_lip_sync'},
        headers={
            'content-type': 'application/json',
            'appid': '513695', 'appvr': '8.4.0', 'pf': '7',
            'lan': 'zh-Hans', 'loc': 'cn', 'sign-ver': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        },
        cookies=cookies,
        json={"scene": 1},
        timeout=15,
    )
    data = resp.json()
    if data.get('ret') != '0':
        fail(f"获取凭证失败: {data.get('errmsg', 'unknown')}", 'get_token')
    d = data['data']
    log(f'  AK: {d["access_key_id"][:16]}...  过期: {d["expired_time"]}')
    return d


def step2_apply_upload(creds, file_size, file_type):
    """申请上传地址"""
    log(f'[Step 2] 申请上传地址 (type={file_type}, size={file_size})...')
    url = (
        f"https://vod.bytedanceapi.com/"
        f"?Action=ApplyUploadInner&Version=2020-11-19"
        f"&SpaceName={creds['space_name']}&FileType={file_type}"
        f"&IsInner=1&FileSize={file_size}"
    )
    auth_h = aws4_auth('GET', url, None, creds['access_key_id'], creds['secret_access_key'], creds['session_token'])
    resp = requests.get(url, headers={
        **auth_h,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'origin': 'https://jimeng.jianying.com',
        'referer': 'https://jimeng.jianying.com/',
    }, timeout=15)
    result = resp.json()
    if 'Result' not in result:
        fail(f"ApplyUpload 失败: {result.get('ResponseMetadata', {}).get('Error', result)}", 'apply_upload')

    addr = result['Result'].get('InnerUploadAddress') or result['Result'].get('UploadAddress')
    if not addr or not addr.get('UploadNodes'):
        fail('无上传节点返回', 'apply_upload')

    node = addr['UploadNodes'][0]
    info = node['StoreInfos'][0]
    log(f'  Vid: {node["Vid"]}  Host: {node["UploadHost"]}  Type: {node.get("Type")}')
    return {
        'vid': node['Vid'],
        'store_uri': info['StoreUri'],
        'auth': info['Auth'],
        'host': node['UploadHost'],
        'session_key': node['SessionKey'],
    }


def step3_upload_to_tos(upload_info, filepath, file_size):
    """分片上传到 TOS"""
    log(f'[Step 3] 分片上传到 TOS...')
    base = f"https://{upload_info['host']}/upload/v1/{upload_info['store_uri']}"
    auth = upload_info['auth']
    common_h = {
        'Authorization': auth,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Origin': 'https://jimeng.jianying.com',
        'Referer': 'https://jimeng.jianying.com/',
    }

    # init
    resp = requests.post(f"{base}?uploadmode=part&phase=init", headers={**common_h, 'Content-Type': 'application/octet-stream'}, timeout=15)
    init_data = resp.json()
    upload_id = init_data.get('data', {}).get('uploadid', '')
    if not upload_id:
        fail(f"TOS init 失败: {init_data}", 'tos_init')
    log(f'  uploadID: {upload_id}')

    # transfer
    crc_parts = []
    part_num = 0
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            part_num += 1
            crc_hex = f"{zlib.crc32(chunk) & 0xffffffff:08x}"
            log(f'  分片 {part_num}: {len(chunk)} bytes, CRC32={crc_hex}')

            resp = requests.post(
                f"{base}?uploadmode=part&phase=transfer&uploadid={upload_id}&part_number={part_num}",
                headers={**common_h, 'Content-Type': 'application/octet-stream', 'Content-CRC32': crc_hex},
                data=chunk,
                timeout=60,
            )
            tr = resp.json()
            if tr.get('code') != 2000:
                fail(f"分片 {part_num} 上传失败: {tr}", 'tos_transfer')
            crc_parts.append(f"{part_num}:{crc_hex}")

    # finish
    finish_body = ','.join(crc_parts)
    resp = requests.post(
        f"{base}?uploadmode=part&phase=finish&uploadid={upload_id}",
        headers={**common_h, 'Content-Type': 'text/plain;charset=UTF-8'},
        data=finish_body,
        timeout=15,
    )
    fr = resp.json()
    if fr.get('code') != 2000:
        fail(f"TOS finish 失败: {fr}", 'tos_finish')
    log(f'  finish: OK (hash={fr.get("data", {}).get("hash", "?")})')


def step4_commit(creds, upload_info):
    """提交上传确认"""
    log('[Step 4] 提交确认...')
    url = f"https://vod.bytedanceapi.com/?Action=CommitUploadInner&Version=2020-11-19&SpaceName={creds['space_name']}"
    body = json.dumps({"SessionKey": upload_info['session_key'], "Functions": []})
    auth_h = aws4_auth('POST', url, body, creds['access_key_id'], creds['secret_access_key'], creds['session_token'])
    resp = requests.post(url, headers={
        **auth_h,
        'content-type': 'text/plain;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'origin': 'https://jimeng.jianying.com',
        'referer': 'https://jimeng.jianying.com/',
    }, data=body, timeout=15)

    result = resp.json()
    if 'Result' not in result:
        fail(f"CommitUpload 失败: {result}", 'commit')

    results = result['Result'].get('Results', [{}])
    entry = results[0] if results else {}
    meta = entry.get('VideoMeta', {})
    vid = entry.get('Vid', upload_info['vid'])
    log(f'  Vid: {vid}')
    if meta.get('Width'):
        log(f'  {meta["Width"]}x{meta["Height"]}, {meta.get("Duration", 0):.1f}s, {meta.get("Format", "?")}')
    return vid, meta


def detect_type(filepath):
    """返回 (vod_file_type, actual_media_type)"""
    ext = os.path.splitext(filepath)[1].lower()
    vod_type = EXT_TO_TYPE.get(ext)
    media_type = EXT_TO_MEDIA.get(ext)
    if not vod_type:
        fail(f"无法识别文件类型: {ext}，支持: video/audio/image", 'detect_type')
    return vod_type, media_type


def main():
    parser = argparse.ArgumentParser(description='即梦 VOD 媒体上传')
    parser.add_argument('file', help='要上传的文件路径')
    parser.add_argument('--type', choices=['video', 'audio', 'image'], help='文件类型 (默认自动检测)')
    parser.add_argument('--cookies', help='cookies.json 路径 (默认: skills/upload-media/cookies.json)')
    args = parser.parse_args()

    filepath = os.path.abspath(args.file)
    if not os.path.exists(filepath):
        fail(f"文件不存在: {filepath}", 'input')

    file_size = os.path.getsize(filepath)

    if args.cookies:
        global CONFIG_PATH
        CONFIG_PATH = args.cookies

    if args.type:
        # 用户强制指定: 音频也映射到 video
        vod_type = 'video' if args.type in ('video', 'audio') else args.type
        media_type = args.type
    else:
        vod_type, media_type = detect_type(filepath)

    log(f'文件: {filepath}')
    log(f'大小: {file_size} bytes ({file_size/1024/1024:.1f} MB)')
    log(f'媒体类型: {media_type} (VOD FileType={vod_type})')
    log('')

    cookies = load_cookies()
    creds = step1_get_token(cookies)
    upload_info = step2_apply_upload(creds, file_size, vod_type)
    step3_upload_to_tos(upload_info, filepath, file_size)
    vid, meta = step4_commit(creds, upload_info)

    # JSON 结果输出到 stdout
    print(json.dumps({
        "ok": True,
        "vid": vid,
        "uri": meta.get('Uri', ''),
        "meta": {
            "width": meta.get('Width') or meta.get('OriginWidth', 0),
            "height": meta.get('Height') or meta.get('OriginHeight', 0),
            "duration": meta.get('Duration', 0),
            "format": meta.get('Format', ''),
            "codec": meta.get('Codec', ''),
            "size": meta.get('Size', file_size),
            "md5": meta.get('Md5', ''),
            "file_type": media_type,
        },
    }))


if __name__ == '__main__':
    main()
