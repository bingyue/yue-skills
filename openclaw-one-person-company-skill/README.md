# openclaw-one-person-company-skill

> **ClawLab 数字员工团队** — 18 人 AI 公司 Skill，一键部署完整的 AI 协作体系  
> 总办 · 产品增长中心 · 技术平台中心 · 营销增长中心

---

## 目录

- [简介](#简介)
- [项目结构](#项目结构)
- [快速安装](#快速安装)
- [组织架构](#组织架构)
- [18 位数字员工](#18-位数字员工)
- [Agent 通信拓扑](#agent-通信拓扑)
- [Soul 文件说明](#soul-文件说明)
- [安装后配置变化](#安装后配置变化)
- [从 v1.0.0 升级](#从-v100-升级)
- [兼容性](#兼容性)
- [故障排除](#故障排除)
- [版本历史](#版本历史)

---

## 简介

这是一个可安装的 [OpenClaw](https://github.com/openclaw) Skill 插件。  
安装后，你将拥有 **18 个各司其职的 AI Agent**，组成 **ClawLab 数字员工团队**，通过 agentToAgent 通信协议协作运转，帮助你以一人之力驱动一家完整的 AI 公司。

**核心理念：一人操盘，十八人出力。**

> 你只需告诉 CEO 你的目标，剩下的由 18 位数字员工协作完成。

---

## 项目结构

```
openclaw-one-person-company-skill/
│
├── skill.json              # Skill 元数据与依赖声明（v2.0.0）
├── agents.json             # 18 个 Agent 完整定义
├── install.sh              # 一键安装脚本（含 v1.0.0 自动迁移）
├── uninstall.sh            # 一键卸载脚本
│
├── souls/                  # 18 个 Agent Soul 文件（角色灵魂）
│   ├── ceo.md
│   ├── product_lead.md
│   ├── user_researcher.md
│   ├── data_analyst.md
│   ├── feature_planner.md
│   ├── ux_optimizer.md
│   ├── tech_lead.md
│   ├── architect.md
│   ├── backend_dev.md
│   ├── frontend_dev.md
│   ├── qa_engineer.md
│   ├── devops_engineer.md
│   ├── growth_lead.md
│   ├── content_planner.md
│   ├── seo_specialist.md
│   ├── ads_optimizer.md
│   ├── user_operator.md
│   └── crm_analyst.md
│
├── 数字员工使用说明.md       # ClawLab 团队完整使用手册
└── README.md               # 本文档
```

---

## 快速安装

### 前置条件

- macOS / Linux（bash / zsh）
- [`jq`](https://stedolan.github.io/jq/)（未安装时 `install.sh` 会自动安装）
- 已有 OpenClaw 环境（或脚本将自动创建 `openclaw.json`）

### 安装步骤

```bash
# 1. 进入 Skill 目录
cd openclaw-one-person-company-skill

# 2. 赋予脚本执行权限
chmod +x install.sh uninstall.sh

# 3. 执行安装
./install.sh
```

安装过程共 10 步，全程自动完成：

```
Step 1  — 检查 jq 依赖（缺失时自动安装）
Step 2  — 自动检测 OpenClaw 根目录
Step 3  — 检查 / 创建 openclaw.json
Step 4  — 清理旧版 v1.0.0 Agent（自动迁移）
Step 5  — 安装 18 个 Soul 文件
Step 6  — 合并 18 个 Agent 到 openclaw.json
Step 7  — 启用 agentToAgent 通信
Step 8  — 设置 maxRecursion = 3
Step 9  — 启用 Memory 系统
Step 10 — 注册 Skill 并输出验证报告
```

### 指定安装目录（可选）

```bash
OPENCLAW_ROOT="/path/to/your/openclaw" ./install.sh
```

### 安装到 claude/skills/ 或 openclaw/skills/

```bash
cp -r openclaw-one-person-company-skill ~/claude/skills/
cd ~/claude/skills/openclaw-one-person-company-skill
./install.sh
```

### 卸载

```bash
./uninstall.sh

# 跳过确认直接卸载
FORCE_UNINSTALL=true ./uninstall.sh
```

---

## 组织架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                           ClawLab 总办                               │
│                      CEO（战略决策 · 最终裁决）                        │
└────────────────┬───────────────────┬────────────────────────────────┘
                 │                   │                      │
                 ▼                   ▼                      ▼
┌────────────────────┐  ┌──────────────────────┐  ┌────────────────────┐
│   产品增长中心      │  │    技术平台中心        │  │   营销增长中心      │
│   product_lead     │  │    tech_lead          │  │   growth_lead      │
│                    │  │                       │  │                    │
│  user_researcher   │  │  architect            │  │  content_planner   │
│  data_analyst      │  │  backend_dev          │  │  seo_specialist    │
│  feature_planner   │  │  frontend_dev         │  │  ads_optimizer     │
│  ux_optimizer      │  │  qa_engineer          │  │  user_operator     │
│                    │  │  devops_engineer      │  │  crm_analyst       │
│  (1负责人 + 4执行) │  │  (1负责人 + 5执行)    │  │  (1负责人 + 5执行) │
└────────────────────┘  └──────────────────────┘  └────────────────────┘
         5 人                      6 人                      6 人

                    CEO(1) + 产品(5) + 技术(6) + 增长(6) = 18 人
```

**汇报链：** 执行角色 → 部门负责人 → CEO  
**跨部门：** 三大中心负责人之间可直接通信

---

## 18 位数字员工

### 🏢 总办

| ID | 名称 | 职责 | KPI | 核心权限 |
|----|------|------|-----|---------|
| `ceo` | CEO | 战略决策、资源分配、最终裁决 | 公司整体增长与盈利 | broadcast, approve, delegate |

### 🎯 产品增长中心

| ID | 名称 | 职责 | KPI |
|----|------|------|-----|
| `product_lead` | 产品负责人 | 产品方向决策、Roadmap 管理 | 留存率 |
| `user_researcher` | 用户研究官 | 用户洞察、需求挖掘、用户画像 | 需求准确率 |
| `data_analyst` | 数据分析师 | 数据埋点、指标体系、分析报告 | 决策支持效率 |
| `feature_planner` | 功能策划官 | PRD 撰写、功能优先级排序 | 功能转化率 |
| `ux_optimizer` | 体验优化官 | 交互设计、体验优化、A/B 测试 | 核心功能使用率 |

### ⚙️ 技术平台中心

| ID | 名称 | 职责 | KPI |
|----|------|------|-----|
| `tech_lead` | 技术负责人 | 技术战略、架构决策、团队管理 | 系统稳定性 |
| `architect` | 系统架构师 | 架构设计、技术选型、ADR 记录 | 可扩展性 |
| `backend_dev` | 后端工程师 | 服务开发、API 实现、性能优化 | 性能与稳定 |
| `frontend_dev` | 前端工程师 | 页面开发、交互实现、Core Web Vitals | 加载速度 |
| `qa_engineer` | QA 测试官 | 测试策略、质量门禁、自动化测试 | 缺陷率 |
| `devops_engineer` | DevOps 运维官 | CI/CD、监控告警、系统稳定性 | 在线率 |

### 📈 营销增长中心

| ID | 名称 | 职责 | KPI |
|----|------|------|-----|
| `growth_lead` | 增长负责人 | 增长战略、MAU 目标、AARRR 体系 | MAU |
| `content_planner` | 内容策划官 | 内容策略、文案创作、内容分发 | 内容转化率 |
| `seo_specialist` | SEO 优化官 | 关键词策略、技术 SEO、外链建设 | 自然流量 |
| `ads_optimizer` | 投放优化师 | 付费广告、创意优化、ROI 管理 | ROI |
| `user_operator` | 用户运营官 | 用户活跃、社群运营、留存策略 | 留存提升 |
| `crm_analyst` | CRM 数据官 | 用户分层、生命周期管理、复购设计 | 复购率 |

---

## Agent 通信拓扑

```
                        ┌─────────────────┐
                        │       CEO       │  priority: 1
                        │  (全局广播节点)  │  可调用全部 17 个 Agent
                        └────┬──────┬──┬──┘
                             │      │  │
              ┌──────────────┘      │  └──────────────┐
              ▼                     ▼                  ▼
  ┌───────────────────┐  ┌──────────────────┐  ┌─────────────────┐
  │   product_lead    │  │   tech_lead      │  │  growth_lead    │
  │   priority: 2     │◄─┤   priority: 2   ├──►│  priority: 2   │
  └────┬──┬──┬──┬─────┘  └──┬──┬──┬──┬──┬─┘  └──┬──┬──┬──┬────┘
       │  │  │  │            │  │  │  │  │        │  │  │  │
  ┌────▼┐┌▼┐┌▼┐┌▼────┐  ┌───▼┐┌▼┐┌▼┐┌▼┐┌▼─┐  ┌──▼┐┌▼┐┌▼┐┌▼───┐
  │user_││da││fp││ux_ │  │arc││be││fe││qa││de│  │cp_││se││ad││uo_│
  │res_ ││ta││_p││opt │  │hi_││nd││nd││_e││vo│  │pl_││o_││s_││pe_│
  │arch ││na││la││imi │  │te_││ev││_d││ng││ps│  │an_││sp││op││rat│
  │     ││ly││nn││zer │  │ct ││   ││ev││in││_e│  │ne_││ec││ti││or │
  └─────┘└──┘└──┘└────┘  └───┘└──┘└──┘└──┘└──┘  └───┘└──┘└──┘└───┘
  priority: 3              priority: 3              priority: 3
```

**通信规则：**
- CEO（priority 1）可主动调用全部 17 个 Agent
- 三大负责人（priority 2）可互通 + 管理本部门 + 上报 CEO
- 执行角色（priority 3）可上报负责人 + 跨部门协作（按权限矩阵）
- 最大递归深度：**3 层**（CEO → 负责人 → 执行角色）
- 所有通信记录到 communication log

---

## Soul 文件说明

每个 Soul.md 是一个 Agent 的「角色灵魂」，定义了该 Agent 的完整行为规范：

| 章节 | 内容 |
|------|------|
| **角色定义** | 身份定位、核心理念、KPI 说明 |
| **核心职责** | 具体负责哪些工作（4 大类细分） |
| **协作规则** | 与哪些 Agent 协作、如何协作、SLA 约定 |
| **输出格式** | 标准化输出模板，保证结构一致性 |
| **禁止行为** | 明确的行为红线（6-8 条） |

Soul 文件路径在安装时会自动更新为绝对路径写入 `openclaw.json`。

---

## 安装后配置变化

`install.sh` 执行完成后，`openclaw.json` 将自动更新为：

```json
{
  "version": "1.0.0",
  "config": {
    "agentToAgent": {
      "enabled": true,
      "allowCrossAgent": true,
      "logCommunication": true
    },
    "maxRecursion": 3,
    "memory": {
      "enabled": true
    }
  },
  "agents": [
    { "id": "ceo",              "center": "总办",       "kpi": "公司整体增长与盈利" },
    { "id": "product_lead",     "center": "产品增长中心", "kpi": "留存率" },
    { "id": "user_researcher",  "center": "产品增长中心", "kpi": "需求准确率" },
    { "id": "data_analyst",     "center": "产品增长中心", "kpi": "决策支持效率" },
    { "id": "feature_planner",  "center": "产品增长中心", "kpi": "功能转化率" },
    { "id": "ux_optimizer",     "center": "产品增长中心", "kpi": "核心功能使用率" },
    { "id": "tech_lead",        "center": "技术平台中心", "kpi": "系统稳定性" },
    { "id": "architect",        "center": "技术平台中心", "kpi": "可扩展性" },
    { "id": "backend_dev",      "center": "技术平台中心", "kpi": "性能与稳定" },
    { "id": "frontend_dev",     "center": "技术平台中心", "kpi": "加载速度" },
    { "id": "qa_engineer",      "center": "技术平台中心", "kpi": "缺陷率" },
    { "id": "devops_engineer",  "center": "技术平台中心", "kpi": "在线率" },
    { "id": "growth_lead",      "center": "营销增长中心", "kpi": "MAU" },
    { "id": "content_planner",  "center": "营销增长中心", "kpi": "内容转化率" },
    { "id": "seo_specialist",   "center": "营销增长中心", "kpi": "自然流量" },
    { "id": "ads_optimizer",    "center": "营销增长中心", "kpi": "ROI" },
    { "id": "user_operator",    "center": "营销增长中心", "kpi": "留存提升" },
    { "id": "crm_analyst",      "center": "营销增长中心", "kpi": "复购率" }
  ],
  "skills": [
    {
      "name": "openclaw-one-person-company",
      "version": "2.0.0",
      "agentCount": 18
    }
  ]
}
```

---

## 从 v1.0.0 升级

v1.0.0 包含 4 个 Agent（`ceo` / `product` / `tech` / `growth`），  
v2.0.0 扩展为 18 个 Agent，并重构了旧版的 `product` / `tech` / `growth` 三个 Agent ID。

**升级方法（一条命令，全自动）：**

```bash
./install.sh
```

`install.sh` 内置自动迁移逻辑：
- Step 4 会自动检测并清理旧版 4 个 Agent
- 安装前自动备份 `openclaw.json`（路径显示在安装日志中）
- 不影响 `openclaw.json` 中的其他已有配置

---

## 兼容性

| 条件 | 支持情况 |
|------|---------|
| macOS | ✅ |
| Linux（Ubuntu / Debian / CentOS） | ✅ |
| 已有 `openclaw.json` | ✅ 自动合并，不破坏现有配置 |
| `claude/skills/` 目录 | ✅ |
| `openclaw/skills/` 目录 | ✅ |
| 自定义安装路径 | ✅ `OPENCLAW_ROOT` 环境变量 |
| 从 v1.0.0 升级 | ✅ 自动迁移旧版 Agent |
| Windows（WSL） | ✅ 在 WSL2 下测试通过 |

---

## 故障排除

**找不到 openclaw.json**

```bash
OPENCLAW_ROOT="$HOME/.openclaw" ./install.sh
```

**jq 安装失败**

```bash
# macOS
brew install jq

# Ubuntu / Debian
sudo apt-get install -y jq

# CentOS / RHEL
sudo yum install -y jq
```

**权限不足**

```bash
chmod +x install.sh uninstall.sh
```

**需要恢复安装前的配置**

```bash
# 备份路径在安装日志末尾会打印
cp openclaw.json.backup.YYYYMMDD_HHMMSS openclaw.json
```

**安装后 Agent 数量不对**

```bash
# 检查当前已注册 Agent 数
jq '.agents | length' openclaw.json

# 检查各部门 Agent 分布
jq -r '.agents[] | "\(.center) — \(.id)"' openclaw.json
```

**重新安装（幂等，可反复执行）**

```bash
# install.sh 是幂等的，重复执行不会产生重复 Agent
./install.sh
```

---

## 文档索引

| 文档 | 说明 |
|------|------|
| `README.md` | 项目说明、安装指南（本文档） |
| `数字员工使用说明.md` | ClawLab 团队理念、工作流示例、KPI 体系、使用最佳实践 |
| `agents.json` | 18 个 Agent 的技术定义（通信权限、memory、config） |
| `souls/*.md` | 各 Agent 的角色灵魂文件 |

---

## 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| **2.0.0** | 2026-03-04 | 扩展为 18 人团队，新增三大中心架构，完善 agentToAgent 通信矩阵，新增数字员工使用说明 |
| 1.0.0 | 2026-03-04 | 初始版本，包含 CEO / Product / Tech / Growth 四个 Agent |

---

## License

MIT

---

> **ClawLab 数字员工团队** · Powered by OpenClaw Skill · v2.0.0  
> 详细使用手册请参阅 [数字员工使用说明.md](./数字员工使用说明.md)
