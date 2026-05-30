# OpenClaw Ecommerce Team Skill

> 电商运营 AI 团队 —— 10 个专属 Agent，3 个自动工作流，支持 Agent-to-Agent 协作

---

## 目录结构

```
openclaw-ecommerce-team/
├── package.json                    # 项目依赖与脚本
├── tsconfig.json                   # TypeScript 编译配置
├── skill.config.json               # OpenClaw Skill 配置（含 Agent 与 Workflow 注册）
├── install.sh                      # 一键安装脚本
├── README.md                       # 本文档
└── src/
    ├── index.ts                    # Skill 主入口，负责初始化所有 Agent 与 Workflow
    ├── agents/
    │   ├── traffic-strategist/     # 流量策略官
    │   │   ├── Soul.md             # Agent 灵魂文档（人格/价值观/行为准则）
    │   │   └── skill.ts            # Agent 能力定义
    │   ├── ads-optimizer/          # 广告优化师
    │   ├── content-marketer/       # 内容营销官
    │   ├── product-architect/      # 商品架构师
    │   ├── inventory-guard/        # 库存守护者
    │   ├── order-processor/        # 订单处理官
    │   ├── aftersales-manager/     # 售后管理官
    │   ├── customer-replier/       # 客户回复官
    │   ├── review-guardian/        # 评价守护者
    │   └── data-director/          # 数据总监
    └── workflows/
        ├── daily-report.workflow.json     # 每日 08:00 销售日报
        ├── order-flow.workflow.json       # 每 5 分钟订单轮询
        └── growth-cycle.workflow.json    # 每周增长周期任务
```

---

## 快速安装

### 方式一：使用 install.sh（推荐）

```bash
cd openclaw-ecommerce-team
bash install.sh
```

### 方式二：使用 OpenClaw CLI

```bash
cd openclaw-ecommerce-team
npm install
npm run build
openclaw skill install .
```

### 方式三：手动安装

```bash
cd openclaw-ecommerce-team
npm install
npm run build
npm start
```

> **要求：** Node.js >= 22.0.0

---

## 10 个 Agent 介绍

| Agent 名称 | 角色 | 核心能力 |
|---|---|---|
| `traffic-strategist` | 流量策略官 | 流量分析、趋势预测、活动策划 |
| `ads-optimizer` | 广告优化师 | 广告投放、ROI 优化、预算分配 |
| `content-marketer` | 内容营销官 | 内容创作、SEO 优化、素材管理 |
| `product-architect` | 商品架构师 | 商品选品、定价策略、类目管理 |
| `inventory-guard` | 库存守护者 | 库存监控、补货预警、滞销处理 |
| `order-processor` | 订单处理官 | 订单审核、物流跟踪、异常处理 |
| `aftersales-manager` | 售后管理官 | 退换货处理、纠纷调解、满意度管理 |
| `customer-replier` | 客户回复官 | 智能客服、咨询解答、关系维护 |
| `review-guardian` | 评价守护者 | 评价监控、差评处理、口碑管理 |
| `data-director` | 数据总监 | 数据分析、报表生成、决策支撑 |

---

## 3 个 Workflow

### 1. daily-report（每日销售日报）

- **触发时间：** 每天 08:00
- **执行 Agent：** `data-director`
- **输出：** 前一天销售数据汇总报告

```json
{
  "trigger": { "type": "cron", "expression": "0 8 * * *" },
  "steps": [{ "agent": "data-director", "action": "generateDailyReport" }]
}
```

### 2. order-flow（订单自动流转）

- **触发时间：** 每 5 分钟
- **执行 Agent：** `order-processor` → 异常时转发 `aftersales-manager`
- **逻辑：** 自动轮询新订单，异常订单自动转售后

### 3. growth-cycle（每周增长周期）

- **触发时间：** 每周一 09:00
- **执行 Agent：** `traffic-strategist` → `ads-optimizer` → `content-marketer`
- **逻辑：** 分析上周流量 → 调整广告策略 → 更新营销素材

---

## 如何启用 Workflow

### 启动所有 Workflow

```bash
npm run workflow:start
# 或
node dist/index.js --start-workflows
```

### 启动单个 Workflow

```typescript
import { WorkflowEngine } from './src/index';

const engine = new WorkflowEngine();
await engine.startWorkflow('daily-report');
await engine.startWorkflow('order-flow');
await engine.startWorkflow('growth-cycle');
```

### 通过 OpenClaw CLI 管理

```bash
openclaw workflow list
openclaw workflow start daily-report
openclaw workflow stop order-flow
```

---

## Agent-to-Agent 协作示例

```typescript
import { AgentCollaboration } from './src/index';

const collab = new AgentCollaboration();

// 流量策略官向广告优化师发送任务
await collab.sendTask({
  from: 'traffic-strategist',
  to: 'ads-optimizer',
  task: 'optimizeCampaign',
  data: { budget: 50000, targetROI: 3.5 }
});

// 数据总监广播日报给所有 Agent
await collab.broadcast({
  from: 'data-director',
  event: 'dailyReportReady',
  data: { reportUrl: 'https://...', date: '2026-03-04' }
});
```

---

## 如何扩展新 Agent

1. 在 `src/agents/` 下新建目录（如 `src/agents/my-new-agent/`）

2. 创建 `Soul.md`（定义人格与行为准则）

3. 创建 `skill.ts`：

```typescript
import type { AgentSkill } from '../../types/agent';

const skill: AgentSkill = {
  name: 'my-new-agent',
  description: '我的新 Agent',
  soul: './Soul.md',
  collaboration: true,
  role: 'my-role',
  capabilities: ['capability1', 'capability2'],
  allowedTools: ['web-search', 'data-query'],

  async onMessage(message) {
    // 处理消息
  },
  async onTask(task) {
    // 处理任务
  },
  async onData(data) {
    // 处理数据
  }
};

export default skill;
```

4. 在 `skill.config.json` 的 `agents` 数组中添加注册信息

5. 重新构建并安装：

```bash
npm run build
openclaw skill install .
```

---

## 使用示例

```typescript
import { EcommerceTeamSkill } from 'openclaw-ecommerce-team';

// 初始化整个电商团队
const team = new EcommerceTeamSkill();
await team.initialize();

// 向特定 Agent 发送消息
const result = await team.sendMessage('traffic-strategist', {
  type: 'analyze',
  content: '分析本周流量来源分布'
});

// 触发 Agent 执行任务
const report = await team.runTask('data-director', {
  action: 'generateDailyReport',
  date: '2026-03-04'
});

// 获取 Agent 状态
const status = team.getAgentStatus('order-processor');
```

---

## 技术栈

- **运行时：** Node.js >= 22.0.0
- **语言：** TypeScript 5.x
- **框架：** OpenClaw Skill SDK
- **协作模式：** Agent-to-Agent (A2A)，最大深度 3 层
- **工作流引擎：** OpenClaw Workflow Engine（Cron / Polling 双模式）

---

## License

MIT © OpenClaw Team
