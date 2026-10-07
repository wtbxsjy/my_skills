---
name: gt-xlsx-roundtrip
description: 在带格式的 Excel 电子表格（.xlsx）与 R 语言 gt 表格对象之间双向转换，使用 forgts（电子表格 → gt）和 gtxlsx（gt → 电子表格）。当用户提到把 Excel/xlsx 转成 gt 表格、保留单元格颜色/填充/加粗/边框、把 gt 表格导出为 Excel、spreadsheet 与 gt 往返（round-trip）、forgts、gtxlsx、wb_add_gt、wb_to_gt、openxlsx2，或想在报告（HTML、PDF、Quarto、R Markdown）里展示带格式的电子表格而不贴截图时，务必使用本 skill，即使用户没有明确说出这两个包的名字。Convert formatted spreadsheets to gt tables and back with forgts and gtxlsx.
---

# gt 与电子表格往返转换（forgts + gtxlsx）

## 这个 skill 解决什么问题

很多数据最初存在带颜色、加粗、边框的 Excel 文件里，这些格式本身携带信息（例如高亮异常值）。把它放进报告时，常见做法是截图，既不能编辑，也不清晰。两个 R 包恰好各管一个方向：

| 方向 | 包 | 核心函数 |
|---|---|---|
| 电子表格 → gt 表格 | forgts | `forgts(file, sheet = NULL)` |
| gt 表格 → 电子表格 | gtxlsx | `wb_add_gt(wb, x, ...)` |

两者串联即可“往返”：先读入 → 在 R 里对 gt 对象做修改 → 再写回 Excel，格式不丢。

名词说明（按本 skill 的写作约定，专业名词首次出现时解释）：

- **gt**：R 语言包，全称 “Grammar of Tables”（表格语法），用来构建可发表的展示表格。
- **forgts**：名称取自 “for gt s”，即“为 gt 服务”的读取包。
- **openxlsx2**：读写 Excel 文件的 R 包，gtxlsx 把 gt 表格写入它创建的工作簿对象。
- **工作簿（workbook）**：一个 .xlsx 文件；**工作表（worksheet）**：工作簿内的一个标签页。
- **列跨越标题（column spanner）**：横跨多列的上层表头。
- **行名栏（stub）**：gt 表格最左侧用作行标签的那一列。

## 工作流程

### 第 0 步：确认 R 环境

先检查 R 是否可用以及包是否已安装：

```bash
Rscript -e 'for (p in c("gt","forgts","gtxlsx","openxlsx2")) cat(p, requireNamespace(p, quietly = TRUE), "\n")'
```

缺包时运行 `scripts/install_packages.R`（forgts 来自 CRAN；gtxlsx 目前通过 r-universe 或 GitHub 安装，不在 CRAN 的稳定版里时用后者）。如果环境没有 R，不要假装执行成功：把代码交给用户在本机运行，并明确说明未经本地验证。

### 第 1 步：判断转换方向

- 用户有 .xlsx 想得到 gt 表格（用于 HTML/PDF/幻灯片）→ 方向 A
- 用户有 gt 表格想得到 .xlsx → 方向 B
- 用户想“读入、改一改、再写回 Excel” → 往返（A + B）

### 方向 A：电子表格 → gt（forgts）

```r
library(forgts)
library(gt)

gt_tbl <- forgts("input.xlsx")            # 默认读第一个工作表
gt_tbl <- forgts("input.xlsx", sheet = 2) # 按位置；也可传工作表名称字符串
gtsave(gt_tbl, "table.html")              # 或 .png / .pdf（后两者需额外依赖）
```

forgts 支持的格式：字体粗体、斜体、颜色、下划线、删除线，单元格填充色，以及边框的颜色和粗细。

### 方向 B：gt → 电子表格（gtxlsx）

```r
library(gt)
library(openxlsx2)
library(gtxlsx)

wb <- wb_workbook()$add_worksheet(grid_lines = FALSE)
wb <- wb_add_gt(wb, gt_tbl, dims = "B2")   # dims 为表格左上角位置
wb_save(wb, "output.xlsx")
```

