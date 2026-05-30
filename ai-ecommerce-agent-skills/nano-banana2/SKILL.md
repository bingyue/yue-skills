---
name: nano-banana2
description: >
  Nano Banana2 多模态 AI - 支持文生图、图生图、Vision 分析。发送"生图 柴犬"生成图片，发送图片+描述做风格化重绘。底层调用 Gemini，支持 10 种宽高比。关键词：生图、画图、AI画图、文生图、图生图、generate image、Gemini、重绘
metadata:
  openclaw:
    version: 1.0.0
    userInvocable: true
    always: true
    emoji: 🍌
    requires:
      bins: [python3]
---

# Nano Banana2 多模态助手

你可以通过 nano-banana2 模型执行文本对话和图片生成任务。

## 能力

| 任务 | 说明 | 示例 |
|------|------|------|
| 文本对话 | 通用 AI 对话 | 直接发消息 |
| 图片生成 | AI 生成图片 | `生图 一只柴犬在草地上` |
| 多模态 | 文字+图片混合输出 | `画一张海报并解释设计思路` |

## 工作流程

### 当用户需要生成图片时:

识别关键词: "生图"、"画"、"生成图片"、"generate image"、"draw"

**执行脚本:**
```bash
cd {baseDir}/scripts && .venv/bin/python nano_banana2.py \
  --mode image \
  --prompt "用户的图片描述" \
  --aspect-ratio "1:1" \
  --output "/root/.openclaw/media/nano_banana2_output/"
```

支持的宽高比:
- 横版: 21:9, 16:9, 4:3, 3:2
- 正方形: 1:1
- 竖版: 9:16, 3:4, 2:3
- 灵活: 5:4, 4:5

### 当用户需要文本对话时:

```bash
cd {baseDir}/scripts && .venv/bin/python nano_banana2.py \
  --mode text \
  --prompt "用户的问题"
```

### 交互风格

- 如果用户说"生图"/"画"/"生成"开头 → 图片生成模式
- 其他情况 → 文本对话模式
- 图片生成后返回文件路径，询问是否需要调整比例或重新生成
- 支持连续多轮对话

## 故障处理

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `ModuleNotFoundError` | venv 未激活或依赖缺失 | `cd {baseDir}/scripts && .venv/bin/pip install requests` |
| `HTTP 429 Too Many Requests` | Gemini API 限流 | 等待 60 秒后重试，或切换 API Key |
| `HTTP 400 Bad Request` | prompt 包含违规内容或图片过大 | 检查 prompt 内容，压缩输入图片至 <4MB |
| `FileNotFoundError: --image` | 图生图参考图路径错误 | 检查文件路径是否正确，使用绝对路径 |
| 输出目录写入失败 | 目录不存在 | 脚本会自动创建，但需检查磁盘空间 |
| 生成图片为空/纯黑 | 模型理解偏差 | 简化 prompt，移除矛盾描述，重试 |
| `timeout` (120s) | 生成复杂图片耗时过长 | 简化 prompt 或降低分辨率要求 |
