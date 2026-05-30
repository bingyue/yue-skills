# WPS JSA API 参考手册

## 概述

WPS JSA（JavaScript for Applications）是 WPS Office 的宏编程语言，基于 JavaScript，
用于自动化 WPS 文字、WPS 表格和 WPS 演示的操作。

## 与 VBA 的根本区别

JSA 使用 **JavaScript 语法**，但对象模型与 VBA 大体一致。记住：
- 用 `function` 而非 `Sub`
- 用 `var/let/const` 而非 `Dim`
- 用 `//` 注释而非 `'`
- 用 `+` 连接字符串而非 `&`
- 不需要 `Set` 关键字
- 布尔值是 `true/false` 不是 `True/False`

## 常用枚举值

### 对齐方式
```
xlLeft       = -4131
xlCenter     = -4108
xlRight      = -4152
xlJustify    = -4130
```

### 边框类型
```
xlEdgeLeft       = 7
xlEdgeTop        = 8
xlEdgeBottom      = 9
xlEdgeRight      = 10
xlInsideVertical = 11
xlInsideHorizontal = 12
xlDiagonalDown   = 5
xlDiagonalUp     = 6
```

### 方向
```
xlDown  = -4121
xlUp    = -4162
xlToLeft = -4159
xlToRight = -4161
```

### 线条样式
```
xlContinuous = 1
xlDash       = -4115
xlDot        = -4118
xlNone       = -4142
```

### 线条粗细
```
xlThin       = 2
xlMedium     = -4138
xlThick      = 4
xlHairline   = 1
```

### 单元格格式
```
xlGeneral    = 1
xlNumber     = -4145
xlCurrency   = -4146
xlDate       = -4136
xlTime       = 20
xlPercentage = -4147
xlText       = -4158
```

### 查找替换
```
wdReplaceNone = 0
wdReplaceOne  = 1
wdReplaceAll  = 2
```

## WPS 文字 API

### Document 对象

| 属性/方法 | 说明 | 示例 |
|-----------|------|------|
| `Content` | 文档全部内容的Range | `doc.Content.Text` |
| `Paragraphs` | 段落集合 | `doc.Paragraphs.Count` |
| `Tables` | 表格集合 | `doc.Tables.Item(1)` |
| `Bookmarks` | 书签集合 | `doc.Bookmarks.Item("name")` |
| `Sections` | 节集合 | `doc.Sections.Item(1)` |
| `Save()` | 保存 | `doc.Save()` |
| `SaveAs(path)` | 另存为 | `doc.SaveAs("/path/to.docx")` |
| `Close()` | 关闭 | `doc.Close()` |

### Range 对象

| 属性/方法 | 说明 |
|-----------|------|
| `Text` | 获取/设置文本 |
| `Font` | 字体对象（Name, Size, Bold, Italic, Color） |
| `ParagraphFormat` | 段落格式（Alignment, LineSpacing, FirstLineIndent） |
| `Find` | 查找对象 |
| `InsertAfter(text)` | 在后方插入文本 |
| `InsertBefore(text)` | 在前方插入文本 |
| `Delete()` | 删除范围内容 |

### Selection 对象

```javascript
var sel = Application.Selection
sel.TypeText("输入文字")
sel.TypeParagraph()     // 换行
sel.HomeKey(6)          // 移到文档开头（wdStory=6）
sel.EndKey(6)           // 移到文档末尾
sel.MoveDown(5, 3)      // 下移3行（wdLine=5）
```

## WPS 表格 API

### Workbook 对象

| 属性/方法 | 说明 |
|-----------|------|
| `Sheets` / `Worksheets` | 工作表集合 |
| `ActiveSheet` | 当前活动工作表 |
| `Names` | 名称管理器 |
| `Save()` | 保存 |
| `SaveAs(path)` | 另存为 |
| `Close(saveChanges)` | 关闭 |

### Worksheet 对象

| 属性/方法 | 说明 | 示例 |
|-----------|------|------|
| `Range(ref)` | 获取范围 | `ws.Range("A1:B10")` |
| `Cells(row, col)` | 获取单元格 | `ws.Cells(1, 1)` |
| `Rows(ref)` | 行 | `ws.Rows("1:3")` |
| `Columns(ref)` | 列 | `ws.Columns("A:C")` |
| `UsedRange` | 已使用范围 | `ws.UsedRange.Rows.Count` |
| `Name` | 工作表名 | `ws.Name = "数据"` |
| `Copy()` | 复制工作表 | `ws.Copy(undefined, ws2)` |
| `Delete()` | 删除工作表 | `ws.Delete()` |
| `Visible` | 可见性 | `ws.Visible = false` |

