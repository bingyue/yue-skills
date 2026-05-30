# NER + IE（实体识别与信息抽取）参考文档

## 为什么 ABSA 不够用

ABSA 识别的"方面"是抽象概念（舒适度、外观、尺码），它能告诉你**在哪里有问题**，但无法回答：

- 用户说"图案不好看"，是**哪个图案/哪个颜色**？
- 用户说"尺寸偏小"，具体是**哪个尺码**偏小？
- 用户说"耳朵疼"，是**哪个部件**（耳塞/头梁）导致的？
- 用户说"降噪有问题"，是**主动降噪**不行，还是**被动隔音**不足？

这类细粒度信息，需要 NER + IE 来抽取。

---

## NER 实体类型定义

以下是商品评论场景下的标准实体类型：

| 实体类型 | 代码 | 说明 | 示例 |
|---------|------|------|------|
| 商品款式/型号 | `product_variant` | 具体款式名、型号 | "碎花蓝"、"Pro版"、"大号款" |
| 颜色/配色 | `color` | 具体颜色描述 | "米白"、"复古绿"、"深蓝色" |
| 尺码/规格 | `size_spec` | 尺码或规格值 | "XL码"、"12粒装"、"500ml" |
| 产品部件 | `part` | 产品的具体组成部件 | "左耳"、"充电盒"、"耳塞" |
| 组成组件 | `component` | 可拆卸/可更换的零件 | "硅胶耳塞"、"头梁"、"耳垫" |
| 材质/材料 | `material` | 具体材质描述 | "硅胶"、"金属外壳"、"尼龙" |
| 连接设备 | `device` | 连接/使用的设备 | "iPhone"、"Mac"、"安卓手机" |
| 口味/风味 | `flavor` | 食品/饮品口味 | "奶油味"、"抹茶口味"、"原味" |
| 使用人群 | `user_group` | 明确提到的使用人群 | "老人"、"婴儿"、"跑步人群" |
| 使用场景 | `scenario` | 具体使用场景 | "通勤"、"跑步"、"送礼" |
| 时间/季节 | `time_condition` | 时间相关条件 | "夏天"、"晚上"、"洗后" |
| 数量 | `quantity` | 商品数量/规格量 | "12粒"、"500g" |

---

## 槽位（Slot）抽取格式

槽位是 IE 的核心输出，表达"实体-属性-值-极性"四元组：

```json
{
  "slot_id": "s1",
  "aspect": "对应的 ABSA 方面",
  "entity": "涉及的具体实体（可为null）",
  "entity_type": "实体类型代码",
  "attribute": "被评价的属性",
  "value": "属性值或问题描述",
  "polarity": "positive | negative | neutral",
  "severity": "high | medium | low | null",
  "condition": "触发条件（可选，如'洗后'、'大量出汗后'）",
  "recommendation": "用户建议（可选）",
  "evidence": "原文证据片段（必填）"
}
```

---

## 完整示例集（多类目）

### 示例 1：服装类 —— 颜色/款式/部件/尺码

**评论（rating=3）：**
> "花色总体很好看，但'碎花蓝'这款颜色偏暗，实物跟图片差距大。面料摸起来挺舒服的，就是领口有点扎，特别是刚洗完之后更明显。尺码偏大，建议身材娇小的妹妹买小一码。"

