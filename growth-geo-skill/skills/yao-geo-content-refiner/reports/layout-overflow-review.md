# Word/PDF 版式溢出检查记录

日期：2026-05-21

## 检查对象

- `examples/hubspot-cn-demo/hubspot-cn-geo-content-refiner-report.docx`
- `examples/hubspot-cn-demo/hubspot-cn-geo-content-refiner-report.pdf`

## 发现的问题

- 首次结构检查发现 Word 表格固定宽度为 `15310 dxa`，页面可用宽度为 `15308 dxa`，实际超出 2 dxa。
- 8 列“原子事实卡”和 5 列“改造前后差异报告”在 Word 中存在天然右溢出风险，即使自动换行也会造成列过窄和阅读体验差。

## 修复

- 将 Word 固定表宽降为 `15260 dxa`，保留 48 dxa 安全余量。
- Word 默认改为横向 A4，左右边距 1.35 cm。
- 超过 4 列的表格在 Word/PDF 中自动转为纵向事实卡。
- 长 URL 在 Word/PDF 中强制可换行。
- 质量报告记录 `layout_profile: fixed-width-docx-wide-table-cards-sticky-html-nav`。

## 复检结果

- Word 页面可用宽度：`15308 dxa`。
- Word 所有 63 张表格宽度：`15260 dxa`。
- Word 溢出表格数量：0。
- PDF 渲染为 15 页 PNG 后，各页右侧留白均为正，最小右侧留白约 65 px。
- HTML 报告新增 sticky 菜单栏，质量报告记录菜单锚点 16 个、正文 section 16 个。
- HTML 报告按 Kami 编辑排版细节检查：墨蓝强调、serif 标题、暖灰边框、无 `rgba()`。

## 结论

HubSpot 示例的 Word/PDF 右溢出问题仍保持修复状态。后续所有该 skill 生成的 Word/PDF 报告应沿用固定表宽、宽表转事实卡和 PDF 渲染检查逻辑；HTML 报告应保留 sticky 菜单栏和锚点完整性检查。
