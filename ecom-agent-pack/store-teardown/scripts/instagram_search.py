#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["instaloader"]
# ///
"""
Instagram 图片搜索采集 — Creo 美学参考工具

三种搜索模式：
  1. hashtag  — 按 hashtag 搜索最新/热门帖子（需登录获取更多结果）
  2. profile  — 抓取公开账号的最新帖子（无需登录）
  3. google   — 通过 Google 搜索 site:instagram.com（无需登录，兜底方案）

用法:
    # 按 hashtag 搜索（公开，无需登录，但结果有限）
    python3 instagram_search.py --mode hashtag --keyword "minimalistfashion" --max 10

    # 抓取公开账号最新帖子
    python3 instagram_search.py --mode profile --keyword "seekwithin_official" --max 10

    # Google 兜底搜索（最稳定）
    python3 instagram_search.py --mode google --keyword "极简女装 穿搭" --max 10

    # 多关键词 Google 搜索
    python3 instagram_search.py --mode google \
        --keyword "minimalist fashion lookbook" \
        --keyword "克制美学 穿搭" \
        --max 15

    # 使用登录 session（可获取更多 hashtag 结果）
    python3 instagram_search.py --mode hashtag --keyword "ootd" --max 20 \
        --login your_username --session-file ~/.instaloader/session

输出:
    - 图片下载到 --output 目录
    - JSON manifest 输出到 stdout
"""

import argparse
import json
import os
import re
import sys
import time
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
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
}

IMAGE_DOWNLOAD_HEADERS = {
    "User-Agent": HEADERS["User-Agent"],
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
}

# Instagram CDN URL pattern
INSTA_CDN_PATTERN = re.compile(
    r"https?://(?:scontent[^\"'\s<>]*?\.cdninstagram\.com|instagram\.[^\"'\s<>]*?/v/)"
    r"[^\"'\s<>\\]+"
)


def log(msg: str) -> None:
    print(f"[instagram] {msg}", file=sys.stderr, flush=True)


# ---------------------------------------------------------------------------
# Mode 1: Hashtag search via instaloader
# ---------------------------------------------------------------------------

def search_hashtag(keyword: str, max_count: int, output_dir: Path,
                   login: str | None = None, session_file: str | None = None) -> list[dict]:
    """Search Instagram by hashtag using instaloader."""
    try:
        import instaloader
    except ImportError:
        log("instaloader 未安装，请运行: pip3 install instaloader")
        return []

    L = instaloader.Instaloader(
        download_comments=False,
        download_geotags=False,
        download_video_thumbnails=False,
        save_metadata=False,
        post_metadata_txt_pattern="",
    )

    # Load session if available
    if login and session_file and os.path.exists(session_file):
        try:
            L.load_session_from_file(login, session_file)
            log(f"已加载登录 session: {login}")
        except Exception as e:
            log(f"加载 session 失败: {e}，将以匿名模式继续")

    # Clean hashtag (remove #)
    tag = keyword.lstrip("#").strip()
    log(f"搜索 hashtag: #{tag}")

    manifest = []
    try:
        hashtag = instaloader.Hashtag.from_name(L.context, tag)
        count = 0
        for post in hashtag.get_posts():
            if count >= max_count:
                break
            if not post.is_video:
                try:
                    url = post.url
                    filename = f"ig_hashtag_{count + 1:02d}.jpg"
                    filepath = output_dir / filename
                    L.download_pic(filepath.with_suffix(""), url, post.date_utc)
                    # instaloader adds its own extension
                    actual_files = list(output_dir.glob(f"ig_hashtag_{count + 1:02d}*"))
                    if actual_files:
                        actual_file = actual_files[0]
                        size = actual_file.stat().st_size
                        manifest.append({
                            "filename": actual_file.name,
                            "filepath": str(actual_file),
                            "source": f"https://www.instagram.com/p/{post.shortcode}/",
                            "likes": post.likes,
                            "caption": (post.caption or "")[:200],
                            "size_bytes": size,
                            "size_kb": round(size / 1024, 1),
                        })
                        log(f"  [{count + 1}/{max_count}] OK {actual_file.name} ({size:,} bytes)")
                        count += 1
                except Exception as e:
                    log(f"  SKIP: {e}")
            time.sleep(0.5)  # Rate limiting
    except Exception as e:
        log(f"hashtag 搜索失败: {e}")
        log("提示: hashtag 搜索可能需要登录，尝试 --mode google 作为替代")

    return manifest


