# 模式 2: 产品主图 (Product Main Image)

**触发词**: "做主图"、"生成产品图"、"产品主图"

**输入**:
- 必填: 产品名称/描述
- 可选: 风格参考 URL 或风格描述

**流程**:

## Step 1: 风格确认

如果提供了参考 URL，执行模式 1 的 Step 1-3 获取风格简报。
如果提供了文字描述，直接提取风格关键词。
如果都未提供，使用默认电商主图风格 (干净白底、产品居中、柔光)。

## Step 2: 构造主图提示词

主图提示词模板:

```
[产品名称] product photo,
[产品材质/颜色/特征描述],
[风格关键词] style,
[背景: 默认 clean white background, 或根据风格调整],
centered composition, studio lighting,
soft shadows, product photography,
e-commerce main image, high resolution, 8K detail
```

**变体策略** (为同一产品生成多个变体):

| 变体 | 调整维度 | 示例 |
|------|----------|------|
| A - 标准白底 | background: pure white | 淘宝标准主图 |
| B - 场景化 | background: lifestyle scene | 使用场景展示 |
| C - 氛围感 | lighting: dramatic | 品牌质感图 |
| D - 细节特写 | composition: macro close-up | 材质/工艺展示 |

## Step 3: 批量调用生图

为每个变体调用 nano-banana2:

```bash
# 变体 A: 白底标准
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[产品名] product photo, clean white background, centered, studio lighting, soft shadows, e-commerce main image, 8K" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/product-main/variant-a/"

# 变体 B: 场景化
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[产品名] in a [场景] setting, lifestyle photography, natural lighting, warm tones, 8K" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/product-main/variant-b/"

# 变体 C: 氛围感
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[产品名], dramatic studio lighting, rim light, dark moody background, premium feel, 8K" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/product-main/variant-c/"

# 变体 D: 细节特写
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[产品名] macro close-up, texture detail, shallow depth of field, studio lighting, 8K" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/product-main/variant-d/"
```

## Step 4: 输出

```
/tmp/design-pipeline/product-main/
├── variant-a/    # 白底标准主图
├── variant-b/    # 场景化主图
├── variant-c/    # 氛围感主图
└── variant-d/    # 细节特写主图
```

向用户展示所有变体，询问偏好方向后可进一步迭代。
