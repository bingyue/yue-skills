# 模式 4: 批量生成 (Batch Generation)

**触发词**: "批量生成"、"一组产品图"、"全店主图"、"系列产品图"

**输入**:
- 必填: 产品列表 (名称 + 简要描述)
- 必填: 风格参考 (URL 或风格描述，仅需提供一次)

**流程**:

## Step 1: 风格锁定

执行一次风格分析 (模式 1 的 Step 1-3 或从文字描述提取)。
生成全局风格锚点:

```yaml
style_anchor:
  keywords: ["日系极简", "暖色调", "留白通透"]
  primary_color: "#F5E6D3"
  accent_color: "#C4956A"
  background: "warm beige gradient"
  lighting: "soft natural window light"
  mood: "warm, inviting, premium"
  composition: "centered, generous whitespace"
```

此风格锚点将注入到每一个产品的提示词中，确保全系列视觉一致。

## Step 2: 构造产品提示词矩阵

为每个产品构造独立提示词，但共享风格锚点:

```
产品提示词 =
  [产品具体描述] +
  [style_anchor.keywords] style +
  color palette: [style_anchor.primary_color] with [style_anchor.accent_color] +
  [style_anchor.background] +
  [style_anchor.lighting] +
  [style_anchor.mood] +
  [style_anchor.composition] +
  product photography, e-commerce ready, high resolution
```

示例 (假设 3 个产品):

```
产品矩阵:
├── Product 1: 保温杯 → "[保温杯描述], 日系极简 style, warm beige gradient bg, ..."
├── Product 2: 咖啡壶 → "[咖啡壶描述], 日系极简 style, warm beige gradient bg, ..."
└── Product 3: 茶具套装 → "[茶具描述], 日系极简 style, warm beige gradient bg, ..."
```

## Step 3: 顺序执行生图

为每个产品调用 nano-banana2 (顺序执行，避免并发限制):

```bash
# 产品 1
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[产品1完整提示词]" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/batch/product-01/"

# 产品 2
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[产品2完整提示词]" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/batch/product-02/"

# 产品 N ...
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[产品N完整提示词]" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/batch/product-NN/"
```

## Step 4: 一致性审查

生成完所有产品图后，将结果截图或路径汇总展示给用户:

```
批量生成结果:
├── product-01/ 保温杯     ✅ 已生成
├── product-02/ 咖啡壶     ✅ 已生成
├── product-03/ 茶具套装   ✅ 已生成
└── 风格一致性: [简要评估]
```

如果某个产品图风格偏离，调整该产品提示词后单独重新生成。

## Step 5: 输出

```
/tmp/design-pipeline/batch/
├── style-anchor.yaml    # 风格锚点文件
├── product-01/          # 产品1的主图
├── product-02/          # 产品2的主图
├── product-03/          # 产品3的主图
└── ...
```
