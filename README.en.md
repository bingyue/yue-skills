<div align="center">

[中文](./README.md) · **English**

# 🧰 Yue Skills

#### A practical, external-facing skills collection: research · content · visuals · distribution

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-94-10B981?style=for-the-badge)](#-skill-categories)
[![Prompts](https://img.shields.io/badge/Prompts-1-F59E0B?style=for-the-badge)](#-prompts)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

</div>

Yue Skills focuses on a "real and actionable" AI production pipeline — from information input, content processing, and visual generation to multi-platform publishing.

---

## 📦 Install

In any agent that supports Skills, install a single directory directly:

```text
Install this skill: <your-repo-url>/tree/main/<skill-name>
```

e.g. `diagram-svg-generator`, `publish-wechat-official`, `image-generate-multiapi`, `workflow-neat-sync`.

---

## 🗂️ Skill Categories

### A. Research & Information Input

> Fetch, extract, translate, research — the starting point of the information chain.

| Skill | Purpose | Path |
|---|---|---|
| `news-aihot-daily` | AI hot-news daily digest & retrieval (aihot.virxact.com) | [`./news-aihot-daily`](./news-aihot-daily) |
| `web-markdown-extract` | Any webpage → Markdown | [`./web-markdown-extract`](./web-markdown-extract) |
| `danger-x-markdown-export` | X/Twitter content → Markdown archival | [`./danger-x-markdown-export`](./danger-x-markdown-export) |
| `youtube-transcript-extract` | YouTube subtitle & cover image extraction | [`./youtube-transcript-extract`](./youtube-transcript-extract) |
| `youtube-video-clipper` | YouTube smart clipping & bilingual subtitle burn-in | [`./youtube-video-clipper`](./youtube-video-clipper) |
| `wechat-group-summary` | WeChat group chat summary & persona profiling | [`./wechat-group-summary`](./wechat-group-summary) |
| `text-translate-workflow` | Multi-mode translation: fast / standard / refined | [`./text-translate-workflow`](./text-translate-workflow) |
| `research-hv-analysis` | Horizontal-Vertical analysis deep research report | [`./research-hv-analysis`](./research-hv-analysis) |

---

### B. Writing & Content Processing

> Structure, voice, and multi-platform copy — the core of content production.

| Skill | Purpose | Path |
|---|---|---|
| `markdown-format-polish` | Markdown structural clean-up & layout optimization | [`./markdown-format-polish`](./markdown-format-polish) |
| `markdown-html-wechat` | Markdown → WeChat Official Account compatible HTML | [`./markdown-html-wechat`](./markdown-html-wechat) |
| `text-check-skill` | Sensitive word scan & compliance check | [`./text-check-skill`](./text-check-skill) |
| `writing-khazix-style` | Khazix-style WeChat long-form article writing | [`./writing-khazix-style`](./writing-khazix-style) |
| `Viral_Writer_Skill` | Multi-platform viral copywriting (WeChat / Xiaohongshu / Douyin) | [`./Viral_Writer_Skill`](./Viral_Writer_Skill) |
| `social-account-doctor` | Social account benchmarking, deconstruction & imitation loop | [`./social-account-doctor`](./social-account-doctor) |

---

### C. Visual Creation

#### C1. Images & Illustration

> From article images to e-commerce product shots — full coverage of content image scenarios.

| Skill | Purpose | Path |
|---|---|---|
| `image-generate-multiapi` | Unified multi-model text-to-image (GPT-Image / Gemini / Azure) | [`./image-generate-multiapi`](./image-generate-multiapi) |
| `danger-gemini-webapi` | Gemini Web image & text capability integration (reverse) | [`./danger-gemini-webapi`](./danger-gemini-webapi) |
| `article-cover-generator` | Article cover image generation (5-dimension styles) | [`./article-cover-generator`](./article-cover-generator) |
| `article-image-illustrator` | Article auto-illustration (position detection + prompt generation) | [`./article-image-illustrator`](./article-image-illustrator) |
| `document-illustrator` | Document smart illustration (cover + body, style locking) | [`./document-illustrator`](./document-illustrator) |
| `ecom-product-image` | E-commerce full-scene image generation (hero/detail/banner, 25 templates) | [`./ecom-product-image`](./ecom-product-image) |
| `logo-svg-generator` | SVG logo & brand showcase generation (12 background styles) | [`./logo-svg-generator`](./logo-svg-generator) |
| `social-image-cards` | Social media graphic card series generation | [`./social-image-cards`](./social-image-cards) |
| `xhs-social-card` | Xiaohongshu image sets & WeChat cover pairs, Guizang style (Swiss / magazine) | [`./xhs-social-card`](./xhs-social-card) |
| `visual-infographic-generator` | Professional infographic generation (21 layouts) | [`./visual-infographic-generator`](./visual-infographic-generator) |
| `image-compress-optimizer` | Image compression optimization (WebP/PNG, auto quality reduction) | [`./image-compress-optimizer`](./image-compress-optimizer) |

#### C2. Diagrams & Data Visualization

> Code-level SVG diagrams and comic-style knowledge expression.

| Skill | Purpose | Path |
|---|---|---|
| `diagram-svg-generator` | SVG architecture / flowchart / sequence diagrams (dark theme) | [`./diagram-svg-generator`](./diagram-svg-generator) |
| `content-comic-generator` | Knowledge comic generation (multi-style) | [`./content-comic-generator`](./content-comic-generator) |

#### C3. Presentations & PPT

> From document to deck — web-based PPT to AI image PPT, fully covered.

| Skill | Purpose | Path |
|---|---|---|
| `slides-deck-generator` | Slide / presentation image generation workflow | [`./slides-deck-generator`](./slides-deck-generator) |
| `html-ppt-guizang` | Horizontal swipe HTML PPT (magazine / Swiss International style, single HTML) | [`./html-ppt-guizang`](./html-ppt-guizang) |
| `ppt-image-generator` | AI-generated PPT images + Kling AI transition videos (Nano Banana) | [`./ppt-image-generator`](./ppt-image-generator) |

#### C4. Video & Motion

> Clipping, effects wrapping, and product animation prompts.

| Skill | Purpose | Path |
|---|---|---|
| `youtube-video-clipper` | YouTube smart clipping + bilingual subtitle burn-in | [`./youtube-video-clipper`](./youtube-video-clipper) |
| `video-wrapper-effects` | Interview video variety-show effects (captions/cards/banners, 4 themes) | [`./video-wrapper-effects`](./video-wrapper-effects) |
| `seedance-video-prompt` | Seedance 2.0 product animation prompts (4 aesthetic styles) | [`./seedance-video-prompt`](./seedance-video-prompt) |

---

### D. Publishing & Distribution

> The last mile of content reach: one-click multi-platform publishing.

| Skill | Purpose | Path |
|---|---|---|
| `publish-wechat-official` | Publish to WeChat Official Account (API / draft box) | [`./publish-wechat-official`](./publish-wechat-official) |
| `publish-weibo-post` | Publish to Weibo (text / image+text / video) | [`./publish-weibo-post`](./publish-weibo-post) |
| `publish-x-post` | Publish to X / Twitter (post / long article) | [`./publish-x-post`](./publish-x-post) |

---

### E. Workflow Governance & Platform Capabilities

> Session governance, knowledge sync, and vertical-domain Agent capabilities.

| Skill | Purpose | Path |
|---|---|---|
| `workflow-neat-sync` | Session wrap-up: sync docs, CLAUDE.md & Agent memory | [`./workflow-neat-sync`](./workflow-neat-sync) |
| `openclaw-ecommerce-skill` | OpenClaw e-commerce assistant (product management / copywriting) | [`./openclaw-ecommerce-skill`](./openclaw-ecommerce-skill) |
| `openclaw-ecommerce-team` | OpenClaw e-commerce team collaboration workflow | [`./openclaw-ecommerce-team`](./openclaw-ecommerce-team) |
| `openclaw-one-person-company-skill` | OpenClaw solo founder full-cycle workflow | [`./openclaw-one-person-company-skill`](./openclaw-one-person-company-skill) |

---

### F. Deprecated

| Skill | Status | Replacement |
|---|---|---|
| `xhs-cards-legacy` | Deprecated | → `social-image-cards` |
| `image-generate-legacy` | Deprecated | → `image-generate-multiapi` |

---

### G. Extended Skill Packs (New Migration on 2026-05-30)

> First-round naming normalization is completed in this batch: `gr-*` is unified to `growth-*`, and selected abbreviated `wps-*` names are expanded into clearer 2-part/3-part names.

| Source | Count | Notes | Directory Index |
|---|---:|---|---|
| `archive/gingiris-skills/skills` | 12 | Growth / SEO / content distribution workflows | `growth-research`, `growth-aso-optimizer`, `growth-b2b-engine`, `growth-seo-backlinks`, `growth-blog-writer`, `growth-competitor-intel`, `growth-geo-citations`, `growth-oss-marketing`, `growth-producthunt-launch`, `growth-seo-monitor`, `growth-social-insights`, `growth-user-interview` |
| `archive/influencer-marketing-skill` | 1 | Influencer marketing specialized skill | `influencer-marketing-skill` |
| `archive/wps-skills/skills` | 42 | WPS office automation skill suite | All `wps-*` directories (e.g. `wps-ppt-generator`, `wps-data-clean`, `wps-proofread`, `wps-vlookup`) |
| `archive/text-check-skill` | 0 (already exists) | Same directory name already present; skipped to avoid overwrite | `text-check-skill` |
| `archive/awesome-amazon-ec-skills` | 0 | No `SKILL.md` directories detected | - |
| `archive/common-skills` | 0 | No `SKILL.md` directories detected | - |

---

#### G.1 Naming Normalization Map (Current Round)

| Old Name | New Name |
|---|---|
| `gr` | `growth-research` |
| `gr-aso` | `growth-aso-optimizer` |
| `gr-b2b-growth` | `growth-b2b-engine` |
| `gr-backlinks` | `growth-seo-backlinks` |
| `gr-blog-post` | `growth-blog-writer` |
| `gr-competitor` | `growth-competitor-intel` |
| `gr-geo-cite` | `growth-geo-citations` |
| `gr-oss-marketing` | `growth-oss-marketing` |
| `gr-ph-launch` | `growth-producthunt-launch` |
| `gr-seo-patrol` | `growth-seo-monitor` |
| `gr-social-distill` | `growth-social-insights` |
| `gr-user-interview` | `growth-user-interview` |
| `wps-cn-calendar` | `wps-chinese-calendar` |
| `wps-data-viz` | `wps-data-visualization` |
| `wps-gongwen` | `wps-official-doc` |
| `wps-i18n` | `wps-localization-i18n` |
| `wps-jsa-macro` | `wps-js-macro` |
| `wps-ppt-gen` | `wps-ppt-generator` |
| `wps-resume-cn` | `wps-resume-chinese` |

---

## 🔗 Recommended Workflows

| Scenario | Pipeline |
|---|---|
| **Deep research** | `web-markdown-extract` → `text-translate-workflow` → `research-hv-analysis` |
| **WeChat content production** | `writing-khazix-style` → `article-image-illustrator` / `document-illustrator` → `markdown-html-wechat` → `publish-wechat-official` |
| **Multi-platform distribution** | `Viral_Writer_Skill` → `social-image-cards` → `publish-x-post` + `publish-weibo-post` + `publish-wechat-official` |
| **Video content processing** | `youtube-transcript-extract` / `youtube-video-clipper` → `video-wrapper-effects` |
| **Visual asset generation** | `ecom-product-image` / `logo-svg-generator` / `document-illustrator` → `image-compress-optimizer` |
| **Presentation creation** | `research-hv-analysis` → `html-ppt-guizang` / `ppt-image-generator` |

---

## 📝 Prompts

| Name | Description | Path |
|---|---|---|
| `Horizontal-Vertical Analysis (Prompt edition)` | Lightweight research template — paste into any Deep Research model, no installation needed | [`./prompts/横纵分析法.md`](./prompts/横纵分析法.md) |

---

## ⚠️ Compliance Notes

`danger-*` skills involve browser automation or reverse-engineered interfaces. Use only within the bounds of the platform's ToS and applicable local laws.

---

<div align="center">

[MIT License](./LICENSE) · Free to use, modify, and redistribute

</div>
