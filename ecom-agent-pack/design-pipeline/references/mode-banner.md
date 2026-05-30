# 模式 3: 店铺 Banner

**触发词**: "做Banner"、"做海报"、"做活动图"、"促销Banner"

**输入**:
- 必填: 活动信息 (活动名称、折扣力度、时间)
- 可选: 风格参考 URL 或风格描述
- 可选: 需要的文案内容

**流程**:

## Step 1: 提取活动信息

解析用户输入，提取:

```yaml
activity_name: "618年中大促"        # 活动名称
discount: "全场5折起"               # 折扣信息
date_range: "6.1 - 6.18"           # 活动日期
tagline: "年中钜惠，不负好时光"      # 宣传语 (如无则生成)
products: ["产品A", "产品B"]         # 主推产品 (如有)
cta: "立即抢购"                     # 行动号召 (如无则生成)
```

## Step 2: 确定风格

如果提供了参考 URL，执行模式 1 的 Step 1-3。
否则根据活动类型匹配预设风格:

| 活动类型 | 推荐风格 | 色彩方向 |
|----------|----------|----------|
| 618/双11/双12 | 热烈促销 | 红金/橙红 |
| 年货节/春节 | 国潮喜庆 | 正红/金色 |
| 38女王节 | 优雅精致 | 粉紫/玫瑰金 |
| 夏季清仓 | 清凉活力 | 蓝绿/冰蓝 |
| 日常上新 | 简约时尚 | 品牌主色 |
| 会员日 | 尊享高端 | 黑金/深蓝 |

## Step 3: 构造 Banner 提示词

Banner 提示词模板:

```
E-commerce promotional banner design,
[活动名称] sale event,
[风格关键词] style,
color scheme: [色彩方案],
[布局描述: 如 large bold text on left, product images on right],
text area reserved for: "[活动名称]" "[折扣信息]" "[行动号召]",
[装饰元素: 如 geometric shapes, confetti, light effects, ribbon],
festive and eye-catching, high contrast,
wide format banner, e-commerce ready, high resolution
```

**重要**: Banner 通常需要留出文字区域。在提示词中明确指示文案放置位置和空间，生成后用 ecommerce-designer 或手工叠加文字层。

## Step 4: 生成多尺寸 Banner

```bash
# 通栏 Banner (21:9)
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[Banner提示词]" \
  --aspect-ratio "21:9" \
  --output "/tmp/design-pipeline/banner/wide/"

# 标准 Banner (16:9)
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[Banner提示词]" \
  --aspect-ratio "16:9" \
  --output "/tmp/design-pipeline/banner/standard/"

# 移动端 Banner (如需要, 3:4)
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[Banner提示词, 竖版构图调整]" \
  --aspect-ratio "3:4" \
  --output "/tmp/design-pipeline/banner/mobile/"
```

## Step 5: 文字叠加 (可选)

如果 ecommerce-designer 可用，调用其模版渲染:

```bash
cd {baseDir}/../ecommerce-designer/scripts && .venv/bin/python render_template.py \
  --type poster \
  --title "[活动名称]" \
  --subtitle "[折扣信息]" \
  --discount "[折扣]" \
  --style "[风格]" \
  --background "/tmp/design-pipeline/banner/wide/[生成的图片]" \
  --output "/tmp/design-pipeline/banner/final/"
```

否则在输出中注明: 文字需要后期在 PS/Figma/Canva 中叠加。

## Step 6: 输出

```
/tmp/design-pipeline/banner/
├── wide/       # 21:9 通栏Banner
├── standard/   # 16:9 标准Banner
├── mobile/     # 3:4 移动端Banner (如生成)
└── final/      # 叠加文字后的成品 (如可用)
```
