#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Google 图片搜索 → alicdn URL 提取 → 高清图下载

通过 Google Image Search 搜索品牌关键词，从返回 HTML 中提取
alicdn.com 的商品图片 URL，去掉尺寸后缀后下载高清原图。

⚠️  备选方案 — Google 搜索结果可能不准确，下载的图片必须让用户确认！

用法:
    # 基本搜索（提取所有 alicdn 图片）
    uv run google_images.py --keyword '1747 淘宝 女装' -o /tmp/brand_images

    # 精准过滤（只保留指定 seller_id 的图片）
    uv run google_images.py \\
        --keyword '"1747" 大话国潮 淘宝' \\
        --seller-id 2207758505229 \\
        -o /tmp/brand_images --max 15

    # 多关键词搜索（自动合并去重）
    uv run google_images.py \\
        --keyword '"1747" 淘宝 品牌' \\
        --keyword 'site:dbqy8.com 1747' \\
        --seller-id 2207758505229 \\
        -o /tmp/brand_images

原理:
    1. 向 Google Image Search 发送 HTTP 请求（桌面 Chrome UA）
    2. 用正则从 HTML 中提取 img.alicdn.com / gw.alicdn.com / cbu01.alicdn.com URL
    3. 如果提供了 --seller-id，只保留包含该 ID 的 URL
    4. 去掉尾部尺寸后缀（_310x310.jpg 等），获取原图 URL
    5. 下载图片到输出目录，输出 JSON manifest
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GOOGLE_SEARCH_URL = "https://www.google.com/search"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

