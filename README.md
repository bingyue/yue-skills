<div align="center">

<img src="https://img.shields.io/badge/Yue%20Skills-AI%20Production%20Toolkit-10B981?style=for-the-badge&logo=anthropic&logoColor=white" alt="Yue Skills">

# Yue Skills

**可直接安装的 AI Agent 技能库，覆盖电商、社媒、视频、增长、办公全场景**

[English](./README.en.md) · 中文

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-84+-10B981?style=flat-square)](#-技能分类)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-D97706?style=flat-square&logo=anthropic)](https://claude.ai/code)
[![Codex](https://img.shields.io/badge/Codex-Ready-10B981?style=flat-square&logo=openai)](https://openai.com/codex)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=flat-square)](https://agentskills.io)

</div>

---

## 关于越哥

> Yue Skills 由越哥整理维护，聚焦"真实可落地"的 AI 生产链路。

**越哥**（Yue），AI 内容创作者，专注于把前沿 AI 工具转化成**普通人能直接用**的工作流。  
从电商 AI 选品到小红书爆款写作，从视频剪辑自动化到跨境增长 SEO，这里收录的每一个 Skill 都是经过真实业务场景验证后才开源的。

| 平台 | 账号 | 说明 |
|---|---|---|
| 微信公众号 | **越哥聊AI** | AI 工具评测、技能实战教程、工作流拆解 |
| 微信交流群 | **越哥AI智能体** | 扫码进群，一起探讨 AI Agent 实战 |
| GitHub | [@bingyue](https://github.com/bingyue) | 开源工作流与 Skill 仓库 |

---

## 这是什么

Yue Skills 是一个**可安装式 AI Agent 技能集合**，遵循 [AgentSkills](https://agentskills.io) 开放标准。  
每个技能目录包含 `SKILL.md`，Agent 加载后即可直接调用，无需二次开发。

- **84+ 顶层可安装 Skill**：每个目录根下均有 `SKILL.md`，可独立安装
- **20+ 技能包（Bundle）**：包含多个子 Skill 的聚合包，按需取用
- **10 大场景分类**：电商 · 社媒 · 写作 · 视觉 · 视频 · 数据分析 · 音频播客 · PPT · 研究 · 增长 · 办公
- **社区推荐**：每个分类附来自 GitHub 的高星真实仓库推荐（可直接安装）

---

## 快速安装

### Claude Code

```bash
# 告诉 Agent 直接安装（Agent 会自动 clone）
Install this skill: https://github.com/bingyue/yue-skills/tree/main/<skill-name>
```

### Codex / OpenAI Agents

```bash
# 在 Codex 中一句话安装
Install skill from GitHub: https://github.com/bingyue/yue-skills/tree/main/<skill-name>
```

### OpenClaw / OpenCode

```bash
# 安装到本地 .claude/skills 目录
git clone https://github.com/bingyue/yue-skills.git /tmp/yue-skills
cp -r /tmp/yue-skills/<skill-name> ~/.claude/skills/
```

### 手动安装（通用）

```bash
git clone https://github.com/bingyue/yue-skills.git
# 复制需要的 skill 目录到你的 Agent 的 skills 文件夹
cp -r yue-skills/<skill-name> ~/.claude/skills/<skill-name>
```

> **统计口径**：`Skill` 指根目录含 `SKILL.md` 的可直接安装目录；`Bundle` 指根目录无 `SKILL.md` 但内含多个子 Skill 的聚合包目录。

---

## 🗂️ 技能分类

### 🛒 电商与选品

> 从商品研究、详情页设计、图片生成到电商文案，覆盖电商全链路。

| Skill | 说明 |
|---|---|
| [`1click-ecom-detailpage`](./1click-ecom-detailpage) | 一键生成跨境电商高转化 PDP 详情页与主图 |
| [`ecom-product-image`](./ecom-product-image) | 电商全场景图片生成（主图/详情页/Banner，25 种模板） |
| [`ecom-claw`](./ecom-claw) | 电商选品抓取与数据分析 |
| [`ecommerce-image-suite`](./ecommerce-image-suite) | 电商套图生成（主图/卖点图/场景图/模特图） |
| [`ecommerce-product-research-skills`](./ecommerce-product-research-skills) | 亚马逊精细化选品调研报告生成 |
| [`ecommerce-visual-copywriting-skill`](./ecommerce-visual-copywriting-skill) | 电商主图+详情页文案设计 SOP |
| [`gpt-image2-ecommerce`](./gpt-image2-ecommerce) | GPT-Image-2 电商产品图生成（25 个高质量模板） |
| [`ReviewMind-Skills`](./ReviewMind-Skills) | 电商/消费品用户评论三层结构化分析（ABSA/痛点/推荐指数） |
| [`amazon-visual-architect-skill`](./amazon-visual-architect-skill) | 亚马逊 Listing 视觉架构设计 |
| [`douyin-drama-commerce-skill`](./douyin-drama-commerce-skill) | 抖音剧情带货脚本生成（融合影视美术与转化设计） |
| [`shop-tryon-skill`](./shop-tryon-skill) | AI 虚拟试穿 Agent（上传服装+人物即可试穿预览） |
| [`influencer-marketing-skill`](./influencer-marketing-skill) | 海外红人营销全流程（竞品分析/Brief撰写/红人建联/数据复盘） |
| [`influencer-outreach-skill`](./influencer-outreach-skill) | KOL 达人投放管理工作流（话题生成→达人搜索→建联发送） |
| [`pugongying-skill`](./pugongying-skill) | 蒲公英 KOL 达人筛选工具 |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills) | 亚马逊卖家专项：关键词研究、竞品分析、Listing 审计、评论分析（MIT） |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/ecommerce-skills) | 多平台电商：差评监控/竞品价格追踪/品牌保护（Amazon/eBay/Walmart/TikTok） |
| [noique/cross-border-ecommerce-skills](https://github.com/noique/cross-border-ecommerce-skills) | 跨境电商全链路（37 个单文件技能）：选品/市场研究/供应商评估/Trustpilot VOC 分析 |
| [buluslan/ecommerce-competitor-analyzer](https://github.com/buluslan/ecommerce-competitor-analyzer) | 多平台竞品分析（Amazon/Temu/Shopee），四维框架，输出 Google Sheets + Markdown |

---

### 📱 社媒运营与内容分发

> 小红书、抖音、微博、公众号、X 多平台运营与一键分发。

| Skill | 说明 |
|---|---|
| [`xiaohongshu-ops-skill`](./xiaohongshu-ops-skill) | 小红书全链路运营（账号定位/选题/内容生产/发布/复盘） |
| [`Auto-Redbook-Skills`](./Auto-Redbook-Skills) | 小红书笔记素材自动创作 |
| [`XiaohongshuSkills`](./XiaohongshuSkills) | 小红书图文/视频自动发布 + 内容检索与互动 |
| [`xhs-social-card`](./xhs-social-card) | 归藏风格小红书图文卡片 + 公众号封面图对生成 |
| [`social-account-doctor`](./social-account-doctor) | 自媒体账号对标拆解与仿写闭环（小红书/抖音/快手/视频号） |
| [`Viral_Writer_Skill`](./Viral_Writer_Skill) | 多平台爆款文案创作（公众号/小红书/抖音），含配图指导 |
| [`skills-douyin-text-to-text`](./skills-douyin-text-to-text) | 抖音分享链接解析 → 视频下载 → FunASR 语音转文字 |
| [`social-image-cards`](./social-image-cards) | 社媒图文卡片系列生成 |
| [`publish-wechat-official`](./publish-wechat-official) | 发布到微信公众号（API/草稿箱） |
| [`publish-weibo-post`](./publish-weibo-post) | 发布到微博（文字/图文/视频） |
| [`publish-x-post`](./publish-x-post) | 发布到 X/Twitter（正文/长文章） |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [autoclaw-cc/xiaohongshu-skills](https://github.com/autoclaw-cc/xiaohongshu-skills) | 小红书完整自动化（认证/发布/内容发现/互动/复合运营），基于真实浏览器 |
| [ibreez3/xiaohongshu-skill](https://github.com/ibreez3/xiaohongshu-skill) | 小红书 MCP 发布插件（Claude Code/Cursor/Cline，支持图文+视频） |
| [jihe520/social-push](https://github.com/jihe520/social-push) | 多平台一键发布（小红书图文/长文 + X/Twitter），自演进——页面改版自动修复 |
| [solar-luna/fully-automatic-article-generation-skill](https://github.com/solar-luna/fully-automatic-article-generation-skill) | 文章→小红书格式自动压缩+发布（≤1000字，emoji风格，MCP接口） |

---

### ✍️ 内容写作与文案加工

> 从 Markdown 排版、风格写作到合规检查，内容生产核心链路。

| Skill | 说明 |
|---|---|
| [`writing-khazix-style`](./writing-khazix-style) | 卡兹克风格公众号长文写作（固定语气/禁忌/四层自查） |
| [`Viral_Writer_Skill`](./Viral_Writer_Skill) | 多平台爆款文案创作 |
| [`markdown-format-polish`](./markdown-format-polish) | Markdown 结构化整理与排版优化 |
| [`markdown-html-wechat`](./markdown-html-wechat) | Markdown 转微信公众号兼容 HTML |
| [`text-check-skill`](./text-check-skill) | 敏感词扫描与合规检查 |
| [`text-translate-workflow`](./text-translate-workflow) | 多模式翻译：快翻/常规/精修三档 |
| [`ecommerce-visual-copywriting-skill`](./ecommerce-visual-copywriting-skill) | 电商图文文案 SOP |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [avectats7/copy-that-sells](https://github.com/avectats7/copy-that-sells) | 广告文案写作（D&AD+Bly直效框架）：广告/落地页/邮件/宣言，含122个获奖案例参考，严格反AI痕迹层 |
| [sociilabs/claude-content-writer](https://github.com/sociilabs/claude-content-writer) | 博客/LinkedIn/邮件专业写作，5阶段 GSD 流程，内置 SEO 优化 + 25项反AI写作审计 |
| [pedronauck/skills](https://github.com/pedronauck/skills) | 140个精选技能集（75个原创），其中 `content-research-writer`/`copywriting`/`humanizer`/`writing-clearly-and-concisely` 直接可用 |
| [kaisdavis/claude-skills](https://github.com/kaisdavis/claude-skills) | `docs-update`（会话结束自动同步多文档）、`open-source-skill`（内部文档公开化）写作治理工具 |

---

### 🎨 视觉生成与设计

> 文生图、配图、信息图、Logo 与品牌视觉资产生成。

| Skill | 说明 |
|---|---|
| [`image-generate-multiapi`](./image-generate-multiapi) | 多模型统一文生图（GPT-Image/Gemini/Azure） |
| [`danger-gemini-webapi`](./danger-gemini-webapi) | Gemini Web 图片与文本能力接入（逆向） |
| [`article-cover-generator`](./article-cover-generator) | 文章封面图生成（5 维度风格） |
| [`article-image-illustrator`](./article-image-illustrator) | 文章段落自动配图（位置识别+提示词生成） |
| [`document-illustrator`](./document-illustrator) | 文档内容智能配图（封面+正文，风格锁定） |
| [`logo-svg-generator`](./logo-svg-generator) | SVG Logo 与品牌展示图生成（12 种背景风格） |
| [`visual-infographic-generator`](./visual-infographic-generator) | 专业信息图生成（21 种布局） |
| [`diagram-svg-generator`](./diagram-svg-generator) | SVG 架构图/流程图/时序图（暗色主题） |
| [`content-comic-generator`](./content-comic-generator) | 知识内容漫画生成（多风格） |
| [`image-compress-optimizer`](./image-compress-optimizer) | 图片压缩优化（WebP/PNG，自动降质） |
| [`social-image-cards`](./social-image-cards) | 社媒图文卡片系列生成 |
| [`xhs-social-card`](./xhs-social-card) | 归藏风小红书图文卡片/公众号封面生成 |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [b1rdmania/claude-brand-skills](https://github.com/b1rdmania/claude-brand-skills) | 品牌全流程开发（8阶段）：从品牌叙事→视觉方向→Logo开发→字形→设计系统→交付物，多模型图像生成 |
| [op7418/logo-generator-skill](https://github.com/op7418/logo-generator-skill) | SVG Logo 生成器：6+种变体 + 12种专业展示背景（void/frosted/spotlight/iridescent 等），Nano Banana 渲染 |
| [dancolta/gen-images-skill](https://github.com/dancolta/gen-images-skill) | 品牌感知图片生成：扫描 Tailwind/CSS 提取视觉标识，为网站缺失位置生成与品牌风格一致的图片 |
| [EmmaStoneX/claude-design-skill](https://github.com/EmmaStoneX/claude-design-skill) | HTML 视觉设计专家（落地页/Deck/原型/动画/海报），来自 Claude.ai 内部 Design 系统提示词改编 |

---

### 🎬 视频与多媒体制作

> 从脚本到成片，剪辑包装、分镜设计、字幕处理全流程。

| Skill | 说明 |
|---|---|
| [`youtube-video-clipper`](./youtube-video-clipper) | YouTube 视频智能剪辑 + 中英双语字幕烧录 |
| [`youtube-transcript-extract`](./youtube-transcript-extract) | YouTube 字幕与封面提取 |
| [`bilibili-subtitle-download-skill`](./bilibili-subtitle-download-skill) | B 站视频字幕下载 + LLM 高质量摘要 |
| [`video-wrapper-effects`](./video-wrapper-effects) | 访谈视频综艺特效（花字/卡片/人物条，4 种主题） |
| [`seedance-video-prompt`](./seedance-video-prompt) | Seedance 2.0 产品动画提示词（4 种美学风格） |
| [`dialogue-video-skill`](./dialogue-video-skill) | 对话视频生成与处理 |
| [`jianying-editor-skill`](./jianying-editor-skill) | 剪映 AI 自动化剪辑封装（字幕/素材/动效/导出） |
| [`script-to-video-skill`](./script-to-video-skill) | 文章/脚本 → OmiVoice TTS 配音 → 完整视频 |
| [`video-storyboard-gen-skill`](./video-storyboard-gen-skill) | 视频分镜脚本生成（融合剧情结构与画面描述） |
| [`promo-creator-skills`](./promo-creator-skills) | 产品宣传片制作总控（60-90 秒，从官网/截图到成片） |
| [`AI-Animation-Skill`](./AI-Animation-Skill) | 科普内容 → 可视化 PPT 风格网页动画 |
| [`skills-douyin-text-to-text`](./skills-douyin-text-to-text) | 抖音视频 → 语音转文字 |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [AgriciDaniel/claude-video](https://github.com/AgriciDaniel/claude-video) | 完整 AI 视频生产套件：剪辑/转码/降噪/Whisper字幕/Veo生成/竖屏裁剪/社媒适配（15个子技能） |
| [MadAppGang/claude-code](https://github.com/MadAppGang/claude-code/tree/main/plugins/video-editing) | 专业视频编辑插件：FFmpeg操作 + Whisper转录 + Final Cut Pro FCPXML生成 |

---

### 📊 数据分析与可视化

> CSV/Excel 数据到洞察报告，SQL 优化，A/B 测试，业务指标追踪。（**缺失方向，待补充本地 Skill**）

*当前库内暂无专项 Skill，以下为 GitHub 热门推荐：*

| 仓库 | Stars | 说明 |
|---|---:|---|
| [dongzhang84/data-analysis-skill](https://github.com/dongzhang84/data-analysis-skill) | — | 丢入 CSV/Excel 即得：多专家并行分析 → 交互式 HTML 报告 + PowerPoint 导出（含 KPI/图表/风险卡） |
| [nimrodfisher/data-analytics-skills](https://github.com/nimrodfisher/data-analytics-skills) | — | 31 个数据分析技能：队列/漏斗/时序/A/B测试/根因/指标计算，全链路覆盖 |
| [adityawrk/analytics-with-claude-code](https://github.com/adityawrk/analytics-with-claude-code) | — | 分析团队生产配置：`/eda`/`/sql-optimizer`/`/data-quality`/`/ab-test`/`/weekly-report` 等 10 个斜杠命令 |
| [coffeefuelbump/csv-data-summarizer](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) | — | 上传 CSV 即自动分析：统计+图表+洞察（电商/财务/运营/调研多行业自适应） |
| [anthropics/skills xlsx](https://github.com/anthropics/skills/tree/main/document-skills) | ⭐ 1.4K | Anthropic 官方 xlsx 技能：操作 Excel 文件、公式、表格、图表 |

**💡 建议优先迁移方向：** `ecom-data-dashboard`（电商数据看板）、`sales-funnel-analyzer`（销售漏斗分析）

---

### 🎙️ 音频与播客

> 音频转录、播客生成、会议纪要，语音内容处理全链路。（**缺失方向，待补充本地 Skill**）

*当前库内暂无专项 Skill，以下为 GitHub 热门推荐：*

| 仓库 | Stars | 说明 |
|---|---:|---|
| [zarazhangrui/personalized-podcast](https://github.com/zarazhangrui/personalized-podcast) | ⭐ 313 | NotebookLM 同款体验：任意内容→双主持人 AI 播客 MP3，可订阅到 Apple Podcasts/Spotify/Overcast |
| [soanseng/podcast-use](https://github.com/soanseng/podcast-use) | — | 播客编辑工作流：Groq Whisper 转录 → AI 剪辑 → SRT 字幕 → YouTube 视频 → 竖版 Reels + 封面生成 |
| [terminator1333/claude-listen](https://github.com/terminator1333/claude-listen) | — | 本地会议转录（faster-whisper + pyannote 说话人分离），生成项目上下文感知会议纪要，完全离线 |
| [sgasser/claude-skill-podcast](https://github.com/sgasser/claude-skill-podcast) | — | 零成本播客：浏览器 Web Speech API，无需 API Key，多语言，含互动播放器 |

**💡 建议优先迁移方向：** `meeting-transcript-notes`（会议录音→纪要+待办）、`audio-to-article`（播客→文章）

---

### 🎪 PPT 与演示文档

> 从文档/报告自动生成演示文稿，覆盖 HTML PPT 到 AI 图片 PPT。

| Skill | 说明 |
|---|---|
| [`slides-deck-generator`](./slides-deck-generator) | 演示页 / Slide 图片生成流程 |
| [`html-ppt-guizang`](./html-ppt-guizang) | 网页横向翻页 PPT（杂志风/瑞士国际主义风，单 HTML） |
| [`ppt-image-generator`](./ppt-image-generator) | AI 生成 PPT 图片 + 可灵转场视频（Nano Banana） |
| [`gpt-image2-ppt-skills`](./gpt-image2-ppt-skills) | GPT-Image-2 生成视觉精美 PPT 幻灯片 |
| [`visual-style-ppt-skill`](./visual-style-ppt-skill) | 风格驱动 Slide 图片生成（Image 2） |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | Stars | 说明 |
|---|---:|---|
| [Akxan/ppt-agent-skill](https://github.com/akxan/ppt-agent-skill) | ⭐ 57 | 万元级 PPT 效果：26种风格 + 18种数据可视化（桑基/热力/甘特），输出 HTML + 可编辑矢量 PPTX |
| [mrigankad/SlideArchitect](https://github.com/mrigankad/SlideArchitect) | — | 演示策略师：20+版式模板，专项适配投资人路演/销售 Deck/技术架构/培训课件 |
| [daymade/claude-code-skills ppt-creator](https://github.com/daymade/claude-code-skills) | — | 带自动评分（<75分自动2次迭代）的演示稿生成，Marp + PPTX 双路输出 |
| [Gabberflast/academic-pptx-skill](https://github.com/Gabberflast/academic-pptx-skill) | — | 学术会议/论文答辩 PPT 规范（动作标题/结构论证/引用标准/图表注释） |

---

### 🔍 研究与信息采集

> 网页抓取、字幕提取、平台动态监控，信息链路入口。

| Skill | 说明 |
|---|---|
| [`news-aihot-daily`](./news-aihot-daily) | AI 热点日报与动态检索（aihot.virxact.com） |
| [`web-markdown-extract`](./web-markdown-extract) | 任意网页抓取转 Markdown |
| [`danger-x-markdown-export`](./danger-x-markdown-export) | X/Twitter 内容转存 Markdown |
| [`wechat-group-summary`](./wechat-group-summary) | 微信群聊记录摘要与群体画像 |
| [`research-hv-analysis`](./research-hv-analysis) | 横纵分析法深度研究报告 |
| [`last30days-skill-cn`](./last30days-skill-cn) | 中国 8 大平台近 30 天深度研究（微博/小红书/B站/知乎/抖音…） |
| [`content-collector-skill`](./content-collector-skill) | 多平台内容采集（X/微信/即刻/Reddit） |
| [`boss-daily-brief`](./boss-daily-brief) | Boss 直聘每日招聘初筛简报 |
| [`text-translate-workflow`](./text-translate-workflow) | 多模式翻译（快翻/常规/精修） |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [BexTuychiev/firecrawl-claude-code-skill](https://github.com/BexTuychiev/firecrawl-claude-code-skill) | Firecrawl 网页抓取：Markdown 提取/截图/结构化数据/网页搜索/文档整站爬取（支持 500+ 信用免费额度） |
| [Cedriccmh/claude-code-skill-scrapling](https://github.com/Cedriccmh/claude-code-skill-scrapling) | 智能爬虫（自动选 Fetcher）：支持 Cloudflare/WAF 绕过、登录态会话、站点模式库 |
| [webcpu/deep-research-skill](https://github.com/webcpu/deep-research-skill) | 并行多 Agent 深度研究：3-5 个 Opus Agent 并行搜索→合成→注明出处的 Markdown 报告 |
| [pete-builds/claude-research-agent](https://github.com/pete-builds/claude-research-agent) | 反幻觉引文研究：严格引用纪律 + 置信度评估，输出 Markdown + 可分享 HTML（含 portable 版无需自建 MCP） |

---

### 📈 增长策略与 SEO

> Product Hunt 发布、SEO 外链、B2B 增长、GEO 引用追踪。

| Skill | 说明 |
|---|---|
| [`growth-research`](./growth-research) | Gingiris 增长工具包主入口 |
| [`growth-aso-optimizer`](./growth-aso-optimizer) | ASO + App 冷启动（关键词/metadata/UGC） |
| [`growth-b2b-engine`](./growth-b2b-engine) | B2B SaaS 全生命周期增长（PLG/SLG，到 $10M ARR） |
| [`growth-seo-backlinks`](./growth-seo-backlinks) | 系统外链建设（5 种渠道策略） |
| [`growth-blog-writer`](./growth-blog-writer) | Jekyll 博客 SEO 写作与发布流水线 |
| [`growth-competitor-intel`](./growth-competitor-intel) | 竞品深度扫描（落地页/定价/博客/SEO） |
| [`growth-geo-citations`](./growth-geo-citations) | GEO 引用追踪 + AI 搜索曝光优化 |
| [`growth-oss-marketing`](./growth-oss-marketing) | 开源项目发布整合营销（GitHub star/KOL/Reddit/HN） |
| [`growth-producthunt-launch`](./growth-producthunt-launch) | Product Hunt 发布剧本（T-14 预热到 T+7 复盘） |
| [`growth-seo-monitor`](./growth-seo-monitor) | 每日 SEO/GEO 巡逻（SERP 排名/Google 索引/llms.txt） |
| [`growth-social-insights`](./growth-social-insights) | 博客→社媒多变体分发（X/小红书/LinkedIn） |
| [`growth-user-interview`](./growth-user-interview) | 用户访谈框架（HeyGen 937 次访谈找 PMF 方法论） |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [openai/skills](https://github.com/openai/skills) | OpenAI 官方技能库，含 `gh-address-comments`、`create-plan`，可与增长 SEO 工作流组合 |
| [AlirezaRezvani/claude-skills](https://github.com/AlirezaRezvani/claude-skills) | 含 SEO/营销/内容分发工作流，533 个 stdlib-only Python 工具，支持 Claude Code/Codex/Gemini CLI 等 13 个平台 |
| [noique/cross-border-ecommerce-skills](https://github.com/noique/cross-border-ecommerce-skills) 的 `outbound-prospecting` | 海外客户开拓（含 Python 脚本 + CSV 追踪器的完整外联技能包） |

---

### 💼 职场、办公与工程治理

> WPS 办公自动化、飞书协作、求职招聘、会话知识同步。

| Skill | 说明 |
|---|---|
| [`feishu-bitable-skill`](./feishu-bitable-skill) | 飞书多维表格全生命周期管理（建表/CRUD/视图） |
| [`lark-todo-skill`](./lark-todo-skill) | 飞书全平台待办扫描（8 源并行采集，按优先级汇总） |
| [`lark-fashion-cockpit`](./lark-fashion-cockpit) | 女装电商运营驾驶舱（38 大能力，飞书 CLI 数字化方案） |
| [`workflow-neat-sync`](./workflow-neat-sync) | 会话收尾知识同步（文档/CLAUDE.md/Agent 记忆三层对齐） |
| [`boss-auto-job`](./boss-auto-job) | Boss 直聘自动求职（隐身搜索→多 Agent 匹配→投递） |
| [`job-hunter-skill`](./job-hunter-skill) | 定时求职助手（自动发现/筛选/记录合适岗位） |

**WPS 办公自动化（42 项，按场景取用）：**

| 场景 | 代表 Skill |
|---|---|
| 文档写作 | `wps-docx-writer`、`wps-report-writer`、`wps-contract`、`wps-gongwen`→`wps-official-doc` |
| PPT 制作 | `wps-ppt-generator`、`wps-ppt-outline`、`wps-ppt-polish`、`wps-ppt-speaker-notes` |
| 数据处理 | `wps-data-clean`、`wps-data-visualization`、`wps-formula`、`wps-vlookup`、`wps-pivot` |
| 财务报表 | `wps-financial-report`、`wps-salary`、`wps-budget` |
| HR 场景 | `wps-resume-chinese`、`wps-exam-paper`、`wps-certificate`、`wps-attendance` |
| 日程规划 | `wps-gantt`、`wps-schedule`、`wps-cn-calendar`→`wps-chinese-calendar` |
| 格式与转换 | `wps-format-fix`、`wps-batch-convert`、`wps-pdf-extract`、`wps-pdf-merge-split` |
| 宏与自动化 | `wps-jsa-macro`→`wps-js-macro`、`wps-template-engine`、`wps-mail-merge` |

**来自 GitHub 的高价值 Skill 推荐（可直接安装）：**

| 仓库 | 说明 |
|---|---|
| [thoniorf/pm-claude-skills](https://github.com/thoniorf/pm-claude-skills) | 多职能专业技能库：PM/工程/客户成功/营销/设计/法务/财务/HR/销售，含 Linear/Jira/Slack/Notion 对接模板 |
| [dongzhang84/data-analysis-skill](https://github.com/dongzhang84/data-analysis-skill) | 端到端数据分析：多专家并行推理 → 交互式 HTML 报告（图表/洞察/风险卡）+ 一键 PPTX 导出 |
| [nimrodfisher/data-analytics-skills](https://github.com/nimrodfisher/data-analytics-skills) | 31个数据分析技能包：队列分析/漏斗分析/时间序列/A/B测试/根因排查/业务指标计算 |
| [adityawrk/analytics-with-claude-code](https://github.com/adityawrk/analytics-with-claude-code) | 分析团队生产级配置：`/eda`/`/sql-optimizer`/`/ab-test`/`/weekly-report` 等10个斜杠命令 |

---

## 📚 技能包索引（Bundles）

> 技能包内含多个子 Skill，建议按包内 README 或子目录路径安装。

| 目录 | 子 Skill 数量 | 说明 |
|---|---:|---|
| [`ecomm-ai-skills-hub`](./ecomm-ai-skills-hub) | 180+ | 电商 AI 技能大集合（tile.json 体系） |
| [`xiaohongshu-skills`](./xiaohongshu-skills) | 139 | 小红书全场景技能包 |
| [`ecommerce-detail-page-skills`](./ecommerce-detail-page-skills) | 11 | 电商详情页文案（母婴/美妆/食品/3C 等分品类） |
| [`system-prompt-skills`](./system-prompt-skills) | 15 | 系统提示词设计技能集（记忆/人格/安全/输出格式） |
| [`videoclip-AI-skill`](./videoclip-AI-skill) | 6 | AI 视频剪辑技能包（字幕/剪口播/划重点） |
| [`ai-video-skills`](./ai-video-skills) | 5 | AI 视频创作技能包（产品介绍/动画/特效） |
| [`lanshu-awesome-ai-video-kit`](./lanshu-awesome-ai-video-kit) | 7 | 蓝书 AI 视频工具包（Seedance/Kling 系列） |
| [`xhs-claude-skills`](./xhs-claude-skills) | 4 | 小红书 Claude 技能包（发布/封面/批量/分析） |
| [`obsidian-skills`](./obsidian-skills) | 5 | Obsidian 知识库管理技能包 |
| [`axton-obsidian-visual-skills`](./axton-obsidian-visual-skills) | 3 | Obsidian 可视化（Canvas/Mermaid/Excalidraw） |
| [`ai-ecommerce-agent-skills`](./ai-ecommerce-agent-skills) | 10 | 电商 AI Agent 技能包（含选股分析） |
| [`workflow-skill`](./workflow-skill) | 3 | 工作流平台技能包（Dify/Coze/ComfyUI） |
| [`agent-skills`](./agent-skills) | 3 | 中国合规检查技能（广告/商务/电商合规） |
| [`Bright-Data-MCP-Claude-Skill-deep-research`](./Bright-Data-MCP-Claude-Skill-deep-research) | 2 | Bright Data MCP 深度研究技能 |
| [`amazon-alibaba-crossborder-skill-image-generator`](./amazon-alibaba-crossborder-skill-image-generator) | 2 | 亚马逊/阿里跨境图片生成器 |
| [`MaxC-skills`](./MaxC-skills) | 1 | 每日销售摘要 |
| [`codex-ppt-skill`](./codex-ppt-skill) | 1 | Codex PPT 生成技能 |
| [`video-recap`](./video-recap) | 1 | 视频内容回顾技能 |
| [`seedance-prompt-skill`](./seedance-prompt-skill) | 1 | Seedance 提示词专项技能 |
| [`lark-fashion-cockpit`](./lark-fashion-cockpit) | 多子技能 | 飞书女装电商运营子技能集 |

---

## 🔗 推荐工作流

```
研究选题        last30days-skill-cn / news-aihot-daily / research-hv-analysis
      ↓
内容创作        writing-khazix-style / Viral_Writer_Skill / social-account-doctor
      ↓
视觉配图        article-image-illustrator / ecom-product-image / logo-svg-generator
      ↓
格式适配        markdown-html-wechat / xhs-social-card / social-image-cards
      ↓
多平台发布      publish-wechat-official / publish-weibo-post / publish-x-post / XiaohongshuSkills
      ↓
效果复盘        ReviewMind-Skills / growth-seo-monitor / growth-social-insights
```

| 场景 | 推荐链路 |
|---|---|
| 公众号生产 | `research-hv-analysis` → `writing-khazix-style` → `document-illustrator` → `markdown-html-wechat` → `publish-wechat-official` |
| 小红书爆款 | `last30days-skill-cn` → `social-account-doctor` → `Viral_Writer_Skill` → `xhs-social-card` → `XiaohongshuSkills` |
| 电商视觉链路 | `ecommerce-product-research-skills` → `ecom-product-image` → `ecommerce-visual-copywriting-skill` → `1click-ecom-detailpage` |
| 视频内容处理 | `youtube-transcript-extract` → `youtube-video-clipper` → `video-wrapper-effects` → `skills-douyin-text-to-text` |
| 增长 SEO | `growth-competitor-intel` → `growth-seo-backlinks` → `growth-blog-writer` → `growth-seo-monitor` |
| 办公自动化 | `wps-data-clean` → `wps-data-visualization` → `wps-report-writer` → `lark-todo-skill` |

---

## 🗺️ ROADMAP

### v0.2（进行中）

- [ ] 统一所有 Skill 的 `SKILL.md` 描述格式（中英双语 + 使用场景 + 依赖说明）
- [ ] 为每个 Skill 添加 `examples/` 实战示例目录
- [ ] 完善 wps-* 42 个技能的独立说明文档
- [ ] 补充 ecom-product-image 的电商场景示例图
- [ ] 新增：`ecom-review-monitor`（电商评论舆情监控）
- [ ] **新增 📊 数据分析方向**：`sales-funnel-analyzer`、`ecom-data-dashboard`、`csv-report-generator`
- [ ] **新增 🎙️ 音频播客方向**：`meeting-transcript-notes`（会议录音→纪要）、`audio-to-article`（播客→文章）

### v0.3（规划中）

- [ ] 中国合规体系：广告法/敏感词/医疗合规检查一体化 Skill
- [ ] **私域运营系列**：企业微信自动化/群助手/朋友圈运营/SCRM 集成
- [ ] B2B 内容营销套件：LinkedIn 文章 + 白皮书 + 案例故事
- [ ] AI 视频评论区运营：自动回复/关键词监控/差评处理
- [ ] **品牌视觉 AI 套件**：基于 `b1rdmania/claude-brand-skills` 汉化移植（8阶段全流程）
- [ ] 多语言本地化：将核心 Skill 的提示词翻译为英/日/韩版本

### v1.0（长期目标）

- [ ] 提供 Skill 自动测试框架（可验证 SKILL.md 描述与实际行为是否一致）
- [ ] 建立"Skill 组合模板"（按业务场景打包的一键安装套件）
- [ ] 开放 Skill 投稿机制与质量审核 SOP
- [ ] 与主流 Agent 平台（Coze/Dify/FastGPT）打通安装接口
- [ ] **生态对接**：接入 [claudskills.com](https://claudskills.com) 公开目录（69K+ Skills 索引），提高可发现性

---

## 🙏 致谢

本仓库收录和参考了以下开源社区和创作者的工作，向他们表示诚挚感谢：

| 仓库 / 作者 | 贡献说明 |
|---|---|
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 早期 Skill 结构规范与工具集（web-markdown-extract、youtube-transcript-extract 等核心工具链） |
| [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | writing-khazix-style、research-hv-analysis 等写作与研究 Skill 灵感来源 |
| [gingiris/gingiris-skills](https://github.com) | growth-* 系列 12 个增长策略 Skill（ASO/B2B/SEO/PH 发布等） |
| [guizang PPT 系列](https://github.com) | html-ppt-guizang、xhs-social-card 等视觉风格 Skill |
| [NanoBanana/PPT-Generator-Pro](https://github.com) | ppt-image-generator（AI 图片 PPT + 可灵转场视频方案） |
| [lanshu-awesome-ai-video-kit](https://github.com) | Seedance/Kling 视频提示词技能包 |
| [ecommerce-detail-page-skills](https://github.com) | 电商详情页文案分品类 Skill 体系 |
| [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) | GPT-Image-2 电商图片 25 个高质量模板 |
| [coolqoo/1click-ecom-detailpage](https://github.com/coolqoo/1click-ecom-detailpage) | 跨境电商一键详情页灵感与初步工作 |
| [AgentSkills](https://agentskills.io) | Skill 标准规范与 SKILL.md 格式定义 |

> 如果你的工作被收录但未被正确致谢，请开 Issue 告知，我会第一时间补充。

---

## 贡献指南

欢迎提交新 Skill 或改进现有 Skill！

```bash
# 1. Fork 本仓库
# 2. 在根目录新建你的 skill 目录
mkdir my-skill && cd my-skill

# 3. 创建 SKILL.md（参考现有 skill 格式）
# 必须包含：name、description、触发条件、使用示例

# 4. （可选）添加 README.md、examples/ 和 references/

# 5. 提交 PR，说明 skill 的使用场景和实测效果
```

**Skill 质量标准：**
- 根目录下存在 `SKILL.md`，包含 `name`（与目录名一致）、`description` 字段
- `description` 清晰说明：是什么、什么时候用、触发关键词
- 命名使用 `kebab-case`，两段或三段式，见名知意

---

## 许可协议

本仓库以 [MIT License](./LICENSE) 开源，可自由使用、修改、再分发。  
部分 `danger-*` 系列技能涉及浏览器自动化或逆向接口，请在平台 ToS 与本地法律允许范围内使用。

---

<div align="center">

Made with ❤️ by **越哥**（Yue）

微信公众号：**越哥聊AI** · 微信交流群：**越哥AI智能体**

[GitHub](https://github.com/bingyue) · [MIT License](./LICENSE)

</div>
