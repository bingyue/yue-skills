# ABSA（方面级情感分析）参考文档

## 任务定义

ABSA 的目标是将一条评论拆解为多个"方面-情感"对，结构为：

```
[方面] × [情感极性] × [置信度] × [证据片段]
```

情感极性枚举值：
- `positive`：正面，用户对该方面满意
- `negative`：负面，用户对该方面不满意
- `neutral`：中性，用户提到了但无明确情感
- `mixed`：混合，同一方面内有正有负（如"降噪很好但跑步时不安全"）

---

## 输出格式规范

```json
{
  "review_id": "r-0001",
  "absa_results": [
    {
      "aspect": "音质",
      "aspect_category": "product_quality",
      "sentiment": "positive",
      "confidence": 0.94,
      "evidence": "声音很清晰",
      "evidence_span": [8, 14],
      "severity": null
    },
    {
      "aspect": "舒适度",
      "aspect_category": "product_quality",
      "sentiment": "negative",
      "confidence": 0.89,
      "evidence": "戴久了耳朵有点疼",
      "evidence_span": [23, 32],
      "severity": "medium"
    }
  ],
  "rating_sentiment_alignment": "misaligned",
  "alignment_note": "用户给出5星，但舒适度维度存在明确负面反馈"
}
```

### 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `aspect` | string | 方面名称，使用 aspect-taxonomy.md 中定义的标准名称 |
| `aspect_category` | string | 方面类别：`product_quality` / `service` / `price` |
| `sentiment` | enum | positive / negative / neutral / mixed |
| `confidence` | float | 0-1，模型对该判断的置信度 |
| `evidence` | string | 原文中支撑该判断的片段，**必填** |
| `evidence_span` | [int, int] | 证据在原文中的起止字符位置（可选） |
| `severity` | enum | 仅负面/混合时填写：high / medium / low / null |

### severity 分级标准

- **high**：功能性问题、安全问题、质量严重缺陷（如"左耳三周就没声音了"）
- **medium**：明显影响体验但不致命（如"领口有点扎"、"续航比宣传短"）
- **low**：轻微不便、个人偏好差异（如"颜色稍微偏暗一点"）

---

## rating 与方面情感对齐判断

```
rating_sentiment_alignment 取值逻辑：

- aligned：rating 与整体方面情感方向一致
- misaligned：rating 高但存在明确负面方面，或 rating 低但存在明确正面方面
- neutral：评论情感不明显，或方面数量太少难以判断
```

**重要**：`misaligned` 的评论是最有价值的分析对象，应在批量分析时单独统计。

---

## 完整示例集

### 示例 1：5 星好评中的隐藏痛点

**评论（rating=5）：**
> "整体很满意，声音很清晰，降噪也不错。唯一就是戴久了耳朵有点疼。"

```json
{
  "review_id": "r-0001",
  "rating": 5,
  "absa_results": [
    {
      "aspect": "音质",
      "aspect_category": "product_quality",
      "sentiment": "positive",
      "confidence": 0.94,
      "evidence": "声音很清晰",
      "severity": null
    },
    {
      "aspect": "降噪效果",
      "aspect_category": "product_quality",
      "sentiment": "positive",
      "confidence": 0.91,
      "evidence": "降噪也不错",
      "severity": null
    },
    {
      "aspect": "舒适度",
      "aspect_category": "product_quality",
      "sentiment": "negative",
      "confidence": 0.89,
      "evidence": "戴久了耳朵有点疼",
      "severity": "medium"
    }
  ],
  "rating_sentiment_alignment": "misaligned",
  "alignment_note": "5星评论中存在舒适度的明确负面反馈"
}
```

---

### 示例 2：1 星差评中的产品认可

**评论（rating=1）：**
> "声音其实挺好，但左耳用了两天就没电了，退换货还特别麻烦。"

```json
{
  "review_id": "r-0002",
  "rating": 1,
  "absa_results": [
    {
      "aspect": "音质",
      "aspect_category": "product_quality",
      "sentiment": "positive",
      "confidence": 0.88,
      "evidence": "声音其实挺好",
      "severity": null
    },
    {
      "aspect": "续航/电池",
      "aspect_category": "product_quality",
      "sentiment": "negative",
      "confidence": 0.97,
      "evidence": "左耳用了两天就没电了",
      "severity": "high"
    },
    {
      "aspect": "售后/退换货",
      "aspect_category": "service",
      "sentiment": "negative",
      "confidence": 0.95,
      "evidence": "退换货还特别麻烦",
      "severity": "medium"
    }
  ],
  "rating_sentiment_alignment": "misaligned",
  "alignment_note": "1星评论中产品音质被认可，差评主要来源于电池和售后，而非产品核心体验"
}
```

