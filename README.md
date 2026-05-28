<div align="center">

**中文** · [English](./README.en.md)

# 🧰 Yue Skills

#### 对外实用 Skill 分类集合：研究输入 · 内容加工 · 视觉生成 · 多平台分发

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-39-10B981?style=for-the-badge)](#-skills-分类总览)
[![Prompts](https://img.shields.io/badge/Prompts-1-F59E0B?style=for-the-badge)](#-prompts)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

</div>

Yue Skills 聚焦"真实可落地"的 AI 生产链路：从信息输入、内容加工、视觉生成到多平台发布，提供可直接安装与复用的 Skill。

---

## 📦 安装

在支持 Skills 的 Agent 中直接安装单个目录：

```text
安装这个 skill：<你的仓库地址>/tree/main/<skill-name>
```

例如：`diagram-svg-generator`、`publish-wechat-official`、`image-generate-multiapi`、`workflow-neat-sync`。

---

## 🗂️ Skills 分类总览

### A. 研究与信息输入

> 抓取、提取、翻译、研究——信息链路的起点。

| Skill | 用途 | 路径 |
|---|---|---|
| `news-aihot-daily` | AI 热点日报与动态检索（aihot.virxact.com） | [`./news-aihot-daily`](./news-aihot-daily) |
| `web-markdown-extract` | 任意网页抓取转 Markdown | [`./web-markdown-extract`](./web-markdown-extract) |
| `danger-x-markdown-export` | X/Twitter 内容转存 Markdown | [`./danger-x-markdown-export`](./danger-x-markdown-export) |
| `youtube-transcript-extract` | YouTube 字幕与封面提取 | [`./youtube-transcript-extract`](./youtube-transcript-extract) |
| `youtube-video-clipper` | YouTube 视频智能剪辑与中英双语字幕 | [`./youtube-video-clipper`](./youtube-video-clipper) |
| `wechat-group-summary` | 微信群聊记录摘要与群体画像 | [`./wechat-group-summary`](./wechat-group-summary) |
| `text-translate-workflow` | 多模式翻译：快翻 / 常规 / 精修三档 | [`./text-translate-workflow`](./text-translate-workflow) |
| `research-hv-analysis` | 横纵分析法深度研究报告 | [`./research-hv-analysis`](./research-hv-analysis) |

---

### B. 文本加工与写作

> 结构整理、风格写作、多平台文案——内容生产核心。

| Skill | 用途 | 路径 |
|---|---|---|
| `markdown-format-polish` | Markdown 结构化整理与排版优化 | [`./markdown-format-polish`](./markdown-format-polish) |
| `markdown-html-wechat` | Markdown 转微信公众号兼容 HTML | [`./markdown-html-wechat`](./markdown-html-wechat) |
| `text-check-skill` | 文本敏感词扫描与合规检查 | [`./text-check-skill`](./text-check-skill) |
| `writing-khazix-style` | 卡兹克风格公众号长文写作 | [`./writing-khazix-style`](./writing-khazix-style) |
| `Viral_Writer_Skill` | 多平台爆款文案创作（公众号 / 小红书 / 抖音） | [`./Viral_Writer_Skill`](./Viral_Writer_Skill) |
| `social-account-doctor` | 自媒体账号对标拆解与仿写闭环 | [`./social-account-doctor`](./social-account-doctor) |

---

### C. 视觉生成

#### C1. 图片与插图

> 从文章配图到电商主图，覆盖内容图片全场景。

| Skill | 用途 | 路径 |
|---|---|---|
| `image-generate-multiapi` | 多模型统一文生图入口（GPT-Image / Gemini / Azure） | [`./image-generate-multiapi`](./image-generate-multiapi) |
| `danger-gemini-webapi` | Gemini Web 图片与文本能力接入（逆向） | [`./danger-gemini-webapi`](./danger-gemini-webapi) |
| `article-cover-generator` | 文章封面图生成（5 维度风格） | [`./article-cover-generator`](./article-cover-generator) |
| `article-image-illustrator` | 文章段落自动配图（位置识别 + 提示词生成） | [`./article-image-illustrator`](./article-image-illustrator) |
| `document-illustrator` | 文档内容配图（封面图 + 正文配图，支持风格锁定） | [`./document-illustrator`](./document-illustrator) |
| `ecom-product-image` | 电商全场景图片生成（主图 / 详情页 / Banner，25 种模板） | [`./ecom-product-image`](./ecom-product-image) |
| `logo-svg-generator` | SVG Logo 与品牌展示图生成（12 种背景风格） | [`./logo-svg-generator`](./logo-svg-generator) |
| `social-image-cards` | 社媒图文卡片系列生成 | [`./social-image-cards`](./social-image-cards) |
| `xhs-social-card` | 小红书图文套组 / 微信公众号封面图对生成（归藏风，瑞士风 / 杂志风） | [`./xhs-social-card`](./xhs-social-card) |
| `visual-infographic-generator` | 专业信息图生成（21 种布局） | [`./visual-infographic-generator`](./visual-infographic-generator) |
| `image-compress-optimizer` | 图片压缩优化（WebP / PNG，自动降质） | [`./image-compress-optimizer`](./image-compress-optimizer) |

#### C2. 图表与可视化

> 代码级 SVG 图表与漫画式知识表达。

| Skill | 用途 | 路径 |
|---|---|---|
| `diagram-svg-generator` | SVG 架构图 / 流程图 / 时序图（暗色主题） | [`./diagram-svg-generator`](./diagram-svg-generator) |
| `content-comic-generator` | 知识内容漫画生成（多风格） | [`./content-comic-generator`](./content-comic-generator) |

#### C3. 演示与 PPT

> 文档到演示的自动化，网页 PPT 到 AI 图片 PPT 全覆盖。

| Skill | 用途 | 路径 |
|---|---|---|
| `slides-deck-generator` | 演示页 / Slide 图片生成流程 | [`./slides-deck-generator`](./slides-deck-generator) |
| `html-ppt-guizang` | 网页横向翻页 PPT（杂志风 / 瑞士国际主义风，单 HTML） | [`./html-ppt-guizang`](./html-ppt-guizang) |
| `ppt-image-generator` | AI 生成 PPT 图片 + 可灵转场视频（Nano Banana） | [`./ppt-image-generator`](./ppt-image-generator) |

#### C4. 视频与动态

> 视频剪辑、特效包装、产品动画提示词。

| Skill | 用途 | 路径 |
|---|---|---|
| `youtube-video-clipper` | YouTube 视频智能剪辑 + 双语字幕烧录 | [`./youtube-video-clipper`](./youtube-video-clipper) |
| `video-wrapper-effects` | 访谈视频综艺特效（花字 / 卡片 / 人物条，4 种主题） | [`./video-wrapper-effects`](./video-wrapper-effects) |
| `seedance-video-prompt` | Seedance 2.0 产品动画提示词（4 种美学风格） | [`./seedance-video-prompt`](./seedance-video-prompt) |

---

### D. 发布与分发

> 内容触达最后一公里：多平台一键发布。

| Skill | 用途 | 路径 |
|---|---|---|
| `publish-wechat-official` | 发布到微信公众号（API / 草稿箱） | [`./publish-wechat-official`](./publish-wechat-official) |
| `publish-weibo-post` | 发布到微博（文字 / 图文 / 视频） | [`./publish-weibo-post`](./publish-weibo-post) |
| `publish-x-post` | 发布到 X / Twitter（正文 / 长文章） | [`./publish-x-post`](./publish-x-post) |

---

### E. 工程治理与平台能力

> 会话治理、知识同步、垂类平台 Agent 能力封装。

| Skill | 用途 | 路径 |
|---|---|---|
| `workflow-neat-sync` | 会话收尾：同步文档、CLAUDE.md 与 Agent 记忆 | [`./workflow-neat-sync`](./workflow-neat-sync) |
| `openclaw-ecommerce-skill` | OpenClaw 电商助手（商品管理 / 文案生成） | [`./openclaw-ecommerce-skill`](./openclaw-ecommerce-skill) |
| `openclaw-ecommerce-team` | OpenClaw 电商团队协作工作流 | [`./openclaw-ecommerce-team`](./openclaw-ecommerce-team) |
| `openclaw-one-person-company-skill` | OpenClaw 一人公司全流程工作流 | [`./openclaw-one-person-company-skill`](./openclaw-one-person-company-skill) |

---

### F. 兼容保留（Deprecated）

| Skill | 状态 | 替代方案 |
|---|---|---|
| `xhs-cards-legacy` | 已废弃 | → `social-image-cards` |
| `image-generate-legacy` | 已废弃 | → `image-generate-multiapi` |

---

## 🔗 推荐工作流

| 场景 | 推荐链路 |
|---|---|
| **深度研究** | `web-markdown-extract` → `text-translate-workflow` → `research-hv-analysis` |
| **公众号内容生产** | `writing-khazix-style` → `article-image-illustrator` / `document-illustrator` → `markdown-html-wechat` → `publish-wechat-official` |
| **多平台分发** | `Viral_Writer_Skill` → `social-image-cards` → `publish-x-post` + `publish-weibo-post` + `publish-wechat-official` |
| **视频内容处理** | `youtube-transcript-extract` / `youtube-video-clipper` → `video-wrapper-effects` |
| **视觉物料生成** | `ecom-product-image` / `logo-svg-generator` / `document-illustrator` → `image-compress-optimizer` |
| **演示制作** | `research-hv-analysis` → `html-ppt-guizang` / `ppt-image-generator` |

---

## 📝 Prompts

| 名称 | 说明 | 路径 |
|---|---|---|
| `横纵分析法（Prompt 版）` | 无需安装 Skill 的轻量研究模板，粘贴到任意 Deep Research 模型即用 | [`./prompts/横纵分析法.md`](./prompts/横纵分析法.md) |

---

## ⚠️ 合规提示

`danger-*` 系列涉及浏览器自动化或逆向接口，请在平台 ToS 与本地法律允许范围内使用。

---

<div align="center">

[MIT License](./LICENSE) · 可自由使用 / 修改 / 再分发

</div>
