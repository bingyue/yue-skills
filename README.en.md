<div align="center">

<img src="https://img.shields.io/badge/Yue%20Skills-AI%20Production%20Toolkit-10B981?style=for-the-badge&logo=anthropic&logoColor=white" alt="Yue Skills">

# Yue Skills

**A ready-to-install AI Agent skill library covering e-commerce, social media, video, growth, and office automation**

[中文](./README.md) · **English**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-96+-10B981?style=flat-square)](#-skill-categories)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-D97706?style=flat-square&logo=anthropic)](https://claude.ai/code)
[![Codex](https://img.shields.io/badge/Codex-Ready-10B981?style=flat-square&logo=openai)](https://openai.com/codex)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=flat-square)](https://agentskills.io)

</div>

---

## About Yue (越哥)

> Yue Skills is curated and maintained by **Yue (越哥)**, focused on "real and immediately usable" AI production workflows.

**Yue** is an AI content creator dedicated to turning cutting-edge AI tools into workflows **anyone can use directly** — from e-commerce AI product research and Xiaohongshu viral content to automated video editing and cross-border SEO growth. Every Skill in this library has been validated in real business scenarios before being open-sourced.

| Platform | Account | Description |
|---|---|---|
| WeChat Official Account | **越哥聊AI** | AI tool reviews, skill tutorials, workflow breakdowns |
| WeChat Group | **越哥AI智能体** | Scan QR to join — discuss AI Agent practice together |
| GitHub | [@bingyue](https://github.com/bingyue) | Open-source workflows and Skill repositories |

---

## What Is This

Yue Skills is an **installable AI Agent skill collection** following the [AgentSkills](https://agentskills.io) open standard.  
Each skill directory contains a `SKILL.md` file — load it into your Agent and it's ready to use, no further development needed.

- **96+ top-level installable Skills**: each root directory has a `SKILL.md` for standalone installation
- **20+ Bundles**: aggregated packs containing multiple sub-Skills, use as needed
- **10 scenario categories**: E-commerce · Social Media · Writing · Visual · Video · Data Analysis · Audio/Podcast · PPT · Research · Growth · Office
- **Community Recommendations**: each category includes curated high-star GitHub repos (installable directly)

---

## Quick Install

### Claude Code

```bash
# Tell the Agent to install directly (Agent will auto-clone)
Install this skill: https://github.com/bingyue/yue-skills/tree/main/<skill-name>
```

### Codex / OpenAI Agents

```bash
# One-line install in Codex
Install skill from GitHub: https://github.com/bingyue/yue-skills/tree/main/<skill-name>
```

### OpenClaw / OpenCode

```bash
# Install to local .claude/skills directory
git clone https://github.com/bingyue/yue-skills.git /tmp/yue-skills
cp -r /tmp/yue-skills/<skill-name> ~/.claude/skills/
```

### Manual Install (Universal)

```bash
git clone https://github.com/bingyue/yue-skills.git
# Copy the skill directory you need into your Agent's skills folder
cp -r yue-skills/<skill-name> ~/.claude/skills/<skill-name>
```

> **Counting convention**: `Skill` = a root directory with `SKILL.md` that can be installed standalone; `Bundle` = a root directory without `SKILL.md` but containing multiple sub-Skills.

---

## 🗂️ Skill Categories

### 🛒 E-Commerce & Product Research

> From product research and detail page design to image generation and copywriting — the full e-commerce chain.

| Skill | Description |
|---|---|
| [`ecom-pdp-one-click`](./ecom-pdp-one-click) | One-click high-converting PDP detail page + hero image for cross-border e-commerce |
| [`ecom-product-image`](./ecom-product-image) | E-commerce full-scene image generation (hero/detail/banner, 25 templates) |
| [`ecom-claw`](./ecom-claw) | E-commerce product scraping and data analysis |
| [`ecom-image-suite`](./ecom-image-suite) | Product image sets (hero/feature/lifestyle/model shots) |
| [`ecom-product-research`](./ecom-product-research) | Amazon refined product research report generation |
| [`ecom-visual-copy`](./ecom-visual-copy) | E-commerce hero image + detail page copywriting SOP |
| [`ecom-gpt-image2`](./ecom-gpt-image2) | GPT-Image-2 e-commerce product images (25 high-quality templates) |
| [`ecom-review-mind`](./ecom-review-mind) | 3-layer structured review analysis (ABSA / pain points / recommendation score) |
| [`ecom-review-monitor`](./ecom-review-monitor) | Review sentiment monitoring: negative alerts / competitor mining / sentiment analysis / weekly reports |
| [`ecom-amazon-visual`](./ecom-amazon-visual) | Amazon Listing visual architecture design |
| [`ecom-douyin-drama`](./ecom-douyin-drama) | Douyin drama-style sales script generation (cinematic aesthetics + conversion design) |
| [`ecom-ai-tryon`](./ecom-ai-tryon) | AI virtual try-on Agent (upload clothing + person for try-on preview) |
| [`influencer-marketing`](./influencer-marketing) | Overseas influencer marketing full flow (competitor analysis / brief / outreach / review) |
| [`influencer-outreach`](./influencer-outreach) | KOL campaign management workflow (topic → search → outreach) |
| [`influencer-pugongying`](./influencer-pugongying) | Pugongying KOL influencer filtering tool |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills) | Amazon seller suite: keyword research, competitor analysis, Listing audit, review analysis (MIT) |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/ecommerce-skills) | Multi-platform e-commerce: negative monitoring / competitor price tracking / brand protection (Amazon/eBay/Walmart/TikTok) |
| [noique/cross-border-ecommerce-skills](https://github.com/noique/cross-border-ecommerce-skills) | Cross-border e-commerce full chain (37 single-file skills): sourcing / market research / supplier evaluation / VOC analysis |
| [buluslan/ecommerce-competitor-analyzer](https://github.com/buluslan/ecommerce-competitor-analyzer) | Multi-platform competitor analysis (Amazon/Temu/Shopee), 4-dimension framework, outputs Google Sheets + Markdown |

---

### 📱 Social Media Operations & Distribution

> Xiaohongshu, Douyin, Weibo, WeChat Official Account, X — multi-platform operations and one-click publishing.

| Skill | Description |
|---|---|
| [`xhs-ops-workflow`](./xhs-ops-workflow) | Xiaohongshu full-chain operations (positioning / topics / production / publishing / review) |
| [`xhs-auto-creator`](./xhs-auto-creator) | Xiaohongshu note content auto-creation |
| [`xhs-publish-suite`](./xhs-publish-suite) | Xiaohongshu image+text / video auto-publish + search and engagement |
| [`xhs-social-card`](./xhs-social-card) | Guizang-style Xiaohongshu image cards + WeChat cover image pairs |
| [`social-account-doctor`](./social-account-doctor) | Social account benchmarking, deconstruction & imitation loop (XHS/Douyin/Kuaishou/Channels) |
| [`write-viral-creator`](./write-viral-creator) | Multi-platform viral copy (WeChat / Xiaohongshu / Douyin), with image guidance |
| [`video-douyin-transcribe`](./video-douyin-transcribe) | Douyin share link → video download → FunASR speech-to-text |
| [`image-social-card`](./image-social-card) | Social media graphic card series generation |
| [`publish-wechat-official`](./publish-wechat-official) | Publish to WeChat Official Account (API / draft box) |
| [`publish-weibo-post`](./publish-weibo-post) | Publish to Weibo (text / image+text / video) |
| [`publish-x-post`](./publish-x-post) | Publish to X/Twitter (post / long article) |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [autoclaw-cc/xiaohongshu-skills](https://github.com/autoclaw-cc/xiaohongshu-skills) | Full Xiaohongshu automation (auth/publish/discovery/engagement/ops), browser-based |
| [ibreez3/xiaohongshu-skill](https://github.com/ibreez3/xiaohongshu-skill) | Xiaohongshu MCP publish plugin (Claude Code/Cursor/Cline, image+video) |
| [jihe520/social-push](https://github.com/jihe520/social-push) | Multi-platform one-click publish (XHS image+text/long-form + X/Twitter), self-healing on UI changes |
| [solar-luna/fully-automatic-article-generation-skill](https://github.com/solar-luna/fully-automatic-article-generation-skill) | Article → XHS format auto-compress + publish (≤1000 chars, emoji style, MCP interface) |

---

### ✍️ Content Writing & Copywriting

> Markdown formatting, style writing, compliance checking — the core content production chain.

| Skill | Description |
|---|---|
| [`writing-khazix-style`](./writing-khazix-style) | Khazix-style WeChat long-form writing (fixed tone / forbidden patterns / 4-layer self-check) |
| [`write-viral-creator`](./write-viral-creator) | Multi-platform viral copy creation |
| [`write-md-polish`](./write-md-polish) | Markdown structural clean-up and layout optimization |
| [`write-md-wechat`](./write-md-wechat) | Markdown → WeChat Official Account compatible HTML |
| [`write-text-check`](./write-text-check) | Sensitive word scan and compliance check |
| [`write-translate`](./write-translate) | Multi-mode translation: fast / standard / refined |
| [`ecom-visual-copy`](./ecom-visual-copy) | E-commerce image+text copywriting SOP |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [avectats7/copy-that-sells](https://github.com/avectats7/copy-that-sells) | Ad copy writing (D&AD + Bly direct response framework): ads/landing pages/emails/manifesto, 122 award-winning references, strict anti-AI layer |
| [sociilabs/claude-content-writer](https://github.com/sociilabs/claude-content-writer) | Blog/LinkedIn/email professional writing, 5-stage GSD process, built-in SEO + 25-point anti-AI audit |
| [pedronauck/skills](https://github.com/pedronauck/skills) | 140 curated skills (75 original), including `content-research-writer` / `copywriting` / `humanizer` / `writing-clearly-and-concisely` |
| [kaisdavis/claude-skills](https://github.com/kaisdavis/claude-skills) | `docs-update` (auto-sync docs at session end), `open-source-skill` (internalize to publish), writing governance tools |

---

### 🎨 Visual Generation & Design

> Text-to-image, illustration, infographics, Logo, and brand visual asset generation.

| Skill | Description |
|---|---|
| [`image-generate-multiapi`](./image-generate-multiapi) | Unified multi-model text-to-image (GPT-Image / Gemini / Azure) |
| [`image-gemini-webapi`](./image-gemini-webapi) | Gemini Web image and text capability integration (reverse) |
| [`image-cover-gen`](./image-cover-gen) | Article cover image generation (5-dimension styles) |
| [`image-para-illustrator`](./image-para-illustrator) | Article auto-illustration (position detection + prompt generation) |
| [`image-doc-illustrator`](./image-doc-illustrator) | Document smart illustration (cover + body, style locking) |
| [`image-logo-svg`](./image-logo-svg) | SVG Logo and brand showcase generation (12 background styles) |
| [`image-infographic`](./image-infographic) | Professional infographic generation (21 layouts) |
| [`image-diagram-svg`](./image-diagram-svg) | SVG architecture / flowchart / sequence diagrams (dark theme) |
| [`image-comic-gen`](./image-comic-gen) | Knowledge comic generation (multi-style) |
| [`image-compress-optimizer`](./image-compress-optimizer) | Image compression optimization (WebP/PNG, auto quality reduction) |
| [`image-social-card`](./image-social-card) | Social media graphic card series generation |
| [`xhs-social-card`](./xhs-social-card) | Guizang-style Xiaohongshu image cards / WeChat cover generation |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [b1rdmania/claude-brand-skills](https://github.com/b1rdmania/claude-brand-skills) | Full brand development (8 stages): narrative → visual direction → Logo → wordmark → design system → deliverables |
| [op7418/logo-generator-skill](https://github.com/op7418/logo-generator-skill) | SVG Logo generator: 6+ variants + 12 professional showcase backgrounds (void/frosted/spotlight/iridescent), Nano Banana rendering |
| [dancolta/gen-images-skill](https://github.com/dancolta/gen-images-skill) | Brand-aware image generation: scans Tailwind/CSS to extract visual identity, generates brand-consistent images for missing slots |
| [EmmaStoneX/claude-design-skill](https://github.com/EmmaStoneX/claude-design-skill) | HTML visual design expert (landing pages/decks/prototypes/animations/posters), adapted from Claude.ai internal Design system prompts |

---

### 🎬 Video & Multimedia Production

> From script to final cut — clipping, effects wrapping, storyboard, subtitle processing full workflow.

| Skill | Description |
|---|---|
| [`video-youtube-clip`](./video-youtube-clip) | YouTube smart clipping + bilingual subtitle burn-in |
| [`video-youtube-subtitle`](./video-youtube-subtitle) | YouTube subtitle and cover image extraction |
| [`video-bilibili-subtitle`](./video-bilibili-subtitle) | Bilibili video subtitle download + LLM high-quality summary |
| [`video-wrapper-effects`](./video-wrapper-effects) | Interview video variety-show effects (captions/cards/banners, 4 themes) |
| [`video-seedance-prompt`](./video-seedance-prompt) | Seedance 2.0 product animation prompts (4 aesthetic styles) |
| [`video-dialogue`](./video-dialogue) | Dialogue video generation and processing |
| [`video-jianying`](./video-jianying) | Jianying AI automated editing (subtitles/assets/effects/export) |
| [`video-script-to-film`](./video-script-to-film) | Article/script → OmiVoice TTS voiceover → complete video |
| [`video-storyboard`](./video-storyboard) | Video storyboard script generation (narrative structure + shot descriptions) |
| [`video-promo-creator`](./video-promo-creator) | Product promo video controller (60-90s, from website/screenshots to final cut) |
| [`ppt-html-animation`](./ppt-html-animation) | Science content → PPT-style animated HTML web page |
| [`video-douyin-transcribe`](./video-douyin-transcribe) | Douyin video → speech-to-text |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [AgriciDaniel/claude-video](https://github.com/AgriciDaniel/claude-video) | Full AI video production suite: editing/transcoding/denoising/Whisper subtitles/Veo generation/vertical crop/social adapt (15 sub-skills) |
| [MadAppGang/claude-code video-editing](https://github.com/MadAppGang/claude-code/tree/main/plugins/video-editing) | Professional video editing plugin: FFmpeg operations + Whisper transcription + Final Cut Pro FCPXML generation |

---

### 📊 Data Analysis & Visualization

> CSV/Excel data to insight reports, sales funnels, e-commerce dashboards, business metric tracking.

| Skill | Description |
|---|---|
| [`sales-funnel-analyzer`](./sales-funnel-analyzer) | Sales funnel conversion analysis: per-stage rates / drop-off identification / industry benchmarks / optimization suggestions |
| [`ecom-data-dashboard`](./ecom-data-dashboard) | E-commerce operations dashboard: GMV / conversion rate / AOV / retention / ROI, outputs HTML dashboard or Markdown report |
| [`csv-report-generator`](./csv-report-generator) | Universal CSV smart report: auto-detects data type, generates statistical summary + insights + chart suggestions |

*Community hot recommendations (installable directly):*

| Repo | Description |
|---|---|
| [dongzhang84/data-analysis-skill](https://github.com/dongzhang84/data-analysis-skill) | Drop in CSV/Excel and get: multi-expert parallel analysis → interactive HTML report + PowerPoint export (KPI/charts/risk cards) |
| [nimrodfisher/data-analytics-skills](https://github.com/nimrodfisher/data-analytics-skills) | 31 data analysis skills: cohort / funnel / time-series / A/B test / root cause / metric calculation, full chain coverage |
| [adityawrk/analytics-with-claude-code](https://github.com/adityawrk/analytics-with-claude-code) | Production analytics config: `/eda` / `/sql-optimizer` / `/data-quality` / `/ab-test` / `/weekly-report` and 10 slash commands |
| [coffeefuelbump/csv-data-summarizer](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) | Upload CSV for auto-analysis: stats + charts + insights (e-commerce/finance/ops/research multi-industry adaptive) |
| [anthropics/skills xlsx](https://github.com/anthropics/skills/tree/main/document-skills) | Anthropic official xlsx skill: work with Excel files, formulas, tables, charts |

---

### 🎙️ Audio & Podcast

> Meeting recordings to structured notes, podcasts to articles — audio content processing full chain.

| Skill | Description |
|---|---|
| [`meeting-transcript-notes`](./meeting-transcript-notes) | Meeting recording / subtitle / transcript → structured notes (decisions / action items / open issues, with owner and deadline) |
| [`audio-to-article`](./audio-to-article) | Podcast / subtitle / speech recording → readable article, removes filler words, adds structure, fits WeChat/blog/LinkedIn |

*Community hot recommendations (installable directly):*

| Repo | Description |
|---|---|
| [zarazhangrui/personalized-podcast](https://github.com/zarazhangrui/personalized-podcast) | NotebookLM-style experience: any content → dual-host AI podcast MP3, subscribable to Apple Podcasts/Spotify/Overcast |
| [soanseng/podcast-use](https://github.com/soanseng/podcast-use) | Podcast editing workflow: Groq Whisper transcription → AI edit → SRT subtitles → YouTube video → vertical Reels + cover |
| [terminator1333/claude-listen](https://github.com/terminator1333/claude-listen) | Local meeting transcription (faster-whisper + pyannote speaker diarization), project-context-aware meeting notes, fully offline |
| [sgasser/claude-skill-podcast](https://github.com/sgasser/claude-skill-podcast) | Zero-cost podcast: browser Web Speech API, no API key needed, multi-language, includes interactive player |

---

### 🎪 PPT & Presentations

> From documents to decks — HTML PPT to AI image PPT, fully covered.

| Skill | Description |
|---|---|
| [`ppt-slides-gen`](./ppt-slides-gen) | Presentation / slide image generation workflow |
| [`ppt-html-guizang`](./ppt-html-guizang) | Horizontal-swipe HTML PPT (magazine / Swiss International style, single HTML file) |
| [`ppt-image-generator`](./ppt-image-generator) | AI-generated PPT images + Kling AI transition videos (Nano Banana) |
| [`ppt-image2-gen`](./ppt-image2-gen) | GPT-Image-2 visually stunning PPT slides |
| [`ppt-visual-style`](./ppt-visual-style) | Style-driven slide image generation (Image 2) |

**High-value GitHub Skills (installable directly):**

| Repo | Stars | Description |
|---|---:|---|
| [Akxan/ppt-agent-skill](https://github.com/akxan/ppt-agent-skill) | ⭐ 57 | Premium PPT output: 26 styles + 18 data visualizations (Sankey/heatmap/Gantt), HTML + editable vector PPTX |
| [mrigankad/SlideArchitect](https://github.com/mrigankad/SlideArchitect) | — | Presentation strategist: 20+ layout templates for investor decks/sales/tech architecture/training |
| [daymade/claude-code-skills ppt-creator](https://github.com/daymade/claude-code-skills) | — | Auto-scored presentation generation (<75 = auto 2 iterations), Marp + PPTX dual output |
| [Gabberflast/academic-pptx-skill](https://github.com/Gabberflast/academic-pptx-skill) | — | Academic conference / thesis defense PPT standards (action titles / structured argument / citations / figure captions) |

---

### 🔍 Research & Information Gathering

> Web scraping, subtitle extraction, platform monitoring — the information chain entry point.

| Skill | Description |
|---|---|
| [`research-ai-news`](./research-ai-news) | AI hot-news daily digest and retrieval (aihot.virxact.com) |
| [`research-web-extract`](./research-web-extract) | Any webpage → Markdown |
| [`research-x-export`](./research-x-export) | X/Twitter content → Markdown archive |
| [`research-wechat-summary`](./research-wechat-summary) | WeChat group chat summary and persona profiling |
| [`research-hv-analysis`](./research-hv-analysis) | Horizontal-Vertical analysis deep research report |
| [`research-last30days`](./research-last30days) | China's 8 major platforms last-30-day deep research (Weibo/XHS/Bilibili/Zhihu/Douyin…) |
| [`research-content-collect`](./research-content-collect) | Multi-platform content collection (X / WeChat / Jike / Reddit) |
| [`job-boss-brief`](./job-boss-brief) | Boss Zhipin daily recruitment screening brief |
| [`write-translate`](./write-translate) | Multi-mode translation (fast / standard / refined) |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [BexTuychiev/firecrawl-claude-code-skill](https://github.com/BexTuychiev/firecrawl-claude-code-skill) | Firecrawl web scraping: Markdown extraction / screenshots / structured data / search / full-site crawl (500+ free credits) |
| [Cedriccmh/claude-code-skill-scrapling](https://github.com/Cedriccmh/claude-code-skill-scrapling) | Smart scraper (auto-selects Fetcher): Cloudflare/WAF bypass, logged-in sessions, site pattern library |
| [webcpu/deep-research-skill](https://github.com/webcpu/deep-research-skill) | Parallel multi-Agent deep research: 3-5 Opus Agents search in parallel → synthesize → cited Markdown report |
| [pete-builds/claude-research-agent](https://github.com/pete-builds/claude-research-agent) | Anti-hallucination citation research: strict citation discipline + confidence assessment, outputs Markdown + shareable HTML |

---

### 📈 Growth Strategy & SEO

> Product Hunt launch, SEO backlinks, B2B growth, GEO citation tracking.

| Skill | Description |
|---|---|
| [`growth-research`](./growth-research) | Gingiris growth toolkit main entry |
| [`growth-aso-optimizer`](./growth-aso-optimizer) | ASO + App cold start (keywords / metadata / UGC) |
| [`growth-b2b-engine`](./growth-b2b-engine) | B2B SaaS full lifecycle growth (PLG/SLG, to $10M ARR) |
| [`growth-seo-backlinks`](./growth-seo-backlinks) | Systematic backlink building (5 channel strategies) |
| [`growth-blog-writer`](./growth-blog-writer) | Jekyll blog SEO writing and publishing pipeline |
| [`growth-competitor-intel`](./growth-competitor-intel) | Competitor deep scan (landing pages / pricing / blog / SEO) |
| [`growth-geo-citations`](./growth-geo-citations) | GEO citation tracking + AI search visibility optimization |
| [`growth-oss-marketing`](./growth-oss-marketing) | Open-source project launch integrated marketing (GitHub stars / KOL / Reddit / HN) |
| [`growth-producthunt-launch`](./growth-producthunt-launch) | Product Hunt launch playbook (T-14 warm-up to T+7 review) |
| [`growth-seo-monitor`](./growth-seo-monitor) | Daily SEO/GEO patrol (SERP rankings / Google index / llms.txt) |
| [`growth-social-insights`](./growth-social-insights) | Blog → multi-platform social variants (X / Xiaohongshu / LinkedIn) |
| [`growth-user-interview`](./growth-user-interview) | User interview framework (HeyGen 937-interview PMF methodology) |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [openai/skills](https://github.com/openai/skills) | OpenAI official skill library, includes `gh-address-comments`, `create-plan`, combinable with growth/SEO workflows |
| [AlirezaRezvani/claude-skills](https://github.com/AlirezaRezvani/claude-skills) | SEO / marketing / content distribution workflows, 533 stdlib-only Python tools, supports 13 platforms |
| [noique/cross-border-ecommerce-skills](https://github.com/noique/cross-border-ecommerce-skills) `outbound-prospecting` | Overseas customer prospecting (complete outreach skill with Python scripts + CSV tracker) |

---

### 💼 Workplace, Office & Engineering Governance

> WPS office automation, Feishu collaboration, job hunting, compliance, private domain, B2B content.

| Skill | Description |
|---|---|
| [`lark-bitable`](./lark-bitable) | Feishu Bitable full lifecycle management (create / CRUD / views) |
| [`lark-todo`](./lark-todo) | Feishu all-platform todo scan (8 source parallel collection, priority-sorted) |
| [`lark-fashion-cockpit`](./lark-fashion-cockpit) | Women's fashion e-commerce cockpit (38 capabilities, Feishu CLI digital solution) |
| [`workflow-neat-sync`](./workflow-neat-sync) | Session wrap-up knowledge sync (docs / CLAUDE.md / Agent memory 3-layer alignment) |
| [`job-boss-auto`](./job-boss-auto) | Boss Zhipin auto job hunting (stealth search → multi-Agent matching → apply) |
| [`job-hunter`](./job-hunter) | Scheduled job hunting assistant (auto-discover / filter / record matching positions) |
| [`job-boss-brief`](./job-boss-brief) | Boss Zhipin daily recruitment screening brief |
| [`cn-compliance-check`](./cn-compliance-check) | China compliance all-in-one: Advertising Law extreme words / sensitive words / medical forbidden terms, risk-graded report |
| [`wecom-private-domain`](./wecom-private-domain) | WeCom private domain ops: group SOP / Moments planning / user segmentation / keyword replies / SCRM strategy |
| [`b2b-content-suite`](./b2b-content-suite) | B2B content marketing suite: LinkedIn articles / white papers / case studies / industry report summaries |
| [`video-comment-ops`](./video-comment-ops) | Video comment section ops: classification / negative review handling / reply templates / reputation management SOP |
| [`brand-visual-ai`](./brand-visual-ai) | Brand visual AI full flow: narrative → Logo → design system → deliverables (8 stages) |

**WPS Office Automation (42 skills, use by scenario):**

| Scenario | Representative Skills |
|---|---|
| Document Writing | `wps-docx-writer`, `wps-report-writer`, `wps-contract`, `wps-official-doc` |
| PPT Creation | `wps-ppt-generator`, `wps-ppt-outline`, `wps-ppt-polish`, `wps-ppt-speaker-notes` |
| Data Processing | `wps-data-clean`, `wps-data-visualization`, `wps-formula`, `wps-vlookup`, `wps-pivot` |
| Financial Reports | `wps-financial-report`, `wps-salary`, `wps-budget` |
| HR Scenarios | `wps-resume-chinese`, `wps-exam-paper`, `wps-certificate`, `wps-attendance` |
| Scheduling | `wps-gantt`, `wps-schedule`, `wps-chinese-calendar` |
| Format & Convert | `wps-format-fix`, `wps-batch-convert`, `wps-pdf-extract`, `wps-pdf-merge-split` |
| Macros & Automation | `wps-js-macro`, `wps-template-engine`, `wps-mail-merge` |

**High-value GitHub Skills (installable directly):**

| Repo | Description |
|---|---|
| [thoniorf/pm-claude-skills](https://github.com/thoniorf/pm-claude-skills) | Multi-function professional skill library: PM / engineering / customer success / marketing / design / legal / finance / HR / sales, with Linear/Jira/Slack/Notion templates |
| [dongzhang84/data-analysis-skill](https://github.com/dongzhang84/data-analysis-skill) | End-to-end data analysis: multi-expert parallel reasoning → interactive HTML report (charts/insights/risk cards) + one-click PPTX export |
| [nimrodfisher/data-analytics-skills](https://github.com/nimrodfisher/data-analytics-skills) | 31 data analysis skill pack: cohort / funnel / time-series / A/B test / root cause / business metric calculation |
| [adityawrk/analytics-with-claude-code](https://github.com/adityawrk/analytics-with-claude-code) | Production analytics config: `/eda` / `/sql-optimizer` / `/ab-test` / `/weekly-report` and 10 slash commands |

---

## 📚 Bundle Index

> Bundles contain multiple sub-Skills. Install via the bundle's README or sub-directory paths.

| Directory | Sub-Skills | Description |
|---|---:|---|
| [`ecomm-ai-skills-hub`](./ecomm-ai-skills-hub) | 180+ | E-commerce AI skill mega-collection (tile.json system) |
| [`xiaohongshu-skills`](./xiaohongshu-skills) | 139 | Xiaohongshu full-scenario skill pack |
| [`ecom-detail-page`](./ecom-detail-page) | 11 | E-commerce detail page copy (mother & baby / beauty / food / 3C by category) |
| [`system-prompt-skills`](./system-prompt-skills) | 15 | System prompt design skill set (memory / personality / safety / output format) |
| [`video-clip-ai`](./video-clip-ai) | 6 | AI video editing skill pack (subtitles / talking head clipping / highlights) |
| [`video-ai-pack`](./video-ai-pack) | 5 | AI video creation skill pack (product intro / animation / effects) |
| [`video-lanshu-kit`](./video-lanshu-kit) | 7 | Lanshu AI video toolkit (Seedance / Kling series) |
| [`xhs-claude-skills`](./xhs-claude-skills) | 4 | Xiaohongshu Claude skill pack (publish / cover / batch / analysis) |
| [`obsidian-skills`](./obsidian-skills) | 5 | Obsidian knowledge base management skill pack |
| [`axton-obsidian-visual-skills`](./axton-obsidian-visual-skills) | 3 | Obsidian visualization (Canvas / Mermaid / Excalidraw) |
| [`ecom-agent-pack`](./ecom-agent-pack) | 10 | E-commerce AI Agent skill pack |
| [`workflow-skill`](./workflow-skill) | 3 | Workflow platform skill pack (Dify / Coze / ComfyUI) |
| [`agent-skills`](./agent-skills) | 3 | China compliance check skills (advertising / business / e-commerce) |
| [`research-brightdata`](./research-brightdata) | 2 | Bright Data MCP deep research skills |
| [`ecom-crossborder-image`](./ecom-crossborder-image) | 2 | Amazon / Alibaba cross-border image generators |
| [`sales-daily-brief`](./sales-daily-brief) | 1 | Daily sales summary |
| [`codex-ppt-skill`](./codex-ppt-skill) | 1 | Codex PPT generation skill |
| [`video-recap`](./video-recap) | 1 | Video content recap skill |
| [`seedance-prompt-skill`](./seedance-prompt-skill) | 1 | Seedance prompt specialist skill |
| [`lark-fashion-cockpit`](./lark-fashion-cockpit) | multi | Feishu women's fashion e-commerce operations sub-skill set |

---

## 🔗 Recommended Workflows

```
Research        research-last30days / research-ai-news / research-hv-analysis
      ↓
Create          writing-khazix-style / write-viral-creator / social-account-doctor
      ↓
Visualize       image-para-illustrator / ecom-product-image / image-logo-svg
      ↓
Format          write-md-wechat / xhs-social-card / image-social-card
      ↓
Publish         publish-wechat-official / publish-weibo-post / publish-x-post / xhs-publish-suite
      ↓
Review          ecom-review-mind / growth-seo-monitor / growth-social-insights
```

| Scenario | Recommended Chain |
|---|---|
| WeChat article production | `research-hv-analysis` → `writing-khazix-style` → `image-doc-illustrator` → `write-md-wechat` → `publish-wechat-official` |
| Xiaohongshu viral content | `research-last30days` → `social-account-doctor` → `write-viral-creator` → `xhs-social-card` → `xhs-publish-suite` |
| E-commerce visual chain | `ecom-product-research` → `ecom-product-image` → `ecom-visual-copy` → `ecom-pdp-one-click` |
| Video content processing | `video-youtube-subtitle` → `video-youtube-clip` → `video-wrapper-effects` → `video-douyin-transcribe` |
| Growth SEO | `growth-competitor-intel` → `growth-seo-backlinks` → `growth-blog-writer` → `growth-seo-monitor` |
| Office automation | `wps-data-clean` → `wps-data-visualization` → `wps-report-writer` → `lark-todo` |

---

## 🗺️ ROADMAP

### ✅ v1.0 (Completed May 2026)

**Core Library**
- [x] 96 Skills covering 8 major scenarios: e-commerce / social / video / writing / research / data / compliance / office
- [x] Full naming standardization (2/3-segment kebab-case, 65 renames)
- [x] Single root `.gitignore` (consolidated from 51 nested files)
- [x] Complete bilingual README with install guide / category index / acknowledgements

**New Skills Added in v1.0**
- [x] `ecom-review-monitor` — E-commerce review sentiment monitoring and competitor negative mining
- [x] `sales-funnel-analyzer` — Sales funnel conversion rate analysis
- [x] `ecom-data-dashboard` — E-commerce data dashboard (GMV / conversion / retention)
- [x] `csv-report-generator` — Universal CSV smart report generation
- [x] `meeting-transcript-notes` — Meeting recordings / subtitles → structured notes
- [x] `audio-to-article` — Podcast / audio subtitles → readable articles
- [x] `cn-compliance-check` — China Advertising Law / sensitive words / medical compliance all-in-one
- [x] `wecom-private-domain` — WeCom private domain operations full-flow suite
- [x] `b2b-content-suite` — B2B content marketing (LinkedIn / white papers / case studies)
- [x] `video-comment-ops` — Video comment section operations and negative review handling
- [x] `brand-visual-ai` — Brand visual AI suite (based on b1rdmania/claude-brand-skills, 8 stages)

---

### v1.1 (Planned)

- [ ] Standardize core Skills' `SKILL.md` format (complete trigger words and examples for key categories)
- [ ] Build "Skill combination templates" (one-click install bundles by business scenario)
- [ ] Add real-world CSV examples for data analysis Skills
- [ ] Localization: translate ecom-* core Skill prompts to English

### v2.0 (Long-term Goals)

- [ ] Skill automated testing framework (verify SKILL.md description matches actual behavior)
- [ ] Open Skill submission mechanism with quality review SOP
- [ ] Integration with major Agent platforms (Coze / Dify / FastGPT)
- [ ] **Ecosystem**: list on [claudskills.com](https://claudskills.com) public directory (69K+ Skills index)

---

## 🙏 Acknowledgements

This repository incorporates and references work from the following open-source communities and creators:

| Repo / Author | Contribution |
|---|---|
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | Early Skill structure standards and toolset (research-web-extract, video-youtube-subtitle, and other core tools) |
| [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | Inspiration for writing-khazix-style, research-hv-analysis, and other writing/research Skills |
| [gingiris/gingiris-skills](https://github.com) | growth-* series of 12 growth strategy Skills (ASO/B2B/SEO/PH launch, etc.) |
| [guizang PPT series](https://github.com) | ppt-html-guizang, xhs-social-card, and other visual style Skills |
| [NanoBanana/PPT-Generator-Pro](https://github.com) | ppt-image-generator (AI image PPT + Kling AI transition video solution) |
| [lanshu-awesome-ai-video-kit](https://github.com) | Seedance/Kling video prompt skill pack |
| [ecommerce-detail-page-skills](https://github.com) | E-commerce detail page copy skills by product category |
| [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) | GPT-Image-2 e-commerce image 25 high-quality templates |
| [coolqoo/ecom-pdp-one-click](https://github.com/coolqoo/ecom-pdp-one-click) | Cross-border e-commerce one-click detail page inspiration |
| [b1rdmania/claude-brand-skills](https://github.com/b1rdmania/claude-brand-skills) | Brand visual AI 8-stage workflow (brand-visual-ai base) |
| [AgentSkills](https://agentskills.io) | Skill standard specification and SKILL.md format definition |

> If your work is included but not properly credited, please open an Issue and I'll add it right away.

---

## Contributing

Contributions of new Skills or improvements to existing ones are welcome!

```bash
# 1. Fork this repository
# 2. Create your skill directory in the root
mkdir my-skill && cd my-skill

# 3. Create SKILL.md (refer to existing skill format)
# Must include: name, description, trigger conditions, usage examples

# 4. (Optional) Add README.md, examples/, and references/

# 5. Submit a PR describing the skill's use case and real-world test results
```

**Skill quality standards:**
- `SKILL.md` exists in root directory, contains `name` (matching directory name) and `description` fields
- `description` clearly explains: what it is, when to use it, trigger keywords
- Use `kebab-case` naming, 2 or 3 segments, self-explanatory

---

## License

This repository is open-sourced under the [MIT License](./LICENSE) — free to use, modify, and redistribute.  
Some `danger-*` skills involve browser automation or reverse-engineered interfaces. Use only within the platform's ToS and applicable local laws.

---

<div align="center">

Made with ❤️ by **越哥 (Yue)**

WeChat Official Account: **越哥聊AI** · WeChat Group: **越哥AI智能体**

[GitHub](https://github.com/bingyue) · [MIT License](./LICENSE)

</div>
