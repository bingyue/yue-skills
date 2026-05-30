---
name: brand-visual-ai
description: 品牌视觉 AI 全流程套件。从品牌叙事→视觉方向→Logo 设计→字形选择→设计系统→交付物，覆盖品牌视觉建设 8 个阶段。基于 b1rdmania/claude-brand-skills 工作流，适配中文品牌场景。支持新品牌建立、品牌焕新、子品牌延伸场景。
---

# 品牌视觉 AI 套件

> 基于 [b1rdmania/claude-brand-skills](https://github.com/b1rdmania/claude-brand-skills) 工作流，中文场景适配版。

## 8 阶段工作流

### Phase 0 — 品牌叙事（Emotive Narrative）
- 用语言捕捉品牌的灵魂与情感内核
- 产出：`品牌叙事.md`（品牌故事/使命/个性）

### Phase 1 — 品牌策略（Discovery）
- 定位分析（竞品地图/差异化）
- 目标用户画像
- 品牌声音与调性定义
- 产出：`品牌策略.md`

### Phase 2 — 视觉方向（Visual Direction）
- 情绪板描述（Moodboard 关键词）
- 参考风格：极简/国潮/科技/生活/奢侈...
- 提供给图像生成工具的方向描述

### Phase 3 — Logo 开发（Mark Development）
- SVG Logo 设计（几何图形/文字图形/混合）
- 生成 6 个以上方向变体
- 结合 `image-logo-svg` 渲染展示图

### Phase 4 — 字形（Wordmark）
- 品牌英文/中文字体选择建议
- 字重/字间距/大小写规范
- 字形锁定稿

### Phase 5 — 设计系统（Design System）
- 主色/辅色/中性色体系（含 HEX/RGB）
- 字体层级规范（H1/H2/正文/注释）
- 间距/圆角/阴影基础变量
- 网页/APP/印刷 三端适配说明

### Phase 6 — DESIGN.md
- 将所有阶段成果整合进统一主文档

### Phase 7 — 交付打包（Packaging）
- 品牌资产清单（Logo SVG/PNG/各尺寸）
- 使用规范说明
- 禁用示例

## 快速启动

告诉 Agent：
1. 品牌名称和行业
2. 目标用户（年龄/性别/消费力）
3. 品牌想传达的核心感受（3 个形容词）
4. 参考品牌（国内外均可）

即可启动全流程，也可单独调用某个阶段。

## 触发关键词

"帮我做品牌设计" / "品牌 VI" / "Logo 设计" / "品牌视觉系统" / "设计规范"
