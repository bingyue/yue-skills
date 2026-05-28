---
name: ecom-product-image
description: >
  电商全场景图片生成工具。输入产品图片和需求描述，自动生成商品主图、详情页、社媒推广图、
  直播间场景图等全套视觉素材。内置 25 种场景模板（白底主图、生活方式、平铺摆拍、海报 Banner
  等），Campaign Style Lock 机制保证多图视觉一致性。支持 Prompt 输出与 API 直接出图两种模式。
  使用场景：当用户需要为电商产品生成主图、详情页图片、营销图片或完整视觉套组时使用。
---

# ECommerce Product Image Generator

一个面向电商的 AI 图片生成 Skill，基于 GPT-Image-2 API 或兼容接口，
输入产品图片与需求描述，自动生成全套电商视觉素材。

## 功能特性

- **25 种场景模板** — 白底主图、生活方式、平铺摆拍、细节特写、海报 Banner、社媒 UGC、模特展示等
- **Campaign Style Lock** — 多图自动锁定色板、冷暖调、字体、背景光线，保证整套图视觉一致
- **转化驱动诊断** — 自动判断视觉驱动型 / 痛点驱动型 / 情感价值驱动型
- **参考图支持** — 传入产品实拍图，生成外观更贴近真实商品的图片
- **双模式** — 只输出 Prompt 供人工使用，或直接调用 API 出图
- **零依赖脚本** — 纯 Python 标准库实现

## 环境变量

```
OPENAI_API_KEY=<your-openai-compatible-api-key>
OPENAI_BASE_URL=<your-api-endpoint>  # 可选，默认 OpenAI
```

## 使用方式

直接描述产品和需求，例如：

```
帮我生成一套白底主图 + 场景图 + 详情页，产品是北欧风陶瓷咖啡杯
```

也可以附上产品图片让生成结果更贴合实物。