### Range 对象（表格）

| 属性/方法 | 说明 |
|-----------|------|
| `Value2` | 获取/设置值（推荐） |
| `Formula` | 获取/设置公式 |
| `NumberFormat` | 数字格式 |
| `Font` | 字体 |
| `Interior.Color` | 背景色（BGR格式） |
| `Borders` | 边框 |
| `HorizontalAlignment` | 水平对齐 |
| `VerticalAlignment` | 垂直对齐 |
| `WrapText` | 自动换行 |
| `MergeCells` | 合并单元格 |
| `Merge()` | 合并 |
| `UnMerge()` | 取消合并 |
| `AutoFit()` | 自适应 |
| `Copy()` | 复制 |
| `Paste()` | 粘贴 |
| `Clear()` | 清除全部 |
| `ClearContents()` | 清除内容 |
| `ClearFormats()` | 清除格式 |
| `Sort(key1, order1)` | 排序 |
| `AutoFilter(field, criteria)` | 自动筛选 |

### 颜色值（BGR格式）

WPS表格中颜色使用BGR格式（不是RGB）：
```javascript
// 红色
cell.Interior.Color = 0x0000FF  // BGR: Blue=0, Green=0, Red=FF
cell.Font.Color = 0x0000FF

// 常用颜色
var RED    = 0x0000FF
var GREEN  = 0x00FF00
var BLUE   = 0xFF0000
var YELLOW = 0x00FFFF
var WHITE  = 0xFFFFFF
var BLACK  = 0x000000

// RGB转BGR
function rgbToBgr(r, g, b) {
    return b * 65536 + g * 256 + r
}
```

## WPS 演示 API

### Presentation 对象

| 属性/方法 | 说明 |
|-----------|------|
| `Slides` | 幻灯片集合 |
| `SlideWidth` | 幻灯片宽度 |
| `SlideHeight` | 幻灯片高度 |
| `Save()` | 保存 |
| `SaveAs(path)` | 另存为 |

### Slide 对象

| 属性/方法 | 说明 |
|-----------|------|
| `Shapes` | 形状集合 |
| `Layout` | 版式 |
| `Delete()` | 删除 |
| `Copy()` | 复制 |
| `Select()` | 选中 |

### Shape 对象

| 属性/方法 | 说明 |
|-----------|------|
| `TextFrame.TextRange` | 文本范围 |
| `HasTextFrame` | 是否有文本框 |
| `Left, Top, Width, Height` | 位置和大小（pt） |
| `Fill` | 填充 |
| `Line` | 线条 |
| `Delete()` | 删除 |

## 文件操作

```javascript
// WPS JSA 中的文件操作相对有限
// 主要通过 Application.Documents/Workbooks 来打开和保存文件

// 打开文件
var doc = Application.Documents.Open("/path/to/file.docx")
var wb = Application.Workbooks.Open("/path/to/file.xlsx")

// 新建
var newDoc = Application.Documents.Add()
var newWb = Application.Workbooks.Add()

// 遍历打开的文档
for (var i = 1; i <= Application.Documents.Count; i++) {
    var d = Application.Documents.Item(i)
    Console.log(d.Name)
}
```

## 用户交互

```javascript
// 弹窗提示
Application.alert("提示消息")

// 输入框（部分版本支持）
// var input = Application.InputBox("请输入：", "标题", "默认值")

// 文件选择对话框
var fd = Application.FileDialog(1) // 1 = msoFileDialogOpen
fd.Title = "选择文件"
fd.Filters.Add("Excel文件", "*.xlsx;*.xls")
if (fd.Show() == -1) {
    var filePath = fd.SelectedItems.Item(1)
}
```

## 性能优化

```javascript
// 关闭屏幕更新（大批量操作时）
Application.ScreenUpdating = false
// ... 批量操作 ...
Application.ScreenUpdating = true

// 关闭自动计算（表格大批量写入时）
Application.Calculation = -4135 // xlCalculationManual
// ... 写入数据 ...
Application.Calculation = -4105 // xlCalculationAutomatic

// 关闭事件（防止触发宏中的事件）
Application.EnableEvents = false
// ... 操作 ...
Application.EnableEvents = true
```

## 调试技巧

1. 用 `Console.log()` 输出到宏编辑器控制台
2. 用 `Application.alert()` 弹窗查看变量值
3. 用 `try...catch` 捕获错误并显示详细信息
4. 在宏编辑器中可以设置断点（部分版本支持）

```javascript
try {
    // 可能出错的代码
} catch (e) {
    Console.log("错误：" + e.message)
    Console.log("行号：" + e.lineNumber)
    Application.alert("出错了：" + e.message)
}
```
