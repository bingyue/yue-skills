# 字体兼容性映射表

## Windows ↔ macOS 字体映射

| Windows字体 | macOS等效 | 安全替代 |
|-------------|----------|---------|
| 宋体(SimSun) | 宋体-简(Songti SC) | 宋体 |
| 黑体(SimHei) | 黑体-简(Heiti SC) | 黑体 |
| 楷体(KaiTi) | 楷体-简(Kaiti SC) | 楷体 |
| 仿宋(FangSong) | — | 仿宋 |
| 微软雅黑 | 苹方(PingFang SC) | 微软雅黑 |
| 等线(DengXian) | — | 微软雅黑 |
| Calibri | Calibri | Arial |
| Cambria | Cambria | Times New Roman |

## 公文专用字体（可能缺失）

| 字体 | 用途 | 安全替代 |
|------|------|---------|
| 方正小标宋简体 | 公文标题 | 华文中宋 → 黑体 |
| 仿宋_GB2312 | 公文正文 | 仿宋 |
| 楷体_GB2312 | 公文二级标题 | 楷体 |
| 方正大标宋简体 | 大标题 | 华文中宋 → 黑体 |

## 安全字体清单（几乎所有系统都有）

### 中文
- 宋体 (SimSun)
- 黑体 (SimHei)
- 楷体 (KaiTi)
- 仿宋 (FangSong)
- 微软雅黑 (Microsoft YaHei)

### 英文
- Arial
- Times New Roman
- Calibri
- Verdana
- Consolas

## WPS自带字体
WPS Office自带部分字体，不依赖系统：
- 方正书宋_GBK
- 方正仿宋_GBK
- 方正楷体_GBK
- 方正黑体_GBK

## 行距兼容性

| 行距类型 | WPS | Word | 兼容性 |
|---------|-----|------|--------|
| 单倍行距 | ✓ | ✓ | 高 |
| 1.5倍行距 | ✓ | ✓ | 高 |
| 固定值 | ✓ | ✓ | **最高** |
| 多倍行距 | ✓ | ✓ | 中（计算可能不同） |
| 最小值 | ✓ | ✓ | 中 |

建议：跨平台文档使用**固定值**行距。
