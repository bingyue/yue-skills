# CHANGELOG

## [1.0.0] - 2026-05-30

### V1.0 正式发布

**新增 Skill（11 个）**
- `ecom-review-monitor` — 电商评论舆情监控，差评预警/竞品挖掘/情感分析/周报
- `sales-funnel-analyzer` — 销售漏斗转化率分析，识别瓶颈，输出优化建议
- `ecom-data-dashboard` — 电商数据看板，GMV/转化率/客单价/复购率，HTML 看板或 Markdown 周报
- `csv-report-generator` — 通用 CSV 智能报告，自动识别数据类型，洞察+图表建议
- `meeting-transcript-notes` — 会议录音/字幕/文字稿 → 结构化纪要（决议/待办/负责人）
- `audio-to-article` — 播客/字幕/演讲录音 → 可读文章，适配公众号/博客/LinkedIn
- `cn-compliance-check` — 中国合规一体化：广告法极限词/敏感词/医疗违禁词，风险分级报告
- `wecom-private-domain` — 企业微信私域运营全流程：群 SOP/朋友圈/用户分层/SCRM
- `b2b-content-suite` — B2B 内容营销套件：LinkedIn 文章/白皮书/客户案例/行业报告
- `video-comment-ops` — 视频评论区运营：评论分类/差评处理/回复模板/口碑管理
- `brand-visual-ai` — 品牌视觉 AI 全流程（8 阶段）：叙事→Logo→设计系统→交付物

**基础建设（延续自 0.x 阶段）**
- 96 个 Skill 覆盖 8 大场景方向
- 全库命名标准化（两/三段式 kebab-case，65 项重命名）
- 单一根目录 `.gitignore`（整合 51 个嵌套文件）
- 完整中英文 README + ROADMAP 更新

---

## [0.3.0] - 2026-05-30

### 命名标准化 + README 全面重构

- 65 个 Skill 目录重命名（统一分类前缀：ecom-/video-/image-/write-/ppt-/research-/lark-/job-）
- 同步所有 `SKILL.md` 的 `name` 字段与目录名一致
- README.md 全面重写：作者介绍/分类索引/安装指南/GitHub 推荐/致谢/贡献指南
- 新增"📊 数据分析与可视化"和"🎙️ 音频与播客"两个分类方向（含 GitHub 热门推荐）

## [0.2.0] - 2026-05-30

### 批量迁移 + gitignore 整理

- 迁移 6 批技能（gingiris/awesome-amazon/influencer/text-check/wps/common，共 55 个）
- 新增批命名标准化（gr*/wps-* 系列）
- 整合 51 个嵌套 `.gitignore` 为单一根文件
- 删除嵌套 `.git` 目录

## [0.1.0] - 2026-05-28

### 初始发布

- 从 baoyu-skills/archive 迁移 8 批核心 Skill
- 建立基础目录结构与 README
- 配置 Git 提交人（bingyue / bingyue56@163.com）
- 初次推送至 GitHub