# ---------------------------------------------------------------------------
# Mode 2: Profile download via instaloader
# ---------------------------------------------------------------------------

def search_profile(username: str, max_count: int, output_dir: Path) -> list[dict]:
    """Download recent posts from a public Instagram profile."""
    try:
        import instaloader
    except ImportError:
        log("instaloader 未安装，请运行: pip3 install instaloader")
        return []

    L = instaloader.Instaloader(
        download_comments=False,
        download_geotags=False,
        download_video_thumbnails=False,
        save_metadata=False,
        post_metadata_txt_pattern="",
    )

    username = username.lstrip("@").strip()
    log(f"抓取公开账号: @{username}")

    manifest = []
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        log(f"  {profile.full_name} | {profile.mediacount} posts | {profile.followers} followers")

        count = 0
        for post in profile.get_posts():
            if count >= max_count:
                break
            if not post.is_video:
                try:
                    url = post.url
                    filename = f"ig_profile_{count + 1:02d}.jpg"
                    filepath = output_dir / filename
                    L.download_pic(filepath.with_suffix(""), url, post.date_utc)
                    actual_files = list(output_dir.glob(f"ig_profile_{count + 1:02d}*"))
                    if actual_files:
                        actual_file = actual_files[0]
                        size = actual_file.stat().st_size
                        manifest.append({
                            "filename": actual_file.name,
                            "filepath": str(actual_file),
                            "source": f"https://www.instagram.com/p/{post.shortcode}/",
                            "likes": post.likes,
                            "caption": (post.caption or "")[:200],
                            "size_bytes": size,
                            "size_kb": round(size / 1024, 1),
                        })
                        log(f"  [{count + 1}/{max_count}] OK {actual_file.name}")
                        count += 1
                except Exception as e:
                    log(f"  SKIP: {e}")
            time.sleep(0.5)
    except Exception as e:
        log(f"profile 抓取失败: {e}")

    return manifest


# ---------------------------------------------------------------------------
# Mode 3: Google fallback search
# ---------------------------------------------------------------------------

