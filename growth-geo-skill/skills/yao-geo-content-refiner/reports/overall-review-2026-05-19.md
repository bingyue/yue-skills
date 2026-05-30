# 整体 Review 记录

日期：2026-05-19

## Review 范围

- Skill 路由与边界：`SKILL.md`
- Agent 接口：`agents/interface.yaml`
- 方法与质量门：`references/`
- 示例输入与四格式输出：`examples/hubspot-cn-demo/`
- 渲染脚本：`scripts/render_content_refiner_bundle.py`
- 仓库索引：`README.md`、`registry/skills.json`

## 发现并修复的问题

| 问题 | 影响 | 修复 |
|---|---|---|
| README 仍保留已不存在的 `expected-output` 岭序示例链接。 | 导航断链，用户无法打开示例。 | 改为当前真实存在的 HubSpot 国内 AI 平台测试示例。 |
| Skill 包缺少内容方法、证据规则、平台适配、研究框架等参考文件。 | `SKILL.md` 太瘦，执行标准不够可复用。 | 新增 `content-refinement-method.md`、`evidence-and-fact-rules.md`、`platform-adaptation.md`、`research-backed-framework.md`。 |
| `evals/expected_artifacts.json` 未覆盖新增参考文件、接口和 rubric。 | 结构校验无法发现参考资料缺失。 | 扩展 required files，并新增 `quality_cases.json` 与 `rubric.md`。 |
| 渲染脚本的质量报告只检查文件和模块，未自动检查 DOCX 表格宽度。 | Word 右溢出可能复发但质量报告仍显示通过。 | 新增 `inspect_docx_layout()`，把页面可用宽度、最大表格宽度、右侧安全余量和溢出表格写入 `quality-report.json`。 |
| OOXML 辅助函数里存在空元素 truth-testing 写法。 | 未来 Python/lxml 行为变化可能产生警告或不稳定。 | 改成显式 `is None` 判断。 |

## 当前验证

- `python3 scripts/validate_repository.py`：通过；仅提示 `yao-geoflow-design` 和 `yao-geoflow-template` 没有 examples 目录。
- `quality-report.json`：`pass`，`problems: []`。
- DOCX 布局检查：横向页面，可用宽度 `15308 dxa`，最大表格宽度 `15260 dxa`，最小右侧安全余量 `48 dxa`，溢出表格 0。
- PDF PNG 检查：7 页，最小右侧留白 `65 px`。

## 后续建议

- 若后续恢复岭序合成示例，需要重新生成真实四格式文件后再把链接加回 README。
- 若正式项目报告表格超过 4 列，保持 Word/PDF 事实卡逻辑，不要回退到宽表。
