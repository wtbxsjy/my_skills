# 往返转换：带格式 .xlsx -> gt 表格 -> .xlsx（可选同时导出 HTML 预览）
#
# 用法：
#   Rscript roundtrip.R input.xlsx output.xlsx [--sheet 1] [--dims A1] [--html preview.html] [--freeze]
#
# --sheet   工作表位置（整数）或名称，默认第一个
# --dims    gt 表格写入的左上角单元格，默认 A1
# --html    同时把中间的 gt 表格存为 HTML，便于目视检查 forgts 读取是否正确
# --freeze  冻结标题下方与行名栏右侧

suppressPackageStartupMessages({
  library(forgts)
  library(gt)
  library(openxlsx2)
  library(gtxlsx)
})

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("用法：Rscript roundtrip.R input.xlsx output.xlsx [--sheet 1] [--dims A1] [--html preview.html] [--freeze]")
}

input  <- args[1]
output <- args[2]
opts   <- args[-(1:2)]

get_opt <- function(flag, default = NULL) {
  i <- match(flag, opts)
  if (is.na(i) || i == length(opts)) default else opts[i + 1]
}

if (!file.exists(input)) stop("找不到输入文件：", input)

sheet <- get_opt("--sheet", NULL)
if (!is.null(sheet) && grepl("^[0-9]+$", sheet)) sheet <- as.integer(sheet)
dims   <- get_opt("--dims", "A1")
html   <- get_opt("--html", NULL)
freeze <- "--freeze" %in% opts

gt_tbl <- forgts(input, sheet = sheet)

if (!is.null(html)) gtsave(gt_tbl, html)

wb <- wb_workbook()$add_worksheet(grid_lines = FALSE)
wb <- wb_add_gt(wb, gt_tbl, dims = dims, freeze = freeze)
wb_save(wb, output)

# 简单核对：写回的文件能被读取，且行列数合理
chk <- wb_to_df(wb_load(output), col_names = FALSE)
cat(sprintf("完成：%s -> %s（读回 %d 行 × %d 列）\n", input, output, nrow(chk), ncol(chk)))
cat("提示：forgts 有意忽略表头格式，往返后表头外观与原文件不同属预期。\n")
