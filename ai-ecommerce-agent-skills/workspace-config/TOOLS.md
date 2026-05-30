# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

---

## 淘宝/电商 工具链（重要！必读）

### 搜索商品/品牌/店铺 → 用买手技能（免费、2秒出结果）

```bash
cd /root/.openclaw/skills/taobao && uv run scripts/main.py search --source=1 --keyword='关键词'
```

source 参数：1=淘宝/天猫, 2=京东, 3=拼多多, 7=抖音, 8=快手

返回 CSV：idx,goodsId,title,shopName,originalPrice,actualPrice,couponPrice,commission,monthSales,picUrl

### 下载商品图片 → 用 download_images.py（绕过CDN防盗链）

**绝对不能用 curl 直接下载 alicdn.com 图片！** 会返回 1x1 GIF。

```bash
# 先将 picUrl 写入文件（每行一个URL）
cat > /tmp/urls.txt << 'EOF'
https://img.alicdn.com/bao/uploaded/xxx.jpg
EOF

# 用脚本下载
cd /root/.openclaw/skills/store-teardown && uv run scripts/download_images.py -o /tmp/images -f /tmp/urls.txt --max 15
```

### 抓取淘宝页面 → 用 taobao_fetch.py（通过ScraperAPI代理）

```bash
cd /root/.openclaw/skills/store-teardown && uv run scripts/taobao_fetch.py "<url>" -o /tmp/output --max-images 20
```

### 禁止事项（血泪教训，别再踩坑！）

- **禁止** 用浏览器打开淘宝/天猫 → 100%被反爬拦截，白白浪费时间
- **禁止** 安装 Playwright 或 selenium → 服务器上装不了
- **禁止** 用 Google/Bing/百度 搜索淘宝店铺 → 太慢且经常被 reCAPTCHA 拦截
- **禁止** 用 curl 下载 alicdn.com 图片 → 会被防盗链返回 1x1 GIF
- **禁止** 自己写 Python 爬虫脚本 → 已有现成工具，别重复造轮子

### 工作流示例

用户说 "找一下1747的店铺风格"：

1. `cd /root/.openclaw/skills/taobao && uv run scripts/main.py search --source=1 --keyword='1747'`
2. 从结果提取 picUrl 写入 /tmp/urls.txt
3. `cd /root/.openclaw/skills/store-teardown && uv run scripts/download_images.py -o /tmp/store-teardown/images -f /tmp/urls.txt`
4. 读取 SKILL.md: `cat /root/.openclaw/skills/store-teardown/SKILL.md` 然后按流程做视觉分析

---

## General Notes

Add whatever helps you do your job. This is your cheat sheet.

### Google 图片搜索采集品牌素材 → 用 google_images.py（⚠️ 备选方案）

**仅在买手搜索无法获取足够素材（如宣传海报、Banner）时使用。**
**Google 搜索结果可能不准确，下载的图片必须让用户确认后才能使用！**

```bash
cd /root/.openclaw/skills/store-teardown && uv run scripts/google_images.py \
  --keyword '"品牌名" 淘宝 品牌' \
  --seller-id <卖家ID> \
  -o /tmp/store-teardown/google_images --max 15
```

seller_id 可选，有则精准过滤。多个关键词用多个 --keyword 参数。
