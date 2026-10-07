# 安装 gt-xlsx-roundtrip 所需的 R 包。只安装缺失的包。
# 用法：Rscript install_packages.R

cran <- "https://cloud.r-project.org"

need <- function(pkg) !requireNamespace(pkg, quietly = TRUE)

for (p in c("gt", "openxlsx2", "remotes")) {
  if (need(p)) install.packages(p, repos = cran)
}

if (need("forgts")) {
  ok <- tryCatch({
    install.packages("forgts", repos = cran)
    !need("forgts")
  }, error = function(e) FALSE, warning = function(w) FALSE)
  if (!ok) install.packages("forgts", repos = c("https://luisdva.r-universe.dev", cran))
}

if (need("gtxlsx")) {
  ok <- tryCatch({
    install.packages("gtxlsx", repos = c("https://janmarvin.r-universe.dev", cran))
    !need("gtxlsx")
  }, error = function(e) FALSE, warning = function(w) FALSE)
  if (!ok) remotes::install_github("JanMarvin/gtxlsx")
}

for (p in c("gt", "forgts", "gtxlsx", "openxlsx2")) {
  cat(sprintf("%-10s %s\n", p, if (need(p)) "缺失" else "已安装"))
}
