# Reference Scan 2026-05-21

## 当前 Skill 锚点

`yao-geo-content-refiner` 的核心任务是把已有文章改造成国内 AI 平台可引用、可核验、可扫描、可发布的 GEO 内容，并交付 Markdown、HTML、Word、PDF 四格式报告。

## 扫描重点

- 分析是否足够系统、详细、完整。
- 报告是否覆盖证据、语义、平台、发布和自检。
- HTML 可视化报告是否需要更强的导航能力。

## 外部参考对象

| 参考对象 | 借用模式 | 不借用内容 |
|---|---|---|
| GEO: Generative Engine Optimization (`https://arxiv.org/abs/2311.09735`) | 生成式引擎可见性、领域差异、内容引用结果评估。 | 不把论文实验提升数字写成客户承诺。 |
| Retrieval-Augmented Generation (`https://arxiv.org/abs/2005.11401`) | 外部知识、检索结构、来源可更新、事实可归因。 | 不把 RAG 等同于“加链接即可被引用”。 |
| ALCE citation evaluation (`https://arxiv.org/abs/2305.14627`) | 把流畅度、正确性、引用质量分开检查。 | 不引入复杂自动评分器作为本 skill 必需依赖。 |
| Lost in the Middle (`https://arxiv.org/abs/2307.03172`) | 关键结论、证据和边界前置，降低长文中段遗失。 | 不把所有内容压缩到首屏，仍保留完整报告结构。 |
| FActScore / Self-RAG (`https://arxiv.org/abs/2305.14251`, `https://arxiv.org/abs/2310.11511`) | 原子事实卡、自 Review、检索必要性和证据支持检查。 | 不要求每次运行外部模型评分。 |
| Google Search Quality Rater Guidelines (`https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf`) | E-E-A-T、主内容质量、声誉、YMYL 风险和用户需求满足。 | 不把搜索质量指南误作传统 SEO 排名规则。 |

## 本地适配约束

- 保持 `SKILL.md` 精简，细规则放入 `references/`。
- 继续使用现有四格式渲染脚本，不引入新服务依赖。
- Word/PDF 防右溢出优先级高于表格横向完整呈现。
- HTML 必须白底，并新增 sticky 菜单栏。

## 借用计划

1. 增加“分析完整性总览”，把分析面显式化。
2. 增加“语义与实体地图”，补实体、别名、术语和关系。
3. 增加“平台适配矩阵”，把国内 AI 平台和微信生态拆成不同阅读/引用场景。
4. 将旧版证据列表升级为“证据强度与缺口”，增加来源类型和证据强度字段。
5. 增加“发布与追踪建议”，让报告从内容改写延伸到 CMS/公众号/知识库落地。
6. HTML 报告增加 sticky 菜单栏和锚点质量检查。