```json
{
  "review_id": "r-0102",
  "entities": [
    {"entity_id": "e1", "type": "product_variant", "text": "碎花蓝"},
    {"entity_id": "e2", "type": "part", "text": "领口"},
    {"entity_id": "e3", "type": "user_group", "text": "身材娇小"}
  ],
  "slots": [
    {
      "slot_id": "s1",
      "aspect": "外观/图案",
      "entity": "碎花蓝",
      "entity_id": "e1",
      "entity_type": "product_variant",
      "attribute": "颜色",
      "value": "偏暗",
      "comparison": "与商品图片存在色差",
      "polarity": "negative",
      "severity": "medium",
      "evidence": "'碎花蓝'这款颜色偏暗，实物跟图片差距大"
    },
    {
      "slot_id": "s2",
      "aspect": "材质/面料",
      "entity": null,
      "attribute": "触感",
      "value": "舒服",
      "polarity": "positive",
      "severity": null,
      "evidence": "面料摸起来挺舒服的"
    },
    {
      "slot_id": "s3",
      "aspect": "舒适度",
      "entity": "领口",
      "entity_id": "e2",
      "entity_type": "part",
      "attribute": "触感",
      "value": "扎",
      "condition": "洗后更明显",
      "polarity": "negative",
      "severity": "medium",
      "evidence": "领口有点扎，特别是刚洗完之后更明显"
    },
    {
      "slot_id": "s4",
      "aspect": "尺码/版型",
      "entity": null,
      "attribute": "尺码偏差",
      "value": "偏大",
      "recommendation": "建议小一码",
      "target_group": "身材娇小",
      "target_group_entity_id": "e3",
      "polarity": "negative",
      "severity": "low",
      "evidence": "尺码偏大，建议身材娇小的妹妹买小一码"
    }
  ]
}
```

**业务价值解读：**
- s1：碎花蓝有色差问题 → 更新主图或在颜色描述旁标注"实物颜色较图片略深"
- s3：领口扎且洗后加剧 → 领口处理工艺或材质问题，反馈工厂
- s4：尺码偏大集中于娇小身材 → 详情页增加尺码建议说明

---

### 示例 2：电子产品类 —— 部件定位 / 兼容性 / 老化时间

**评论（rating=2）：**
> "耳机整体设计还可以，就是左耳的硅胶耳塞太硬了，戴一小时就很难受。右耳用了三周就开始漏电，充满电不到半天就没电了。蓝牙连接iPhone的时候正常，连Mac就总是掉线。"

```json
{
  "review_id": "r-0234",
  "entities": [
    {"entity_id": "e1", "type": "part", "text": "左耳"},
    {"entity_id": "e2", "type": "component", "text": "硅胶耳塞"},
    {"entity_id": "e3", "type": "part", "text": "右耳"},
    {"entity_id": "e4", "type": "device", "text": "iPhone"},
    {"entity_id": "e5", "type": "device", "text": "Mac"}
  ],
  "slots": [
    {
      "slot_id": "s1",
      "aspect": "舒适度",
      "entity": "硅胶耳塞",
      "entity_id": "e2",
      "entity_type": "component",
      "location": "左耳",
      "location_entity_id": "e1",
      "attribute": "硬度",
      "value": "太硬",
      "consequence": "戴一小时就难受",
      "polarity": "negative",
      "severity": "medium",
      "evidence": "左耳的硅胶耳塞太硬了，戴一小时就很难受"
    },
    {
      "slot_id": "s2",
      "aspect": "续航/电池",
      "entity": "右耳",
      "entity_id": "e3",
      "entity_type": "part",
      "attribute": "电池寿命",
      "value": "不到半天",
      "onset_time": "使用三周后",
      "issue_type": "漏电",
      "polarity": "negative",
      "severity": "high",
      "evidence": "右耳用了三周就开始漏电，充满电不到半天就没电了"
    },
    {
      "slot_id": "s3",
      "aspect": "连接稳定性",
      "entity": null,
      "attribute": "蓝牙兼容性",
      "normal_condition": {
        "device": "iPhone",
        "device_entity_id": "e4",
        "assessment": "正常"
      },
      "problem_condition": {
        "device": "Mac",
        "device_entity_id": "e5",
        "issue": "掉线"
      },
      "polarity": "negative",
      "severity": "medium",
      "evidence": "蓝牙连接iPhone的时候正常，连Mac就总是掉线"
    }
  ]
}
```

**业务价值解读：**
- s1：左耳硅胶耳塞硬度问题 → 检查该批次耳塞硅胶配方，是否需要换更软的材质
- s2：右耳三周后漏电 → severity: high，排查4月入库电池批次，联系电池供应商
- s3：Mac 蓝牙兼容性 → 技术/固件团队排查，可能是 macOS 协议兼容问题

---

### 示例 3：食品类 —— 口味差异 / 规格性价比 / 场景

