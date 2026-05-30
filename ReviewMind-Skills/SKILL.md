---
name: review-analysis
description: 用于对电商/消费品用户评论进行结构化分析的技能。覆盖三层分析体系：(1) ABSA 方面级情感分析——识别用户在哪些维度满意/不满意；(2) NER + IE 信息抽取——定位到具体款式、颜色、部件、尺码、材质等实体的问题；(3) 人群与场景关联——回答"谁在哪里遇到了什么问题"。当用户提到：分析评论、处理用户反馈、评论挖掘、ABSA、方面情感、NER、信息抽取、差评归因、质量分析、评论洞察、用户口碑分析，或者上传了评论数据并希望从中提取信息时，必须使用此技能。即使用户只是说"帮我看看这些评论"或"这些差评是什么原因"，也应触发此技能。
---

# 评论分析技能（Review Analysis Skill）

本技能实现了一套三层递进的用户评论分析框架，从粗粒度到细粒度逐步深入，输出结构化 JSON，可直接驱动业务决策。

## 分析框架总览

```
第一层（粗）：Rating 分析         → 整体好还是差
第二层（中）：ABSA 方面情感分析   → 在哪些方面好 / 在哪些方面差
第三层（细）：NER + IE 信息抽取   → 具体哪个款式 / 部件 / 材质 / 属性值
延伸层：     人群与场景关联        → 谁在哪里遇到了这个问题
```

**何时做到哪一层：**
- 快速商品健康度评估 → 第一层 + 第二层（ABSA）即可
- 质量归因 / 供应链反馈 → 三层全做
- 用户细分 / 场景化运营 → 三层 + 延伸层（人群场景）

---

## 第一步：判断任务类型，选择分析深度

在开始分析之前，先明确：

1. **输入数据形式**：单条评论 / 批量评论列表 / 已有 rating 分布数据
2. **分析目标**：归因（找问题出在哪）/ 监控（某方面是否恶化）/ 竞品对比 / 运营洞察
3. **商品类目**：不同类目的方面体系不同，需要选择对应的 aspect taxonomy

根据目标，选择进入哪个分析模块：
- → **仅 ABSA**：读 `references/absa.md`
- → **ABSA + IE/NER**：读 `references/absa.md` 和 `references/ie-ner.md`
- → **完整三层 + 人群场景**：读全部三个 references 文件
- → **方面体系查询 / 设计**：读 `references/aspect-taxonomy.md`

---

## 第二步：执行分析

### 输入格式规范

单条评论：
```json
{
  "review_id": "string（必填）",
  "product_id": "string（选填）",
  "rating": "1-5 整数（选填，但强烈建议提供）",
  "text": "string（必填，评论正文）",
  "category": "string（选填，商品类目）",
  "source": "string（选填，平台来源）",
  "created_at": "ISO8601（选填）"
}
```

批量评论：以上述格式的 JSON 数组，或带列名的表格数据。

---

## 第三步：输出结构

完整输出包含以下字段（根据分析深度选择性输出）：

```json
{
  "review_id": "...",
  "product_id": "...",
  "rating": 4,

  // 第二层：ABSA 输出
  "absa_results": [...],
  "rating_sentiment_alignment": "aligned | misaligned | neutral",

  // 第三层：IE/NER 输出
  "entities": [...],
  "slots": [...],

  // 延伸层：人群场景输出
  "user_group": {...},
  "usage_scenarios": [...],

  // 聚合分析（批量时使用）
  "aggregation": {...}
}
```

各字段的详细定义和示例见对应 references 文件。

---

## 第四步：批量分析时的聚合输出

当处理多条评论时（>5条），除了逐条输出外，还应生成聚合视图：

```json
{
  "aggregation": {
    "total_reviews": 200,
    "aspect_sentiment_matrix": {
      "音质": {"positive": 156, "negative": 12, "neutral": 8, "net_score": 144},
      "续航": {"positive": 89, "negative": 67, "neutral": 23, "net_score": 22}
    },
    "top_negative_aspects": ["续航", "舒适度", "连接稳定性"],
    "top_positive_aspects": ["音质", "做工", "外观"],
    "rating_misalignment_count": 34,
    "high_severity_issues": [...]
  }
}
```

---

## 核心原则

- **不要在没有证据的情况下标注情感**：每个 aspect 的情感判断必须有 `evidence` 字段支撑，即原文中触发该判断的片段
- **rating ≠ 方面情感**：用户的整体打分受多种因素影响，5 星评论可能包含明确的负面方面，1 星评论可能包含对产品本身的认可
- **方面体系要与类目匹配**：不同类目的方面定义不同，优先使用 `references/aspect-taxonomy.md` 中的预定义体系
- **严重程度分级**：负面方面要标注 `severity`（high / medium / low），便于业务优先级排序
- **隐含方面也要识别**：用户有时不明说方面，如"这个大小刚好放书包里"隐含了"便携性"的正面评价

---

## References 文件导航

| 文件 | 内容 | 何时读 |
|------|------|-------|
| `references/absa.md` | ABSA 任务定义、输出格式、示例、隐含方面处理 | 做方面情感分析时 |
| `references/ie-ner.md` | NER 实体类型定义、槽位抽取格式、多类目示例 | 需要细粒度归因时 |
| `references/aspect-taxonomy.md` | 主要类目的方面体系预定义表 | 设计或选择方面体系时 |