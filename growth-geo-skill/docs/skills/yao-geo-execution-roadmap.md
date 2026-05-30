# yao-geo-execution-roadmap

`yao-geo-execution-roadmap` 用于把 GEO 全景诊断、机会地图和平台采样结论转成 30/60/90 天综合实施方案。

## 适用任务

- GEO 项目启动后，把诊断结果落成可执行计划。
- 给 CEO、市场负责人、增长、内容、技术和客户交付团队同步 90 天节奏。
- 覆盖 DeepSeek、豆包、千问、Kimi、元宝五个平台差异化执行动作。
- 需要默认输出 Markdown、HTML、Word、PDF 四格式报告，HTML 带固定跟随菜单栏。
- 需要报告系统、详细、完整，包含分析完整性、证据成熟度、预算优先级和治理机制。
- 需要说明真实数据能力边界、来源新鲜度和平台采样导入方式。

## 核心输出

- GEO 综合实施方案。
- 真实数据能力与采集计划：公开网页核验、用户授权数据、平台采样导入、待补证缺口。
- 分析完整性矩阵：业务目标、问题覆盖、品牌实体、页面技术、内容资产、标题体系、知识库、外部证据、平台适配、监测治理。
- 证据成熟度与事实底座：A-E 来源成熟度、证据缺口、补证动作和禁用表述。
- 六个项目包：页面技术、内容矩阵、标题体系、知识库、外部证据、监测闭环。
- 30/60/90 天路线图。
- 角色分工与验收指标表。
- 资源预算与优先级、治理节奏与决策机制。
- 风险预案和合规节点。
- 带章节锚点和固定菜单栏的 HTML 可视化报告，参考 kami 的白底编辑排版、暖白辅助面、油墨蓝强调和紧凑行距。

## 示例

- Lingxu 基准样例：`skills/yao-geo-execution-roadmap/examples/lingxu-demo/`
- HubSpot 中文测试样例：`skills/yao-geo-execution-roadmap/examples/hubspot-cn-demo/`

## 生成方式

```bash
python3 skills/yao-geo-execution-roadmap/scripts/render_yao_geo_execution_roadmap.py \
  --input skills/yao-geo-execution-roadmap/examples/hubspot-cn-demo/report_input.json \
  --output-dir skills/yao-geo-execution-roadmap/examples/hubspot-cn-demo
```