IMAGE_DOWNLOAD_HEADERS = {
    "User-Agent": HEADERS["User-Agent"],
    "Referer": "https://www.taobao.com/",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# alicdn 域名模式
ALICDN_PATTERN = re.compile(
    r"(?:img|gw|cbu01)\.alicdn\.com/"
    r"(?:imgextra|bao/uploaded|img/ibank)"
    r"/[^\s\"'\\&<>]+"
)

# alicdn URL 中的唯一图片 ID（用于去重）
IMAGE_ID_PATTERN = re.compile(r"(O1CN01\w+|O9\w{20,})")

# 尾部尺寸后缀（需要移除以获取原图）
SIZE_SUFFIX_PATTERN = re.compile(
    r"[._]"                          # 分隔符: . 或 _
    r"(?:\d+x\d+q?\d*"              # 310x310 / 500x500q90
    r"|q\d+)"                        # q50
    r"(?:\.\w+)?$"                   # 可选的额外后缀 .jpg / .webp
)

# 更精确: 先去掉 _310x310.jpg / _q50.jpg_.webp 等
TRAILING_RESIZE = re.compile(
    r"(?:"
    r"_\d+x\d+(?:q\d+)?(?:\.\w+)?"  # _310x310.jpg / _500x500q90
    r"|_q\d+(?:\.\w+)?(?:_\.webp)?"  # _q50.jpg_.webp
    r"|\.220x220(?:\.\w+)?"          # .220x220.jpg
    r")$"
)


def log(msg: str) -> None:
    print(f"[google-images] {msg}", file=sys.stderr, flush=True)


# ---------------------------------------------------------------------------
# Google 搜索
# ---------------------------------------------------------------------------

def search_google_images(keyword: str, timeout: int = 20) -> str:
    """发送 Google Image Search 请求，返回 HTML 内容。"""
    params = urllib.parse.urlencode({"q": keyword, "tbm": "isch"})
    url = f"{GOOGLE_SEARCH_URL}?{params}"
    log(f"搜索: {keyword}")
    log(f"  URL: {url}")

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        html = resp.read().decode("utf-8", errors="ignore")
        log(f"  返回 {len(html):,} bytes")
        return html
    except urllib.error.HTTPError as e:
        log(f"  HTTP 错误: {e.code} — Google 可能要求验证码")
        return ""
    except Exception as e:
        log(f"  请求失败: {e}")
        return ""


# ---------------------------------------------------------------------------
# URL 提取与清洗
# ---------------------------------------------------------------------------

def extract_alicdn_urls(html: str, seller_id: str | None = None) -> list[str]:
    """从 HTML 中提取 alicdn 图片 URL。

    如果提供了 seller_id，只保留包含该 ID 的 URL。
    """
    if not html:
        return []

    raw_urls = ALICDN_PATTERN.findall(html)
    log(f"  原始 alicdn URL: {len(raw_urls)} 个")

    # 补全协议头
    urls = []
    for u in raw_urls:
        if not u.startswith("http"):
            u = "https://" + u
        urls.append(u)

    # 按 seller_id 过滤
    if seller_id:
        filtered = [u for u in urls if seller_id in u]
        log(f"  seller_id={seller_id} 过滤后: {len(filtered)} 个")
        urls = filtered

    # 去重（基于图片 ID 或完整路径）
    seen: set[str] = set()
    unique: list[str] = []
    for u in urls:
        # 优先用 O1CN01... 作为去重 key
        match = IMAGE_ID_PATTERN.search(u)
        key = match.group(1) if match else u.split("?")[0]
        if key not in seen:
            seen.add(key)
            unique.append(u)

    log(f"  去重后: {len(unique)} 个")
    return unique


def clean_url(url: str) -> str:
    """移除 alicdn URL 的尺寸后缀，获取原图 URL。

    示例:
        .../xxx.jpg_310x310.jpg  → .../xxx.jpg
        .../xxx.png_q50.jpg_.webp → .../xxx.png
        .../xxx.jpg_500x500q90  → .../xxx.jpg
        .../xxx.220x220.jpg     → .../xxx.jpg (ibank 格式)
    """
    # 去掉 URL 参数
    url = url.split("?")[0]

    # 处理 _q50.jpg_.webp 这类双后缀
    url = re.sub(r"_q\d+\.\w+_\.\w+$", "", url)

    # 处理 _310x310.jpg / _500x500q90 / .220x220.jpg
    url = TRAILING_RESIZE.sub("", url)

    # 如果 URL 最后没有扩展名了（被清掉了），猜一个
    if not re.search(r"\.\w{3,4}$", url):
        url += ".jpg"

    return url


# ---------------------------------------------------------------------------
# 下载
# ---------------------------------------------------------------------------

def download_image(url: str, output_path: Path, timeout: int = 15) -> int:
    """下载单张图片，返回文件大小（字节）。失败返回 0。"""
    try:
        req = urllib.request.Request(url, headers=IMAGE_DOWNLOAD_HEADERS)
        resp = urllib.request.urlopen(req, timeout=timeout)
        data = resp.read()

        # 检查防盗链占位图
        if len(data) < 500:
            log(f"  SKIP {output_path.name}: 疑似防盗链 ({len(data)} bytes)")
            return 0

        with open(output_path, "wb") as f:
            f.write(data)
        return len(data)
    except Exception as e:
        log(f"  FAIL {output_path.name}: {e}")
        return 0


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Google 图片搜索 → alicdn URL 提取 → 高清图下载\n"
            "⚠️  备选方案: 搜索结果可能不准确，下载的图片必须让用户确认！"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--keyword", "-k",
        action="append",
        required=True,
        help="搜索关键词（可多次指定，自动合并结果）",
    )
    parser.add_argument(
        "--seller-id", "-s",
        default=None,
        help="淘宝卖家 ID（精准过滤，只保留该卖家的图片）",
    )
    parser.add_argument(
        "--output", "-o",
        default="/tmp/store-teardown/google_images",
        help="输出目录（默认: /tmp/store-teardown/google_images）",
    )
    parser.add_argument(
        "--max", "-m",
        type=int,
        default=15,
        help="最多下载几张（默认: 15）",
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ── 1. 搜索 ──
    all_urls: list[str] = []
    seen_keys: set[str] = set()

    for keyword in args.keyword:
        html = search_google_images(keyword)
        urls = extract_alicdn_urls(html, seller_id=args.seller_id)

        # 跨关键词去重
        for u in urls:
            match = IMAGE_ID_PATTERN.search(u)
            key = match.group(1) if match else u.split("?")[0]
            if key not in seen_keys:
                seen_keys.add(key)
                all_urls.append(u)

    if not all_urls:
        log("未找到任何 alicdn 图片 URL")
        if args.seller_id:
            log(f"提示: 尝试去掉 --seller-id 参数搜索更多结果")
        # 输出空 manifest
        print(json.dumps({"images": [], "total": 0}, ensure_ascii=False))
        sys.exit(0)

    log(f"合计找到 {len(all_urls)} 个唯一 URL，准备下载前 {args.max} 个")

    # ── 2. 清洗 URL 并下载 ──
    to_download = all_urls[: args.max]
    manifest: list[dict] = []

    for i, raw_url in enumerate(to_download):
        hd_url = clean_url(raw_url)

        # 猜测扩展名
        ext = ".jpg"
        if ".png" in hd_url:
            ext = ".png"
        elif ".webp" in hd_url:
            ext = ".webp"

        filename = f"google_{i + 1:02d}{ext}"
        filepath = output_dir / filename

        log(f"[{i + 1}/{len(to_download)}] 下载 {hd_url[:100]}...")
        size = download_image(hd_url, filepath)

        if size > 0:
            manifest.append({
                "filename": filename,
                "filepath": str(filepath),
                "original_url": raw_url,
                "hd_url": hd_url,
                "size_bytes": size,
                "size_kb": round(size / 1024, 1),
            })
            log(f"  OK   {filename}: {size:,} bytes")

    # ── 3. 输出 manifest ──
    result = {
        "warning": "Google 搜索结果可能不准确，请让用户确认图片后再用于分析",
        "keywords": args.keyword,
        "seller_id": args.seller_id,
        "total_found": len(all_urls),
        "downloaded": len(manifest),
        "output_dir": str(output_dir),
        "images": manifest,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    log(f"完成: {len(manifest)}/{len(to_download)} 张下载成功 → {output_dir}")


if __name__ == "__main__":
    main()