def search_google(keywords: list[str], max_count: int, output_dir: Path) -> list[dict]:
    """Search Instagram images via Google Image Search (no login needed).

    Strategy:
    1. Google search site:instagram.com → find fbsbx proxy URLs
    2. Extract Instagram shortcodes from proxy URLs
    3. Use instaloader to download actual images from those posts
    """
    try:
        import instaloader
    except ImportError:
        log("instaloader 未安装，请运行: pip3 install instaloader")
        return []

    shortcodes: list[str] = []
    seen: set[str] = set()

    for keyword in keywords:
        query = f"site:instagram.com {keyword}"
        params = urllib.parse.urlencode({"q": query, "tbm": "isch"})
        url = f"{GOOGLE_SEARCH_URL}?{params}"
        log(f"Google 搜索: {query}")

        req = urllib.request.Request(url, headers=HEADERS)
        try:
            resp = urllib.request.urlopen(req, timeout=20)
            html = resp.read().decode("utf-8", errors="ignore")
            log(f"  返回 {len(html):,} bytes")
        except Exception as e:
            log(f"  搜索失败: {e}")
            continue

        # Extract shortcodes from fbsbx proxy URLs
        # Pattern: /instagram/<SHORTCODE>/
        codes = re.findall(
            r"/instagram/([A-Za-z0-9_-]{8,})/",
            html,
        )
        log(f"  提取到 {len(codes)} 个 shortcode")

        # Also try direct Instagram post URLs in the HTML
        direct_codes = re.findall(
            r"instagram\.com/(?:p|reel)/([A-Za-z0-9_-]+)",
            html,
        )
        codes.extend(direct_codes)

        for sc in codes:
            if sc not in seen:
                seen.add(sc)
                shortcodes.append(sc)

    log(f"合计 {len(shortcodes)} 个唯一帖子")

    if not shortcodes:
        log("未找到 Instagram 帖子")
        return []

    # Download via instaloader
    L = instaloader.Instaloader(
        download_comments=False,
        download_geotags=False,
        download_video_thumbnails=False,
        save_metadata=False,
        post_metadata_txt_pattern="",
    )

    manifest = []
    to_download = shortcodes[:max_count]

    for i, sc in enumerate(to_download):
        try:
            post = instaloader.Post.from_shortcode(L.context, sc)

            if post.is_video:
                log(f"  [{i + 1}/{len(to_download)}] SKIP {sc}: 视频")
                continue

            filename = f"ig_ref_{i + 1:02d}.jpg"
            filepath = output_dir / filename

            # Download directly via urllib (more reliable than instaloader's method)
            img_url = post.url
            req = urllib.request.Request(img_url, headers=IMAGE_DOWNLOAD_HEADERS)
            resp = urllib.request.urlopen(req, timeout=15)
            data = resp.read()

            if len(data) < 1000:
                log(f"  [{i + 1}/{len(to_download)}] SKIP {sc}: 图片太小")
                continue

            with open(filepath, "wb") as f:
                f.write(data)

            size = len(data)
            actual_file = filepath
            if size > 0:
                manifest.append({
                    "filename": actual_file.name,
                    "filepath": str(actual_file),
                    "source": f"https://www.instagram.com/p/{sc}/",
                    "shortcode": sc,
                    "likes": post.likes,
                    "caption": (post.caption or "")[:200],
                    "size_bytes": size,
                    "size_kb": round(size / 1024, 1),
                })
                log(f"  [{i + 1}/{len(to_download)}] OK {actual_file.name} ({size:,} bytes)")

            time.sleep(1)  # Rate limiting for Instagram
        except Exception as e:
            log(f"  [{i + 1}/{len(to_download)}] FAIL {sc}: {e}")

    return manifest


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Instagram 图片搜索采集 — Creo 美学参考工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--mode", "-m",
        choices=["hashtag", "profile", "google"],
        default="google",
        help="搜索模式 (default: google)",
    )
    parser.add_argument(
        "--keyword", "-k",
        action="append",
        required=True,
        help="搜索关键词/hashtag/用户名（可多次指定）",
    )
    parser.add_argument(
        "--output", "-o",
        default="/tmp/creo-references/instagram",
        help="输出目录",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=10,
        help="最多下载几张 (default: 10)",
    )
    parser.add_argument(
        "--login",
        default=None,
        help="Instagram 用户名（用于 hashtag 模式登录）",
    )
    parser.add_argument(
        "--session-file",
        default=None,
        help="instaloader session 文件路径",
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = []

    if args.mode == "hashtag":
        for kw in args.keyword:
            manifest.extend(
                search_hashtag(kw, args.max, output_dir, args.login, args.session_file)
            )
    elif args.mode == "profile":
        for kw in args.keyword:
            manifest.extend(
                search_profile(kw, args.max, output_dir)
            )
    elif args.mode == "google":
        manifest = search_google(args.keyword, args.max, output_dir)

    # Output JSON manifest
    result = {
        "mode": args.mode,
        "keywords": args.keyword,
        "downloaded": len(manifest),
        "output_dir": str(output_dir),
        "images": manifest,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    log(f"完成: {len(manifest)} 张图片 → {output_dir}")


if __name__ == "__main__":
    main()
