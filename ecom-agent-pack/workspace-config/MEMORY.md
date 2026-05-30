# MEMORY.md - 长期记忆

## 已验证的出图类型

- 切头街拍 (Headless Street Style) 场景图 ✓
- 极简水泥光影平铺静物图 ✓
- 淘宝标准尺寸主图 (800×800, 750×1000) ✓
- 极简画框留白排版 ✓

## 工作流状态

### ⚠️ 抠图合成流 — 已否决（2026-03-05）
- Rembg 抠图 → AI 背景 → 合成的方案**被用户否决**
- 问题：割裂感太重、光影不匹配、透视不一致
- 用户原话："割裂感太重了，不要用抠图的这个作法了"
- **不要再推荐或使用这个方案**
- 详见 aesthetic-fragments.md F-007

### ✓ AI 重绘流（可用，有条件）
- 方案：先提取线稿/色稿 → 再结合提示词重绘
- 直接丢原图会破坏版型（详见 F-004），必须有方法地做

### ✓ 纯 AI 生图（主推）
- 用 Banana + 精准 prompt 直出场景图
- 风格参考：aesthetic-patterns.md

## 关键教训

1. **抠图合成不可用** — 用户已明确否决，见 F-007
2. **AI 重绘要有方法** — 提取线稿/色稿再重绘，不是直接丢图（F-004）
3. **Prompt 语言跟模型走** — 即梦用中文，Nano Banana 用英文
4. **先出图，后说话** — 不写长篇分析
5. **审美方向以用户纠正为准** — 被纠正后立即调整，写入 aesthetic-fragments.md

## 设计脚本

持久化路径：`/root/.openclaw/scripts/design-pipeline/`（不是 /tmp/，/tmp/ 会被清除）

| 脚本 | 用途 |
|------|------|
| `create_multi_pants.py` | 白底图 + AI 空景 + 落地阴影合成 |
| `create_deck.py` | 16:9 画册 Deck 自动排版 |
| `editorial_layout.py` | 编辑风排版 |
| `composite.py` | 基础合成工具 |

运行方式：`cd /root/.openclaw/scripts/design-pipeline && python3 <脚本名>`

## 服务器环境

- Chrome 145.0.7632.75 @ `/usr/bin/google-chrome-stable`
- Xvfb :99 (1920x1080) 已配置开机自启
- Brave Search 已启用

## 品牌资料索引

| 品牌 | 档案路径 | 资产目录 | 状态 |
|------|---------|---------|------|
| SEEK WITHIN | `/root/.openclaw/memory/brand-seek-within.md` | `/root/.openclaw/design-assets/seek-within/` | 完整 |
| 1747 大话国潮 | `/root/.openclaw/memory/brand-1747.md` | `/root/.openclaw/design-assets/1747/` | 部分填充 |

## 图片资产

用图之前先查 asset-catalog.json，不要问用户重新发图。

- **SEEK WITHIN 资产索引**：`/root/.openclaw/design-assets/seek-within/asset-catalog.json`
- **产品图（用户发来）**：`/root/.openclaw/design-assets/seek-within/photos-inbound/`
- **原始拍摄**：`/root/.openclaw/design-assets/seek-within/photos/`
- **风格参考图**：`/root/.openclaw/design-assets/seek-within/references/`
- **目录 PDF**：`/root/.openclaw/design-assets/seek-within/catalogs/`

关键图片快查（先查 asset-catalog.json，再取文件）：
- 裤子平铺白底：`photos-inbound/sw-pants-flatlay-white-bg.jpg`
- 裤子男模侧面x2：`photos-inbound/sw-pants-male-model-side-view-01.jpg` / `sw-pants-male-model-side-view-02.jpg`
- 裤子男模行走：`photos-inbound/sw-pants-male-model-walking-01.jpg`
- 裤子男模行走高清：`photos-inbound/sw-pants-male-model-walking-hires.jpg`（4045x6067）
- 裤子户外庭院场景：`photos-inbound/sw-pants-male-model-outdoor-courtyard.jpg`
- 裤脚抽绳细节：`photos-inbound/sw-pants-hem-drawstring-detail.jpg`
- 裤腰细节：`photos-inbound/sw-black-wide-leg-drawstring-pants-main.jpg`
- PIMA TEE 详情页截图（非原图）：`photos-inbound/sw-origin01-pima-cotton-tee-detail-page.jpg`
- 风织裤详情页截图（非原图）：`photos-inbound/sw-origin02-breeze-weave-pants-detail-page.jpg`
- ⚠️ **白色短袖T恤产品摄影原图缺失** — 历史session发过但未存档，需要用户重新发送
