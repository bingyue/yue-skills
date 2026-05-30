# python-docx 高级用法参考

## 安装

```bash
pip install python-docx
```

## 页眉页脚

```python
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

section = doc.sections[0]

# 页眉
header = section.header
header.is_linked_to_previous = False
hp = header.paragraphs[0]
hp.text = "页眉文字"
hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
for run in hp.runs:
    run.font.size = Pt(9)
    run.font.name = '宋体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

# 页脚（页码）
footer = section.footer
footer.is_linked_to_previous = False
fp = footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
# 插入页码域代码
from docx.oxml import OxmlElement
run = fp.add_run()
fldChar1 = OxmlElement('w:fldChar')
fldChar1.set(qn('w:fldCharType'), 'begin')
run._element.append(fldChar1)

run2 = fp.add_run()
instrText = OxmlElement('w:instrText')
instrText.set(qn('xml:space'), 'preserve')
instrText.text = ' PAGE '
run2._element.append(instrText)

run3 = fp.add_run()
fldChar2 = OxmlElement('w:fldChar')
fldChar2.set(qn('w:fldCharType'), 'end')
run3._element.append(fldChar2)
```

## 图片插入

```python
from docx.shared import Inches, Mm

# 插入图片
doc.add_picture('image.png', width=Inches(4))

# 图片居中
last_paragraph = doc.paragraphs[-1]
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

# 在表格单元格中插入图片
cell = table.cell(0, 0)
paragraph = cell.paragraphs[0]
run = paragraph.add_run()
run.add_picture('photo.jpg', width=Mm(25), height=Mm(35))
```

## 高级表格操作

```python
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

# 合并单元格
table.cell(0, 0).merge(table.cell(0, 2))  # 合并第1行的1-3列

# 单元格背景色
cell = table.cell(0, 0)
shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="4472C4"/>')
cell._element.get_or_add_tcPr().append(shading)

# 单元格垂直居中
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

# 设置行高
from docx.shared import Pt
from docx.oxml import OxmlElement
tr = table.rows[0]._tr
trPr = tr.get_or_add_trPr()
trHeight = OxmlElement('w:trHeight')
trHeight.set(qn('w:val'), str(int(Pt(30))))
trHeight.set(qn('w:hRule'), 'atLeast')
trPr.append(trHeight)

# 表格无边框
from docx.oxml import OxmlElement
for row in table.rows:
    for cell in row.cells:
        tc = cell._element
        tcPr = tc.get_or_add_tcPr()
        tcBorders = OxmlElement('w:tcBorders')
        for border_name in ['top', 'left', 'bottom', 'right']:
            border = OxmlElement(f'w:{border_name}')
            border.set(qn('w:val'), 'none')
            border.set(qn('w:sz'), '0')
            tcBorders.append(border)
        tcPr.append(tcBorders)
```

## 样式操作

```python
# 使用内置样式
doc.add_heading('标题1', level=1)
doc.add_heading('标题2', level=2)

# 自定义样式
from docx.enum.style import WD_STYLE_TYPE
style = doc.styles.add_style('CustomBody', WD_STYLE_TYPE.PARAGRAPH)
style.font.name = '仿宋_GB2312'
style.font.size = Pt(16)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '仿宋_GB2312')
style.paragraph_format.first_line_indent = Pt(32)
style.paragraph_format.line_spacing = Pt(28.95)

# 使用自定义样式
doc.add_paragraph('正文内容', style='CustomBody')
```

## 分节符

```python
from docx.enum.section import WD_ORIENT

# 新增节（用于改变页面方向等）
new_section = doc.add_section()
new_section.orientation = WD_ORIENT.LANDSCAPE
new_section.page_width = Mm(297)
new_section.page_height = Mm(210)
```

## 超链接

```python
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_hyperlink(paragraph, url, text):
    part = paragraph.part
    r_id = part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)

    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)

    run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    color = OxmlElement('w:color')
    color.set(qn('w:val'), '0563C1')
    rPr.append(color)
    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    rPr.append(u)
    run.append(rPr)

    text_elem = OxmlElement('w:t')
    text_elem.text = text
    run.append(text_elem)

    hyperlink.append(run)
    paragraph._element.append(hyperlink)
```

## 水印

```python
# python-docx 不直接支持水印，但可通过XML操作添加
# 推荐在生成后用WPS手动添加水印
# 或使用 Header 中的文本框模拟
```

## 常见问题

### WPS兼容性
- `python-docx` 生成的 .docx 文件完全兼容 WPS
- 某些高级Word功能（如内容控件）在WPS中可能显示不同
- 建议最终用WPS打开确认格式

### 中文字体
- Windows: 直接使用字体名称
- macOS: 系统可能未预装公文字体（方正小标宋等），生成文件在Windows/WPS中打开即可
- 字体回退：如果目标字体不存在，WPS会自动替换为相近字体
