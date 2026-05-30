# Bright Data 网络研究项目

## 项目概述

本项目是一个专门用于网络数据收集和市场研究的目录，主要关注电商平台的市场分析，例如： 3D 打印机和便携式电源站。项目利用 Bright Data MCP 工具进行网络爬虫和数据分析。

## 项目结构

```
D:\new_bright_data\
├── amazon_3d_printer_research_report.md    # 3D 打印机市场研究报告
├── portable_power_station_data.json        # 便携式电源站数据
├── .mcp.json                              # MCP 服务器配置
├── .claude/                               # Claude AI 配置
│   ├── settings.local.json                # Claude 权限设置
│   └── skills/                           # Claude 技能
│       ├── ducksearch/                   # DuckDuckGo 搜索技能
│       └── research-brightdata/          # Bright Data 研究技能
└── QWEN.md                               # 项目说明文档
```

## 技术栈

- **Bright Data MCP**: 用于网络爬虫和数据提取
- **Claude AI**: 配置了专门的研究技能
- **DuckDuckGo 搜索**: 辅助网络搜索工具
- **浏览器自动化**: 用于处理 JavaScript 渲染的页面

## 配置说明

项目已配置 Claude AI 技能，支持：
- 网络搜索和发现
- 内容收集和批量处理
- 结构化数据提取
- 浏览器自动化操作
- 数据验证和质量控制

## 使用方法

1. 确保已配置有效的 Bright Data API 密钥
2. 使用 Claude AI 运行研究查询
3. 利用 `research-brightdata` 技能进行综合市场分析
4. 将新的研究数据保存为类似的 JSON 或 Markdown 格式



## 主要demo内容

### 1. 3D 打印机市场研究报告

详细的亚马逊 3D 打印机市场分析，包含：
- 市场规模和增长预测
- 畅销产品排行榜
- 品牌市场份额分析
- 技术趋势和消费者行为
- 定价策略和利润分析
- 竞争格局评估

### 2. 便携式电源站市场数据

结构化的便携式电源站市场数据，包括：
- 主要品牌产品规格对比
- 容量、输出功率、重量和价格数据
- 市场细分和趋势分析
- 主要品牌（Jackery、EcoFlow、Bluetti、Anker、Goal Zero）的竞争分析


## 研究特点

- **自动化数据收集**: 使用 MCP 工具自动收集网络数据
- **反机器人保护**: 采用防机器人措施确保数据收集稳定性
- **结构化分析**: 对收集的数据进行结构化处理和分析
- **多维度研究**: 涵盖市场规模、品牌竞争、技术趋势等多个维度

## 应用场景

- 市场趋势分析
- 竞争对手研究
- 产品定价策略
- 消费者行为分析
- 供应链研究

## 注意事项

- 请遵守网站的 robots.txt 规则
- 合理控制请求频率，避免对服务器造成压力
- 正确引用数据来源
- 不要滥用个人数据