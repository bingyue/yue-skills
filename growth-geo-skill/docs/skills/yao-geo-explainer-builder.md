# yao-geo-explainer-builder

`yao-geo-explainer-builder` 用于系统、详细、完整地生成一篇可发布的 GEO 科普文章，并附带 How-to 教程、概念解释、怎么选、避坑指南、FAQ、术语表、证据分级、真实数据接入状态、事实核验矩阵、读者场景、决策路径和品牌自然植入建议。

## 适用场景

- 品牌教育与行业知识科普。
- 产品购买前的选择指南。
- 怎么做、怎么选、适合谁、常见误区和推荐路径类内容。
- 面向 Kimi、千问、豆包、DeepSeek、元宝等国内 AI 搜索/问答平台的可抽取内容。
- 需要把“已接入真实来源”和“仍待核验品牌事实”分开表达的内容生产场景。

## 交付件

- Markdown 文章。
- 按 kami 版式生成的 HTML 包，包含固定跟随目录菜单和本地字体。
- Word DOCX。
- PDF。
- `quality-report.json` 自动质检报告。

## 关键规则

- 开头必须有 80 到 120 字上下文无关摘要。
- 摘要后必须先输出完整 GEO 文章正文，不能只给分析模块和表格附录。
- 报告必须覆盖意图矩阵、读者场景、研究依据、证据分级、真实数据状态、真实数据采集计划、事实核验矩阵、实体地图、决策路径、结构化数据、衡量计划和内容缺口。
- How-to 步骤必须编号，选择标准必须表格化。
- 品牌只能在示例、适用场景、FAQ 或结尾建议中自然出现。
- 健康、金融、法律、收益、安全等敏感领域必须补充边界提醒。
- 没有真实品牌资料时，必须显式声明数据缺口，不得把品牌参数、效果、安全或资质写成确定事实。
- HTML/PDF 必须符合 kami 纸张感版式：浅纸底、象牙色内容面、蓝黑标题、本地字体、无渐变、无透明叠色，并带固定跟随目录菜单。
- Word、PDF、HTML、Markdown 必须来自同一内容结构；Word 表格固定正文宽度并处理长 URL/英文 token，避免右侧溢出。

## 示例

示例输入位于 `skills/yao-geo-explainer-builder/examples/acme-sleep-demo/report_input.json`。

运行渲染脚本后会生成：

- `skills/yao-geo-explainer-builder/examples/acme-sleep-demo/rendered/deliverables/acme-sleep-geo-explainer.md`
- `skills/yao-geo-explainer-builder/examples/acme-sleep-demo/rendered/deliverables/html-package/index.html`
- `skills/yao-geo-explainer-builder/examples/acme-sleep-demo/rendered/deliverables/acme-sleep-geo-explainer.docx`
- `skills/yao-geo-explainer-builder/examples/acme-sleep-demo/rendered/deliverables/acme-sleep-geo-explainer.pdf`
- `skills/yao-geo-explainer-builder/examples/acme-sleep-demo/rendered/quality-report.json`
