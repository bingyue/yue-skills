#!/usr/bin/env python3
"""
电商设计模版渲染引擎
HTML模版 → Playwright → 高质量PNG图片
"""

import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


SCRIPT_DIR = Path(__file__).parent
TEMPLATES_DIR = SCRIPT_DIR.parent / "templates"

# 风格配色
THEMES = {
    "tech": {
        "bg": "#0a0a1a", "bg2": "#16213e", "text": "#ffffff",
        "text2": "#b0bec5", "accent": "#00d4ff", "accent2": "#7c4dff",
        "gradient": "linear-gradient(135deg, #0a0a1a 0%, #16213e 50%, #0f3460 100%)",
    },
    "minimal": {
        "bg": "#ffffff", "bg2": "#f8f9fa", "text": "#212121",
        "text2": "#757575", "accent": "#000000", "accent2": "#424242",
        "gradient": "linear-gradient(180deg, #ffffff 0%, #f5f5f5 100%)",
    },
    "fresh": {
        "bg": "#f1f8e9", "bg2": "#e8f5e9", "text": "#2e7d32",
        "text2": "#558b2f", "accent": "#4caf50", "accent2": "#81c784",
        "gradient": "linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
    },
    "luxury": {
        "bg": "#1a1a1a", "bg2": "#2c2c2c", "text": "#f5e6cc",
        "text2": "#c9a96e", "accent": "#c9a96e", "accent2": "#d4af37",
        "gradient": "linear-gradient(135deg, #1a1a1a 0%, #2c2c2c 100%)",
    },
    "promo": {
        "bg": "#ff1744", "bg2": "#ff6b35", "text": "#ffffff",
        "text2": "#fff9c4", "accent": "#ffd93d", "accent2": "#ff6b35",
        "gradient": "linear-gradient(135deg, #ff1744 0%, #ff6b35 50%, #ffd93d 100%)",
    },
    "pink": {
        "bg": "#fce4ec", "bg2": "#f8bbd0", "text": "#880e4f",
        "text2": "#ad1457", "accent": "#e91e63", "accent2": "#f06292",
        "gradient": "linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%)",
    },
    "ins": {
        "bg": "#fafafa", "bg2": "#f5f0eb", "text": "#262626",
        "text2": "#8e8e8e", "accent": "#e1306c", "accent2": "#833ab4",
        "gradient": "linear-gradient(135deg, #fafafa 0%, #f5f0eb 100%)",
    },
}

# 平台尺寸
SIZES = {
    "taobao_detail": (790, None),
    "taobao_main": (800, 800),
    "taobao_banner": (1920, 600),
    "jd_detail": (990, None),
    "pdd_main": (750, 750),
    "xiaohongshu": (1080, 1440),
    "douyin": (1080, 1920),
    "wechat_cover": (900, 383),
    "wechat_content": (1080, None),
    "poster_standard": (750, 1334),
}

TEMPLATE_MAP = {
    "detail_page": "detail-page.html",
    "poster": "poster.html",
    "social": "social-post.html",
    "template": "brand-template.html",
    "banner": "banner.html",
    "main_image": "main-image.html",
}


def fill_template(html: str, variables: dict) -> str:
    """简单的 {{var}} 模版替换"""
    for key, value in variables.items():
        html = html.replace(f"{{{{{key}}}}}", str(value))
    return html


def render_to_image(html: str, output: str, width: int, height: int | None, scale: float = 2.0) -> str:
    """Playwright 渲染 HTML → PNG"""
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": width, "height": height or 1080},
            device_scale_factor=scale,
        )
        page.set_content(html, wait_until="networkidle")
        page.wait_for_timeout(800)

        if height is None:
            real_h = page.evaluate("() => document.documentElement.scrollHeight")
            page.set_viewport_size({"width": width, "height": real_h})
            page.wait_for_timeout(300)

        page.screenshot(path=str(out), full_page=(height is None))
        browser.close()

    kb = out.stat().st_size / 1024
    print(f"✅ 设计完成!")
    print(f"   文件: {out}")
    print(f"   大小: {kb:.1f} KB")
    print(f"   尺寸: {width}x{height or 'auto'} @{scale}x")
    return str(out)


def build_selling_points_html(points_str: str) -> str:
    """将 '卖点1|卖点2|卖点3' 转为 HTML"""
    if not points_str:
        return ""
    icons = ["✦", "◆", "●", "▸", "★", "◇"]
    parts = [p.strip() for p in points_str.split("|") if p.strip()]
    html = ""
    for i, pt in enumerate(parts):
        html += f'<div class="selling-point"><span class="icon">{icons[i % len(icons)]}</span><span>{pt}</span></div>\n'
    return html


def main():
    parser = argparse.ArgumentParser(description="电商模版渲染")
    parser.add_argument("--type", required=True, choices=list(TEMPLATE_MAP.keys()))
    parser.add_argument("--product-name", default="产品名称")
    parser.add_argument("--selling-points", default="")
    parser.add_argument("--price", default="")
    parser.add_argument("--original-price", default="")
    parser.add_argument("--title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--discount", default="")
    parser.add_argument("--date-range", default="")
    parser.add_argument("--description", default="")
    parser.add_argument("--style", default="minimal")
    parser.add_argument("--platform", default="xiaohongshu")
    parser.add_argument("--template-name", default="default")
    parser.add_argument("--tags", default="")
    parser.add_argument("--author", default="")
    parser.add_argument("--product-image", default="")
    parser.add_argument("--brand-logo", default="")
    parser.add_argument("--size", default="")
    parser.add_argument("--scale", type=float, default=2.0)
    parser.add_argument("--output", default="/tmp/design_output/result.png")
    args = parser.parse_args()

    # 确定尺寸
    if args.size and args.size in SIZES:
        width, height = SIZES[args.size]
    elif args.size and "x" in args.size:
        parts = args.size.split("x")
        width = int(parts[0])
        height = int(parts[1]) if parts[1] != "auto" else None
    else:
        type_defaults = {
            "detail_page": (790, None), "poster": (750, 1334),
            "social": SIZES.get(args.platform, (1080, 1440)),
            "banner": (1920, 600), "main_image": (800, 800),
            "template": (790, None),
        }
        width, height = type_defaults.get(args.type, (790, None))

    # 主题
    theme = THEMES.get(args.style, THEMES["minimal"])

    # 构建模版变量
    variables = {
        "product_name": args.product_name,
        "selling_points_html": build_selling_points_html(args.selling_points),
        "price": args.price,
        "original_price": args.original_price,
        "title": args.title or args.product_name,
        "subtitle": args.subtitle,
        "discount": args.discount,
        "date_range": args.date_range,
        "description": args.description,
        "platform": args.platform,
        "tags": args.tags,
        "author": args.author,
        "product_image": args.product_image,
        "brand_logo": args.brand_logo,
        "template_name": args.template_name,
    }
    # 注入主题色
    for k, v in theme.items():
        variables[f"theme_{k}"] = v

    # 加载模版
    tpl_file = TEMPLATES_DIR / TEMPLATE_MAP[args.type]
    if not tpl_file.exists():
        print(f"❌ 模版不存在: {tpl_file}")
        sys.exit(1)

    html = fill_template(tpl_file.read_text(encoding="utf-8"), variables)

    # 渲染
    render_to_image(html, args.output, width, height, args.scale)


if __name__ == "__main__":
    main()