---

### 示例 3：物流导致的差评（产品无问题）

**评论（rating=2）：**
> "外观很好看，做工也不错，但物流太慢了，等了八天，急用没赶上。"

```json
{
  "review_id": "r-0003",
  "rating": 2,
  "absa_results": [
    {
      "aspect": "外观/颜值",
      "aspect_category": "product_quality",
      "sentiment": "positive",
      "confidence": 0.92,
      "evidence": "外观很好看",
      "severity": null
    },
    {
      "aspect": "做工/材质",
      "aspect_category": "product_quality",
      "sentiment": "positive",
      "confidence": 0.90,
      "evidence": "做工也不错",
      "severity": null
    },
    {
      "aspect": "物流速度",
      "aspect_category": "service",
      "sentiment": "negative",
      "confidence": 0.98,
      "evidence": "物流太慢了，等了八天",
      "severity": "high"
    }
  ],
  "rating_sentiment_alignment": "misaligned",
  "alignment_note": "2星差评完全来源于物流问题，产品本身获得正面评价——归因应指向履约团队而非品控"
}
```

---

### 示例 4：混合情感评论

**评论（rating=3）：**
> "耳机音质很惊喜，但佩戴不稳，走路容易掉。降噪效果一般，不如我上一款，不过价格便宜很多，整体还是值得的。"

```json
{
  "review_id": "r-0004",
  "rating": 3,
  "absa_results": [
    {
      "aspect": "音质",
      "aspect_category": "product_quality",
      "sentiment": "positive",
      "confidence": 0.93,
      "evidence": "音质很惊喜",
      "severity": null
    },
    {
      "aspect": "佩戴稳定性",
      "aspect_category": "product_quality",
      "sentiment": "negative",
      "confidence": 0.91,
      "evidence": "佩戴不稳，走路容易掉",
      "severity": "medium"
    },
    {
      "aspect": "降噪效果",
      "aspect_category": "product_quality",
      "sentiment": "negative",
      "confidence": 0.85,
      "evidence": "降噪效果一般，不如我上一款",
      "severity": "low"
    },
    {
      "aspect": "价格/性价比",
      "aspect_category": "price",
      "sentiment": "positive",
      "confidence": 0.90,
      "evidence": "价格便宜很多，整体还是值得的",
      "severity": null
    }
  ],
  "rating_sentiment_alignment": "aligned"
}
```

---

## 隐含方面（Implicit Aspect）处理

有些评论中，用户的情感指向某个方面，但没有直接说出方面名称。这类隐含方面也需要识别：

| 原文片段 | 隐含方面 | 识别逻辑 |
|---------|--------|--------|
| "这个大小刚好放书包里" | 便携性/尺寸 | "放书包"暗含便携场景，情感正面 |
| "我家狗子也能用" | 安全性/适用人群 | 暗含对材质安全的认可 |
| "天气热的时候戴很舒服" | 透气性/季节适用性 | 场景触发了对透气性的评价 |
| "送给朋友特别有面子" | 外观/品牌感知 | 送礼场景暗含颜值认可 |
| "充电盒放进去卡卡的响" | 充电盒做工 | 声音描述暗含做工满意 |

处理隐含方面时，在 `absa_results` 中额外加一个字段标注：

```json
{
  "aspect": "便携性",
  "sentiment": "positive",
  "evidence": "大小刚好放书包里",
  "implicit": true,
  "implicit_reason": "放书包的描述隐含了对便携尺寸的正面认可"
}
```

---

## 批量评论聚合分析模板

当分析多条评论时，输出方面情感矩阵：

```json
{
  "product_id": "SKU-XXX",
  "analysis_period": "2024-01 至 2024-06",
  "total_reviews_analyzed": 1200,
  "aspect_sentiment_matrix": {
    "音质": {
      "positive": 876,
      "negative": 45,
      "neutral": 23,
      "mixed": 12,
      "net_score": 831,
      "mention_rate": 0.80
    },
    "续航/电池": {
      "positive": 234,
      "negative": 456,
      "neutral": 89,
      "mixed": 34,
      "net_score": -222,
      "mention_rate": 0.68
    }
  },
  "top_issues": [
    {
      "aspect": "续航/电池",
      "negative_count": 456,
      "net_score": -222,
      "severity_distribution": {"high": 123, "medium": 267, "low": 66},
      "sample_evidence": ["用了两天就没电了", "续航比宣传差太多", "充满电撑不过12小时"]
    }
  ],
  "rating_misalignment_stats": {
    "total_misaligned": 189,
    "misalignment_rate": 0.158,
    "high_rating_with_negative": 134,
    "low_rating_with_positive": 55
  }
}
```