gtxlsx 保留标题、列跨越标题、行分组、行名栏、汇总行、脚注和 `tab_style()`/`tab_options()` 设置的样式。数值保持为数值：gt 显示 `$1,234.50` 时，单元格内是 1234.5，并附带货币数字格式，所以文件仍可计算。

`wb_add_gt()` 常用参数：

- `dims`：左上角单元格，默认 `"A1"`
- `numeric`：能复现格式时按数值写入，设为 `FALSE` 则只写文本
- `col_widths`：`"auto"`（默认）自动列宽
- `features`：`TRUE` 写入全部格式；`FALSE` 只写值；也可给子集，如 `c("font", "fill", "border", "numfmt", "merge", "link")`
- `freeze`：`TRUE` 冻结标题下方和行名栏右侧
- 传入 `gt_group`（`gt_group()` 或 `gt_split()` 的结果）时，多个表格依次写入，`gap` 控制间隔行数

### 往返

```r
library(forgts); library(gt); library(openxlsx2); library(gtxlsx)

gt_tbl <- forgts("input.xlsx")
# 可选：在这里对 gt_tbl 做修改，例如 tab_header()、fmt_number()、tab_style()
wb <- wb_workbook()$add_worksheet(grid_lines = FALSE)
wb <- wb_add_gt(wb, gt_tbl)
wb_save(wb, "input_roundtrip.xlsx")
```

也可以直接运行打包好的脚本：

```bash
Rscript scripts/roundtrip.R input.xlsx output.xlsx --sheet 1 --dims B2 --html preview.html
```

## 必须向用户说明的限制

这些限制来自两个包的文档，转换前先对照用户的文件，避免承诺做不到的事：

1. **forgts 刻意忽略表头（header）的格式**，且格式是叠加在 gt 默认样式之上的。所以往返后表头外观与原文件不同是预期行为，不是 bug。
2. forgts 文档未说明合并单元格和多工作表的支持；有合并单元格的文件要先抽查结果。每次只读一个工作表，多个工作表就分别调用。
3. gtxlsx 无法保留 gt 以图片形式绘制的内容：`fmt_image()` 和 `cols_nanoplot()` 得到空单元格；`fmt_icon()`、`fmt_flag()` 退化为文字标签；`fmt_url()` 只保留链接文字，不保留链接。
4. gtxlsx 还提供 `wb_to_gt()`（直接从 openxlsx2 工作簿读回 gt），但作者标注为实验性的“开发玩具”：行分组、行名栏、脚注标记和数字格式都不会还原。需要还原格式时优先用 forgts。
5. 两个包都较新（forgts 为 0.0.1.9000 开发版号，gtxlsx 为 0.4.0），接口可能变动；出现函数找不到或参数报错时，先查最新文档（见 `references/api-notes.md` 末尾的链接），不要凭记忆改写。
6. gtxlsx 作者自述不使用 gt，对 gt 一侧的更新可能滞后；遇到较新的 gt 功能写出异常时，先用 `gtxlsx_extract()` 查看 gtxlsx 眼中的表格结构。

## 验证转换结果

不要只看代码是否报错，格式是否真的保留才是目的：

- 方向 A：用 `gtsave()` 导出 HTML 或 PNG 并目视对照原文件的几个带格式单元格（填充色、粗体、边框）。
- 方向 B / 往返：用 `openxlsx2::wb_to_df(wb, col_names = FALSE)` 检查数值是否仍为数值；有条件时把 .xlsx 转成 PDF 或图片再看一眼样式。
- 往返后对比行数、列数和关键单元格的值是否与原文件一致。

## 结尾给用户的说明

交付时简要说明：产出文件的位置、哪些格式确认保留、哪些因上述限制发生变化（尤其是表头格式）。若环境没有 R、脚本未实际运行，要直说。

更详细的函数签名与链接见 `references/api-notes.md`。
