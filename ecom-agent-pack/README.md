# AI 电商 Agent Skills

OpenClaw AI Agent 的电商设计技能包，包含生图、电商设计、竞品分析、审美记忆等完整工作流。

## 技能清单

| 技能 | 说明 |
|------|------|
| `nano-banana2` | Gemini 多模态 AI — 文生图、图生图、Vision 分析 |
| `ecommerce-designer` | 电商美工助手 — 详情页、海报、Banner、社媒封面 |
| `design-pipeline` | 美工全流程 — 从参考店铺到成品设计的自动化工作流 |
| `store-teardown` | 店铺视觉拆解 — 分析竞品配色、排版、摄影风格 |
| `taobao` | 电商比价 — 淘宝/京东/拼多多/抖音/快手商品搜索 |
| `ui-ux-pro-max` | UI/UX 设计智能 — BM25 搜索 8 大设计领域 |
| `upload-media` | 媒体上传 — 即梦(Jimeng) VOD 平台上传 |
| `xhs-note-creator` | 小红书笔记 — Markdown 到图片卡片渲染+发布 |
| `stock-analyst` | 美港股分析 — 盘前指标+量化模型+组合追踪 |
| `pitfall-experience` | 踩坑知识库 — 自动记录和检索历史问题解决方案 |

## 审美记忆系统

`aesthetic-memory/` 目录包含品牌审美知识库：

- `aesthetic.md` — 审美工作记忆操作手册 (Preflight → Solidify)
- `aesthetic-fragments.md` — 11 条单条审美经验 (含 7 条负面碎片)
- `aesthetic-patterns.md` — 3 个可复用的风格模式 (含 Prompt 模板)
- `brand-seek-within.md` — SEEK WITHIN 品牌完整档案
- `brand-1747.md` — 1747 大话国潮品牌档案

## Workspace 配置

`workspace-config/` 目录包含 Agent 运行时配置：

- `AGENTS.md` — 主指令文件 (Preflight、自检协议、行为红线)
- `SOUL.md` — Agent 人格定义
- `IDENTITY.md` — Agent 身份
- `TOOLS.md` — 工具链笔记
- `MEMORY.md` — 长期记忆索引
- `USER.md` — 用户档案

## 依赖

- Python 3.10+
- Playwright (chromium)
- Gemini API Key
- 各技能的 Python 依赖见对应 `scripts/` 目录

## 验证状态

使用 skill-creator 框架验证通过：
- 结构验证: 10/10 PASS
- 功能断言: 46/46 PASS (100%)
- 质量评分: 平均 6.9/10

