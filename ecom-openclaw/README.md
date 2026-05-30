# OpenClaw Ecommerce Skill

> **电商爆款分析流水线** — 商品采集 → 热度计算 → 报表生成，全自动化

[![OpenClaw](https://img.shields.io/badge/OpenClaw-≥2026.2.26-blue)](https://openclaw.ai)
[![Data Source](https://img.shields.io/badge/Data-Fake%20Store%20API-orange)](https://fakestoreapi.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 一句话介绍

👉 **拉取商品 → 计算热度 → 输出报表**，一条指令完成电商选品分析全流程

你只需要说一句话：

```
帮我分析当前电商热门商品，生成爆款报表
```

OpenClaw 会自动完成：采集 → 评分 → 报表 全部工作。

---

## 核心演示流程

```
用户：帮我分析当前电商热门商品，找出 electronics 类目的爆款

ecommerce_agent（主控）
├── Step 1: product_fetcher      → 从 Fake Store API 采集商品数据
├── Step 2: hot_score_analyzer   → 计算热度分 (score = rate × count)
└── Step 3: report_generator     → 生成 Markdown 热度分析报表
```

---

## Agent 体系

| Agent ID | 名称 | 职责 | 对应 Skill |
|----------|------|------|-----------|
| `ecommerce_agent` | 电商分析主控 | 调度全流程，理解用户意图 | — |
| `product_fetcher` | 商品采集器 | 从 Fake Store API 拉取标准化商品数据 | `fetch-products` |
| `hot_score_analyzer` | 爆款评分器 | 计算热度评分并排序 | `hot-score` |
| `report_generator` | 报表生成器 | 生成 Markdown 格式分析报表 | `report-generator` |

---

## 安装要求

- **Node.js**: v22 或更高版本
- **OpenClaw**: ≥ 2026.2.26（`npm install -g openclaw`）
- **网络**: 可访问 `https://fakestoreapi.com`（无需登录或 API Key）

---

## 快速安装

```bash
# 克隆项目
git clone https://github.com/your-org/commerce-claw.git
cd commerce-claw/openclaw-ecommerce-skill

# 一键安装
./install.sh

# 指定 OpenClaw 根目录（可选）
OPENCLAW_ROOT=~/.openclaw ./install.sh
```

安装成功后启动电商分析主控：

```bash
openclaw chat --agent ecommerce_agent
```

---

## 在其他 IM 工具里怎么触发

如果你不是在终端里直接运行 `openclaw chat --agent ecommerce_agent`，而是在飞书、Slack、Telegram、企业微信这类 IM 工具里和 OpenClaw 对话，核心原则只有一条：

**让这条消息被路由到 `ecommerce_agent`。**

### 触发前提

要满足下面 3 个条件：

- 这个 Skill 已经通过 `./install.sh` 安装到目标 OpenClaw 实例
- 你的 IM 机器人 / 消息网关已经接到同一个 OpenClaw 实例
- 该 IM 会话支持以下两种方式之一：`默认 Agent 路由` 或 `显式指定 Agent`

### 触发方式 1：把会话默认路由到 `ecommerce_agent`

如果你的 IM 集成层支持给某个群聊、频道或机器人会话绑定默认 Agent，那么把默认 Agent 配成：

```text
ecommerce_agent
```

配置好之后，用户在 IM 里直接说自然语言即可触发：

```text
帮我分析当前电商热门商品，生成爆款报表
```

```text
找出 electronics 类目的爆款商品
```

```text
帮我筛选价格低于 30 美元的 Top 10 热门商品
```

### 触发方式 2：在消息里显式指定 Agent

如果你的 IM 集成层没有“默认 Agent”概念，就需要在消息里明确告诉 OpenClaw 使用哪个 Agent。

推荐写法：

```text
调用 ecommerce_agent：帮我分析当前电商热门商品，生成爆款报表
```

```text
@OpenClaw 使用 ecommerce_agent，找出 electronics 类目热度最高的商品
```

```text
use ecommerce_agent to analyze top hot products under $30
```

### 推荐触发口令

为了让路由更稳定，建议在其他 IM 中优先使用下面这种句式：

```text
调用 ecommerce_agent：<你的分析需求>
```

例如：

```text
调用 ecommerce_agent：生成一份全品类商品热度分析报表
```

```text
调用 ecommerce_agent：只看 women's clothing 类目，输出 Top 5 爆款
```

### 如果没有触发成功，优先检查

- Skill 是否已经安装在当前 OpenClaw 实例中
- 外部 IM 机器人连接的是否是同一个 OpenClaw 实例
- 路由层是否允许调用 `ecommerce_agent`
- 是否把消息发给了默认 Agent，而不是电商分析 Agent
- 是否在消息里明确写出了 `ecommerce_agent`

### 一句话理解

在其他 IM 工具里，这个 Skill 不是靠“平台类型”触发的，而是靠**消息路由到 `ecommerce_agent`** 触发的。

---

## 使用示例

### 场景 1：全品类爆款分析

```
> 帮我分析当前电商热门商品

✅ 分析完成！
- 采集商品：20 件
- 最高热度分：1061.9（Mens Casual Premium Slim Fit T-Shirts）
- 报表已生成（Markdown 格式）
```

### 场景 2：指定类目筛选

```
> 找出 electronics 类目评分最高的商品

✅ 已筛选 electronics 类目，共 6 件商品：
Top 1: WD 2TB Elements Portable External Hard Drive — 热度分 669.9
Top 2: SanDisk SSD PLUS 1TB Internal SSD — 热度分 565.8
...
```

### 场景 3：价格区间 + Top-N

```
> 帮我找出价格低于 30 美元的 Top 5 爆款商品

✅ 过滤条件：价格 ≤ $30，Top 5
[生成对应报表...]
```

### 场景 4：仅生成评分数据，不生成报表

```
> 只给我商品评分列表，不需要报表格式

✅ 已输出 JSON 格式评分列表（按热度降序）
```

---

## 报表输出格式

```markdown
# 商品热度分析报表

**生成时间**：2026/4/22 13:00:00
**商品总数**：20 件
**分析类目**：全品类

---

## 📊 类目热度汇总

| 类目 | 商品数 | 平均热度分 | 最高热度分 |
|------|--------|-----------|-----------|
| electronics | 6 | 312.4 | 520.0 |
| men's clothing | 4 | 287.6 | 468.0 |
| women's clothing | 6 | 241.2 | 395.0 |
| jewelery | 4 | 198.5 | 310.0 |

---

## 🏆 商品热度榜单

## 1. Mens Casual Premium Slim Fit T-Shirts
- **价格**：$22.3
- **类目**：men's clothing
- **评分**：4.1 / 5.0（259 条评价）
- **热度分**：1061.9 🔥🔥🔥

## 2. WD 2TB Elements Portable External Hard Drive
- **价格**：$64.0
- **类目**：electronics
- **评分**：3.3 / 5.0（203 条评价）
- **热度分**：669.9 🔥🔥🔥
```

---

## 热度评分算法

```
score = rating.rate × rating.count
```

| 参数 | 含义 |
|------|------|
| `rating.rate` | 商品平均评分（0~5 分），代表**质量** |
| `rating.count` | 评价总数量，代表**市场热度 / 销量规模** |

| 热度分区间 | 等级 | 说明 |
|-----------|------|------|
| ≥ 400 | 🔥🔥🔥 超级爆款 | 高评分 + 海量评价 |
| 300 ~ 399 | 🔥🔥 热门商品 | 综合表现优秀 |
| 200 ~ 299 | 🔥 潜力商品 | 值得关注 |
| 100 ~ 199 | ⚡ 普通商品 | 正常水平 |
| < 100 | 💤 冷门商品 | 需观察 |

---

## 数据源说明

本项目使用 [Fake Store API](https://fakestoreapi.com)，原因：

- 无需登录或 API Key，零配置直接使用
- 数据结构标准化（商品 / 价格 / 类目 / 评分）
- Demo 稳定可运行，无反爬问题
- 专注于"流程设计"，而非"数据真实性"

**商品字段结构：**

```json
{
  "id": 1,
  "title": "Fjallraven - Foldsack No. 1 Backpack",
  "price": 109.95,
  "category": "men's clothing",
  "rating": {
    "rate": 3.9,
    "count": 120
  }
}
```

**支持的类目：**

| 类目 | 描述 |
|------|------|
| `electronics` | 电子产品 |
| `jewelery` | 珠宝首饰 |
| `men's clothing` | 男装 |
| `women's clothing` | 女装 |

---

## 项目结构

```
openclaw-ecommerce-skill/
├── README.md               # 使用文档
├── agents.json             # 4 个 Agent 配置
├── install.sh              # 一键安装脚本
├── uninstall.sh            # 卸载脚本
└── souls/
    ├── ecommerce_agent.md      # 主控 Agent Soul
    ├── product_fetcher.md      # 商品采集器
    ├── hot_score_analyzer.md   # 爆款评分器
    └── report_generator.md     # 报表生成器
```

---

## Agent 通信架构

```
                    ┌─────────────────────┐
                    │   ecommerce_agent   │  ← 用户入口（主控）
                    │     （主控中心）      │
                    └──────────┬──────────┘
                               │ agentToAgent（串行调度）
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  product_fetcher │→ │hot_score_analyzer│→ │ report_generator │
│  （商品数据采集） │  │  （热度评分计算） │  │  （报表输出渲染） │
│  Fake Store API  │  │ rate × count     │  │  Markdown 格式   │
└──────────────────┘  └──────────────────┘  └──────────────────┘
        Step 1                Step 2                Step 3
```

---

## 完整工作流

```
fetch-products（商品采集）
      ↓
hot-score（爆款评分）
      ↓
report-generator（报表生成）
```

---

## 后续升级方向

本项目作为最小可运行 Demo，后续可扩展：

- [ ] 引入 TikTok Shop / Amazon 真实数据源
- [ ] 加入 LLM 爆款趋势预测（GPT/Claude 辅助分析）
- [ ] 加入利润模型计算（价格 / 成本 / 毛利率）
- [ ] 接入真实选品系统（1688 / 速卖通 API）
- [ ] 支持定时自动分析（Cron Job 触发）
- [ ] 输出结果同步到飞书文档 / 多维表格

---

## 卸载

```bash
./uninstall.sh
```

---

## 设计约束说明

本项目刻意采用 Fake Store API，原因：

- 避免真实电商平台反爬问题
- 保证 Demo 稳定可运行
- 降低开发调试成本
- 专注于"流程设计"，而非"数据真实性"

---

## 项目核心一句话总结

> This project demonstrates how OpenClaw Skills can be composed into a simple yet complete e-commerce data pipeline: **data fetching → scoring → reporting**.

---

## License

MIT