**评论（rating=4）：**
> "口感挺好的，就是奶油味这款比较腻，建议跟原味搭配着吃。包装比较精致，适合送礼。就是量少了点，12粒定价有点贵，原味和抹茶口味倒是很值。"

```json
{
  "review_id": "r-0567",
  "entities": [
    {"entity_id": "e1", "type": "flavor", "text": "奶油味"},
    {"entity_id": "e2", "type": "flavor", "text": "原味"},
    {"entity_id": "e3", "type": "flavor", "text": "抹茶口味"},
    {"entity_id": "e4", "type": "quantity", "text": "12粒"},
    {"entity_id": "e5", "type": "scenario", "text": "送礼"}
  ],
  "slots": [
    {
      "slot_id": "s1",
      "aspect": "口感/味道",
      "entity": "奶油味",
      "entity_id": "e1",
      "entity_type": "flavor",
      "attribute": "甜腻程度",
      "value": "比较腻",
      "recommendation": "与原味搭配食用",
      "polarity": "negative",
      "severity": "low",
      "evidence": "奶油味这款比较腻，建议跟原味搭配着吃"
    },
    {
      "slot_id": "s2",
      "aspect": "包装",
      "entity": null,
      "attribute": "精致程度",
      "value": "精致",
      "scenario": "送礼",
      "scenario_entity_id": "e5",
      "polarity": "positive",
      "evidence": "包装比较精致，适合送礼"
    },
    {
      "slot_id": "s3",
      "aspect": "性价比",
      "entity": "12粒",
      "entity_id": "e4",
      "entity_type": "quantity",
      "attribute": "量感",
      "value": "偏少",
      "price_perception": "偏贵",
      "polarity": "negative",
      "severity": "low",
      "evidence": "量少了点，12粒定价有点贵"
    },
    {
      "slot_id": "s4",
      "aspect": "性价比",
      "entity_list": ["原味", "抹茶口味"],
      "entity_id_list": ["e2", "e3"],
      "attribute": "价值感",
      "value": "很值",
      "polarity": "positive",
      "evidence": "原味和抹茶口味倒是很值"
    }
  ]
}
```

---

### 示例 4：母婴类 —— 安全性 / 季节适用 / 年龄段

**评论（rating=5）：**
> "给四个月的宝宝买的，包裹着睡觉用，材质很柔软，孩子不会起湿疹。就是夏天太厚了点，春秋用很合适。宝宝睡觉翻身多，发现还挺牢固的。"

```json
{
  "review_id": "r-0789",
  "entities": [
    {"entity_id": "e1", "type": "user_group", "text": "四个月的宝宝"},
    {"entity_id": "e2", "type": "scenario", "text": "包裹睡觉"},
    {"entity_id": "e3", "type": "time_condition", "text": "夏天"},
    {"entity_id": "e4", "type": "time_condition", "text": "春秋"}
  ],
  "slots": [
    {
      "slot_id": "s1",
      "aspect": "材质/亲肤性",
      "entity": null,
      "attribute": "柔软度",
      "value": "很柔软",
      "skin_safety": "不起湿疹",
      "affected_group": "婴儿（四个月）",
      "affected_group_entity_id": "e1",
      "polarity": "positive",
      "evidence": "材质很柔软，孩子不会起湿疹"
    },
    {
      "slot_id": "s2",
      "aspect": "保暖性/厚度",
      "entity": null,
      "attribute": "厚度季节匹配",
      "seasonal_assessment": {
        "summer": {"entity_id": "e3", "value": "偏厚", "polarity": "negative"},
        "spring_autumn": {"entity_id": "e4", "value": "合适", "polarity": "positive"}
      },
      "polarity": "mixed",
      "evidence": "夏天太厚了点，春秋用很合适"
    },
    {
      "slot_id": "s3",
      "aspect": "耐用性/牢固性",
      "entity": null,
      "attribute": "结构稳定性",
      "value": "牢固",
      "test_condition": "宝宝大量翻身",
      "affected_group": "婴儿",
      "polarity": "positive",
      "evidence": "宝宝睡觉翻身多，发现还挺牢固的"
    }
  ]
}
```

