# 模式 1: 参考生成 (Reference-based Generation)

**触发词**: "参考这个店铺生成"、"照着这个风格做"、"分析这个链接的设计"

**输入**: 店铺 URL 或产品页面 URL

**流程**:

## Step 1: 截取参考页面

使用 OpenClaw 浏览器打开目标 URL 并截图。截取首页、产品页、详情页等关键页面。

```
操作: 使用 take_screenshot MCP 工具
目标: 截取 3-5 张关键页面截图
保存: /tmp/design-pipeline/reference/
```

## Step 2: 风格拆解分析

对截图进行视觉风格分析，提取以下要素:

```
分析维度:
├── 色彩体系
│   ├── 主色 (dominant color + hex)
│   ├── 辅色 (secondary colors)
│   ├── 强调色 (accent color)
│   └── 整体色温 (暖/冷/中性)
├── 字体风格
│   ├── 标题字体特征 (衬线/无衬线/手写/艺术)
│   ├── 正文字体特征
│   └── 字重分布
├── 布局特征
│   ├── 构图模式 (对称/非对称/网格/自由)
│   ├── 留白比例 (紧凑/适中/通透)
│   └── 视觉层级 (主副标题/图文比例)
├── 视觉情绪
│   ├── 风格标签 (科技/清新/奢华/促销/日系/韩系)
│   ├── 目标人群推测
│   └── 品牌调性关键词
└── 素材特征
    ├── 产品图风格 (实拍/渲染/抠图/场景)
    ├── 背景处理 (纯色/渐变/场景/纹理)
    └── 装饰元素 (几何/花卉/光效/无)
```

## Step 3: 生成设计简报 (Design Brief)

将分析结果整理为结构化设计简报:

```markdown
## 设计简报

**参考来源**: [URL]
**风格定义**: [3-5个关键词，如: 日系极简、暖色调、留白通透]

**色彩方案**:
- 主色: #XXXXXX (色名)
- 辅色: #XXXXXX, #XXXXXX
- 强调色: #XXXXXX
- 背景: #XXXXXX

**视觉规范**:
- 构图: [对称居中 / 左图右文 / 通栏大图]
- 留白: [高 / 中 / 低]
- 情绪: [关键词]

**适用提示词模板**: (见 Step 4)
```

将设计简报保存到 `/tmp/design-pipeline/brief.md`。

## Step 4: AI 生图

根据设计简报构造 nano-banana2 提示词并生成图像:

```bash
cd {baseDir}/../nano-banana2/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "[根据简报构造的提示词]" \
  --aspect-ratio "1:1" \
  --output "/tmp/design-pipeline/output/"
```

**提示词构造规则** (将风格要素注入提示词):

```
[产品/场景主体描述],
[风格关键词] style,
color palette: [主色名] with [辅色名] accents,
[背景描述: 如 clean white background / gradient from #XXX to #XXX],
[光线描述: 如 soft natural lighting / studio lighting with rim light],
[构图描述: 如 centered composition / rule of thirds],
[情绪关键词: 如 premium, minimalist, warm, inviting],
product photography, e-commerce ready, high resolution
```

## Step 5: 输出交付

```
输出目录: /tmp/design-pipeline/output/
├── brief.md          # 设计简报
├── reference/        # 参考截图
└── generated/        # 生成的素材图片
```
