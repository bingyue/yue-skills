---
name: upload-media
description: "上传视频/音频/图片到即梦(Jimeng) VOD 平台并获取 Vid。支持 mp4/mp3/jpg/png 等格式，自动处理 STS 鉴权和分块上传。当需要上传媒体文件、获取视频ID、发布素材到字节跳动平台时使用。关键词：上传、即梦、VOD、视频ID、媒体文件"
metadata:
  openclaw:
    version: 1.0.0
    userInvocable: true
    emoji: "📤"
    requires:
      bins: ["python3"]
---
# 上传媒体文件到即梦 VOD

将本地视频、音频或图片文件上传到字节跳动 VOD (Video On Demand) 平台，获取 Vid 标识符。

## 支持的文件类型

| 类型 | 扩展名 |
|------|--------|
| video | mp4, mov, avi, mkv, webm, flv, wmv, m4v |
| audio | mp3, wav, aac, flac, ogg, m4a, wma |
| image | jpg, jpeg, png, gif, webp, bmp, svg |

## 使用方法

执行上传脚本：

```bash
python3 .claude/skills/upload-media/scripts/upload.py <文件路径> [--type video|audio|image]
```

- `<文件路径>`: 必需，要上传的文件绝对路径
- `--type`: 可选，强制指定文件类型。不指定时根据扩展名自动检测
- `--cookies`: 可选，自定义 cookies.json 路径

## 输出格式

**脚本输出两个流:**

- `stderr`: 人类可读的进度日志
- `stdout`: 最终一行 JSON 结果

**成功:**

```json
{
  "ok": true,
  "vid": "v03870g10004d6480qfog65tipnb6ah0",
  "uri": "tos-cn-v-148450/oxxxxxx",
  "meta": {
    "width": 1920,
    "height": 1080,
    "duration": 9.94,
    "format": "MP4",
    "codec": "h264",
    "size": 8517914,
    "md5": "52c5619242d245bd2d056ae7fe717d76",
    "file_type": "video"
  }
}
```

**失败:**

```json
{
  "ok": false,
  "error": "获取凭证失败: session expired",
  "step": "get_token"
}
```

## 使用示例

```bash
# 上传视频
python3 .claude/skills/upload-media/scripts/upload.py /path/to/video.mp4

# 上传音频
python3 .claude/skills/upload-media/scripts/upload.py /path/to/audio.mp3

# 强制指定类型
python3 .claude/skills/upload-media/scripts/upload.py /path/to/file.dat --type video
```

## 提取结果

只取 stdout 最后一行 JSON (过滤 stderr 日志):

```bash
python3 .claude/skills/upload-media/scripts/upload.py /path/to/file.mp4 2>/dev/null
```

或解析 vid:

```bash
VID=$(python3 .claude/skills/upload-media/scripts/upload.py /path/to/file.mp4 2>/dev/null | python3 -c "import sys,json; print(json.load(sys.stdin)['vid'])")
```

## Cookie 过期处理

上传依赖即梦平台的登录 Cookie。如果上传失败且 `step` 为 `get_token`，说明 Cookie 已过期。

**更新方法:**

1. 在浏览器中登录 https://jimeng.jianying.com
2. 打开 DevTools → Network → 找任意一个请求 → 复制 Cookie
3. 更新 `.claude/skills/upload-media/cookies.json` 中对应的 cookie 值

关键 Cookie 字段: `sessionid`, `sid_tt`, `uid_tt`, `odin_tt`

## 内部流程

```
1. getUploadToken     → 用 Cookie 从即梦获取 STS 临时凭证
2. ApplyUploadInner   → 用 AK/SK 签名调 VOD API，获取上传地址
3. TOS 分片上传        → 4MB 分片 + CRC32 校验，上传到 TOS 存储
4. CommitUploadInner  → 确认上传，VOD 注册视频，返回 Vid + 元数据
```