---

## SKU 级别聚合分析：按实体维度汇总问题

当处理批量评论时，可以按实体维度生成问题分布：

### 按颜色/款式聚合

```json
{
  "dimension": "product_variant",
  "product_id": "SKU-DRESS-023",
  "summary": [
    {
      "entity": "碎花蓝",
      "negative_mentions": 234,
      "main_issues": ["颜色偏暗", "色差大"],
      "severity_max": "medium"
    },
    {
      "entity": "纯白款",
      "negative_mentions": 89,
      "main_issues": ["易透", "易脏"],
      "severity_max": "medium"
    },
    {
      "entity": "浅粉色",
      "negative_mentions": 12,
      "main_issues": [],
      "sentiment": "以正面为主"
    }
  ]
}
```

### 按部件聚合

```json
{
  "dimension": "part",
  "product_id": "SKU-HEADPHONE-007",
  "summary": [
    {
      "entity": "硅胶耳塞",
      "negative_mentions": 234,
      "main_issues": ["太硬", "易滑落", "出汗后不稳"],
      "severity_max": "medium"
    },
    {
      "entity": "充电盒",
      "negative_mentions": 178,
      "main_issues": ["盖子松动", "接触不良"],
      "severity_max": "high"
    },
    {
      "entity": "左耳",
      "negative_mentions": 156,
      "main_issues": ["音量偏小", "电池老化快"],
      "severity_max": "high"
    }
  ]
}
```

### 按尺码聚合（服装类）

```json
{
  "dimension": "size_spec",
  "product_id": "SKU-SHIRT-045",
  "summary": [
    {
      "size": "XS",
      "feedback": {"偏小": "43%", "正好": "52%", "偏大": "5%"},
      "net_bias": "偏小",
      "severity": "medium"
    },
    {
      "size": "M",
      "feedback": {"偏小": "18%", "正好": "70%", "偏大": "12%"},
      "net_bias": "基本准确",
      "severity": "low"
    },
    {
      "size": "XL",
      "feedback": {"偏小": "5%", "正好": "43%", "偏大": "52%"},
      "net_bias": "偏大",
      "severity": "high"
    }
  ]
}
```

---

## 时间序列监控：发现批次质量变化

当评论数据包含时间戳时，可以做趋势监控：

```json
{
  "product_id": "SKU-HEADPHONE-007",
  "monitor_aspect": "续航/电池",
  "monitor_entity": "电池",
  "time_series": [
    {"month": "2024-01", "total": 1234, "negative_count": 45, "negative_rate": 0.036},
    {"month": "2024-02", "total": 1456, "negative_count": 52, "negative_rate": 0.036},
    {"month": "2024-03", "total": 1678, "negative_count": 61, "negative_rate": 0.036},
    {"month": "2024-04", "total": 1523, "negative_count": 89, "negative_rate": 0.058},
    {"month": "2024-05", "total": 1689, "negative_count": 178, "negative_rate": 0.105},
    {"month": "2024-06", "total": 1345, "negative_count": 167, "negative_rate": 0.124}
  ],
  "alert": {
    "triggered": true,
    "trigger_month": "2024-04",
    "reason": "续航负面占比从3.6%升至5.8%，此后持续恶化至12.4%",
    "hypothesis": "4月入库批次电池可能存在质量问题",
    "recommended_action": "排查2024年4月入库电池批次，联系电池供应商"
  }
}
```

---

## 常见错误与边界情况

**不要做的事：**

1. **不要在没有实体的情况下强行填实体**：如果用户只说"颜色不好看"没提具体颜色，entity 字段应为 null，不要猜测
2. **不要把方面和属性混淆**：aspect 是"舒适度"，attribute 是"硬度"，value 是"太硬"——三者层级不同
3. **不要遗漏正面实体**：不只是负面方面才抽取实体，"原味口感很好"中的"原味"也应作为实体抽取
4. **severity 是针对业务影响的判断，不是情绪强度**：用户说"太难受了"（情绪强烈）但如果只是轻微不便，severity 仍应为 medium 或 low