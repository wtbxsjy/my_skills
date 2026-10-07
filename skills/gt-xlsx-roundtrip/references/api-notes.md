# 函数与限制速查

信息来源见文末链接。包版本较新，参数以最新文档为准。

## forgts（电子表格 → gt 表格）

```r
forgts(file, sheet = NULL)
```

- `file`：电子表格路径
- `sheet`：工作表名称（字符串）或位置（整数）；省略时读第一个工作表
- 返回：gt 表格对象，可用于 R Markdown / Quarto，可用 `gt::gtsave()` 导出
- 内部依赖 readxl、tidyxl、unheadr 读取数据和格式
- 支持：粗体、斜体、字体颜色、下划线、删除线、填充色、边框（颜色和粗细）
- 表头格式被有意忽略；格式叠加在 gt 默认样式之上

安装：

```r
install.packages("forgts")                                            # CRAN
install.packages("forgts", repos = "https://luisdva.r-universe.dev")  # R-universe
remotes::install_github("luisDVA/forgts")                             # GitHub 开发版
```

## gtxlsx（gt 表格 → 电子表格）

| 函数 | 作用 |
|---|---|
| `wb_add_gt()` | 把 gt 表格写入工作表 |
| `wb_add_html()` | 把 HTML 表格写入工作表（读取内联样式，`colspan`/`rowspan` 变为合并区域） |
| `wb_add_lt()` | 把 lt 表格写入工作表 |
| `wb_to_gt()` | 把工作表区域转回 gt（实验性） |
| `gtxlsx_extract()` | 查看已构建 gt 表格的各个组成部分 |

```r
wb_add_gt(
  wb, x,
  sheet = current_sheet(), dims = "A1",
  numeric = TRUE, col_widths = "auto", row_heights = NULL,
  ignore_errors = TRUE, gap = 1L, features = TRUE, freeze = FALSE, ...
)
```

- `x`：`gt_tbl`，或 `gt_group()` / `gt_split()` 的结果
- `row_heights`：`NULL` 用电子表格默认；`"gt"` 使用 gt 的内边距；也可给数值向量
- `ignore_errors`：给形似数字或日期的文本单元格加标记，抑制 Excel 的警告
- 返回修改后的工作簿（输入对象本身不被改动，返回的是副本，所以要接收返回值：`wb <- wb_add_gt(wb, tbl)`）

```r
wb_to_gt(wb, sheet = current_sheet(), dims = NULL, styles = TRUE, structure = TRUE, ...)
```

- `structure = TRUE`：顶部整行合并 → 标题；部分合并行 → 列跨越标题；底部整行合并 → 来源注释
- 已知不还原：行分组、行名栏、脚注标记、数字格式（如 `$115,900` 变回 `115900`）

安装：

```r
install.packages(
  "gtxlsx",
  repos = c("https://janmarvin.r-universe.dev", "https://cloud.r-project.org")
)
# 或：remotes::install_github("JanMarvin/gtxlsx")
```

gtxlsx 覆盖 gt 渲染前应用的内容：所有 `fmt_*()`、`sub_*()`、`cols_merge_*()`、`text_transform()`、`data_color()`、`summary_rows()`、列跨越标题、脚注标记、`opt_stylize()` 及 `tab_options()`。

## 最小往返示例（来自 forgts 自带数据）

```r
library(forgts); library(gt); library(openxlsx2); library(gtxlsx)

f <- system.file("extdata/rodentsheet.xlsx", package = "forgts")
gt_tbl <- forgts(f)

wb <- wb_workbook()$add_worksheet(grid_lines = FALSE)
wb <- wb_add_gt(wb, gt_tbl)
wb_save(wb, "rodentsheet_roundtrip.xlsx")
```

## 链接

- 参考博客：https://luisdva.github.io/rstats/roundtrip-spreadsheets/
- forgts 文档：https://luisdva.github.io/forgts/
- gtxlsx 仓库：https://github.com/JanMarvin/gtxlsx
- gtxlsx 函数索引：https://janmarvin.github.io/gtxlsx/reference/index.html
- openxlsx2：https://janmarvin.github.io/ox2/
