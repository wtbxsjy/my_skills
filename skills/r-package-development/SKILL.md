---
name: r-package-development
description: R package development guide covering dependencies, devtools workflow, API design, testing, documentation, NEWS, and release practices. Use when developing, testing, documenting, checking, or releasing R packages; when working with devtools, roxygen2, testthat, pkgdown, pak, or renv; or when building package infrastructure and exported APIs.
---

# R Package Development Decision Guide

*Dependencies, workflow, API design, testing, documentation, and release practices for R packages*

## Skill Boundaries

Use this skill when the task is package-specific:

- scaffolding or maintaining an R package
- editing `DESCRIPTION`, `NAMESPACE`, `NEWS.md`, `_pkgdown.yml`, or roxygen
- setting up tests, checks, CI-facing package workflows, or release steps
- deciding imports, suggests, exports, package API, and lifecycle policy

Prefer narrower companion skills when appropriate:

- Use `testing-r-packages` for deeper `testthat` patterns and test design.
- Use `cli` for sophisticated condition formatting and console UX.
- Use `lifecycle` for deprecations, supersedure, and lifecycle badges.
- Use `modern-r` or `tidyverse-patterns` for non-package-specific code modernization or syntax decisions inside individual functions.

## Preferred Toolchain

Default to the current r-lib and Posit package-development stack unless the repository clearly uses another workflow:

- `usethis` for package scaffolding and common maintenance tasks
- `devtools` for interactive load, test, document, and check loops
- `testthat` edition 3 for tests
- `roxygen2` for documentation and namespace generation
- `pkgdown` for reference site validation
- `pak` for dependency installation and resolution
- `renv` for project-local environment management when the project is already using it
- `cli` for user-facing conditions and semantic console output
- `lifecycle` for staged API changes and deprecations

If the task is mostly about one of these specialized topics, prefer the dedicated skill as well:

- `testing-r-packages` for deeper `testthat` design
- `cli` for rich user-facing conditions and console UX
- `lifecycle` for deprecation, supersedure, and lifecycle badges
- `cran-extrachecks` for CRAN submission hardening

## Core Workflow

Use these commands as the default development loop:

```bash
# Load the package and run exploratory code
Rscript -e "devtools::load_all(); code"

# Run all tests
Rscript -e "devtools::test()"

# Run tests matching a file prefix
Rscript -e "devtools::test(filter = '^{name}')"

# Run tests associated with one source file
Rscript -e "devtools::test_active_file('R/{name}.R')"

# Document exported functions and refresh NAMESPACE/man
Rscript -e "devtools::document()"

# Check pkgdown reference structure
Rscript -e "pkgdown::check_pkgdown()"

# Run package checks
Rscript -e "devtools::check()"

# Format code when the project uses air
air format .
```

Prefer `pak` for installing dependencies and `renv` for project-local environments when the package or repo already uses them.

Use `usethis` for repetitive setup work rather than hand-editing package infrastructure when a standard helper exists.

```r
usethis::create_package()
usethis::use_r("foo")
usethis::use_testthat(3)
usethis::use_test("foo")
usethis::use_package("cli")
usethis::use_package("testthat", type = "Suggests")
usethis::use_lifecycle()
usethis::use_news_md()
```

## Coding Defaults

- Use the native pipe `|>` in new or substantially revised code.
- Use `\(x)` for short anonymous functions and `function(...) {}` when the body is multi-line or needs clarity.
- Keep exported APIs stable and explicit; keep helpers internal unless users need them directly.
- Never call `library()` inside package code.
- Prefer namespace qualification or `@importFrom` for imports.
- Restore any temporary state changes with `on.exit()`.
- Prefer `cli` conditions over raw `stop()`, `warning()`, and `message()` for user-facing paths.
- Think about lifecycle stage before exposing a new API that may need to change soon.

## Dependency Strategy

### When to Add Dependencies vs Base R

```r
# Add dependency when:
# - Significant functionality gain
# - Maintenance burden reduction
# - User experience improvement
# - Complex implementation (regex, dates, web)

# Use base R when:
# - Simple utility functions
# - Package will be widely used (minimize deps)
# - Dependency is large for small benefit
# - Base R solution is straightforward

# Example decisions:
str_detect(x, "pattern")    # Worth stringr dependency
length(x) > 0              # Don't need purrr for this
parse_dates(x)             # Worth lubridate dependency
x + 1                      # Don't need dplyr for this
```

### Tidyverse Dependency Guidelines

```r
# Core tidyverse (usually worth it):
dplyr     # Complex data manipulation
purrr     # Functional programming, parallel
stringr   # String manipulation
tidyr     # Data reshaping

# Specialized tidyverse (evaluate carefully):
lubridate # If heavy date manipulation
forcats   # If many categorical operations
readr     # If specific file reading needs
ggplot2   # If package creates visualizations

# Heavy dependencies (use sparingly):
tidyverse # Meta-package, very heavy
shiny     # Only for interactive apps
```

### Dependency Specification in DESCRIPTION

```
# Strong dependencies (required)
Imports:
    dplyr (>= 1.2.0),
    rlang (>= 1.1.0)

# Suggested dependencies (optional)
Suggests:
    testthat (>= 3.0.0),
    knitr,
    rmarkdown

# Enhanced functionality (optional but loaded if available)
Enhances:
    data.table
```

Prefer narrowly scoped imports over `tidyverse` as a meta-package dependency.
Prefer `Imports` only for functions used in package code and `Suggests` for tooling, examples, optional integrations, and tests.

## API Design Patterns

### Function Design Strategy

```r
# Modern tidyverse API patterns

# 1. Use .by for per-operation grouping
my_summarise <- function(.data, ..., .by = NULL) {
  # Support modern grouped operations
}

# 2. Use {{ }} for user-provided columns
my_select <- function(.data, cols) {
  .data |> select({{ cols }})
}

# 3. Use ... for flexible arguments
my_mutate <- function(.data, ..., .by = NULL) {
  .data |> mutate(..., .by = {{ .by }})
}

# 4. Return consistent types (tibbles, not data.frames)
my_function <- function(.data) {
  result |> tibble::as_tibble()
}
```

### Input Validation Strategy

```r
# Validation level by function type:

# User-facing functions - comprehensive validation
user_function <- function(x, threshold = 0.5) {
  # Check all inputs thoroughly
  if (!is.numeric(x)) stop("x must be numeric")
  if (!is.numeric(threshold) || length(threshold) != 1) {
    stop("threshold must be a single number")
  }
  # ... function body
}

# Internal functions - minimal validation
.internal_function <- function(x, threshold) {
  # Assume inputs are valid (document assumptions)
  # Only check critical invariants
  # ... function body
}

# Package functions with vctrs - type-stable validation
safe_function <- function(x, y) {
  x <- vec_cast(x, double())
  y <- vec_cast(y, double())
  # Automatic type checking and coercion
}
```

For exported functions, prefer `rlang::check_*()` helpers, `vctrs`, or explicit validation over ad hoc coercion that hides invalid input.

## Error Handling Patterns

```r
# Good error messages - specific and actionable
if (length(x) == 0) {
  cli::cli_abort(
    "Input {.arg x} cannot be empty.",
    "i" = "Provide a non-empty vector."
  )
}

# Include function name in errors
validate_input <- function(x, call = caller_env()) {
  if (!is.numeric(x)) {
    cli::cli_abort("Input must be numeric", call = call)
  }
}

# Use consistent error styling
# cli package for user-friendly messages
# rlang for developer tools
```

Prefer `cli::cli_abort()`, `cli::cli_warn()`, and `cli::cli_inform()` for user-facing messages.
Use custom error classes when downstream code or tests need to distinguish failure modes programmatically.

### Error Classes

```r
# Custom error classes for programmatic handling
my_error <- function(message, ..., call = caller_env()) {
  cli::cli_abort(
    message,
    ...,
    class = "my_package_error",
    call = call
  )
}

# Specific error types
validation_error <- function(message, ..., call = caller_env()) {
  cli::cli_abort(
    message,
    ...,
    class = c("validation_error", "my_package_error"),
    call = call
  )
}
```

## When to Create Internal vs Exported Functions

### Export Function When

```r
# Export when:
# - Users will call it directly
# - Other packages might want to extend it
# - Part of the core package functionality
# - Stable API that won't change often

# Example: main data processing functions
#' @export
process_data <- function(.data, ...) {
  # Comprehensive input validation
  # Full documentation required
  # Stable API contract
}
```

### Keep Function Internal When

```r
# Keep internal when:
# - Implementation detail that may change
# - Only used within package
# - Complex implementation helpers
# - Would clutter user-facing API

# Example: helper functions (no @export)
.validate_input <- function(x, y) {
  # Minimal documentation
  # Can change without breaking users
  # Assume inputs are pre-validated
}

# Naming convention: prefix with . for internal functions
.compute_metrics <- function(data) { ... }
```

## Testing and Documentation Strategy

### Testing Defaults

- Put tests for `R/{name}.R` in `tests/testthat/test-{name}.R`.
- Use `testthat` edition 3 by default.
- Add tests for all new user-facing behavior.
- Place new tests next to related existing tests when a convention already exists.
- Keep tests small and focused.
- Prefer specific expectations over `expect_true()` and `expect_false()` when a more informative matcher exists.
- Prefer `expect_snapshot(error = TRUE)` for errors and `expect_snapshot()` for warnings when the full message text matters.
- Use `withr` for cleanup of options, environment variables, temp files, and working directories.
- Prefer self-sufficient tests that can run in isolation.

### Testing Levels

```r
# Unit tests - individual functions
test_that("function handles edge cases", {
  expect_equal(my_func(c()), expected_empty_result)
  expect_error(my_func(NULL), class = "my_error_class")
})

# Integration tests - workflow combinations
test_that("pipeline works end-to-end", {
  result <- data |>
    step1() |>
    step2() |>
    step3()
  expect_s3_class(result, "expected_class")
})

# Property-based tests for package functions
test_that("function properties hold", {
  # Test invariants across many inputs
})
```

### Test File Organization

```
tests/
  testthat/
    test-validation.R      # Input validation tests
    test-processing.R      # Core processing tests
    test-output.R          # Output format tests
    test-integration.R     # End-to-end tests
    helper-fixtures.R      # Shared test fixtures
  testthat.R              # Test runner
```

### Snapshot Testing

```r
# For complex outputs that are hard to specify exactly
test_that("summary output is correct", {
  expect_snapshot(summary(my_object))
})

# For error messages
test_that("errors are informative",
  expect_snapshot(my_function(bad_input), error = TRUE)
})
```

### Documentation Defaults

- Every exported function should have roxygen2 documentation.
- Internal functions should generally not have roxygen blocks.
- Wrap roxygen comments at about 80 characters.
- Re-run `devtools::document()` after changing roxygen comments.
- When you add a new user-facing topic, make sure `_pkgdown.yml` includes it.
- Use `pkgdown::check_pkgdown()` to catch missing reference topics.
- Add lifecycle badges and deprecation notes when function or argument stage is not simply stable.

### Documentation Priorities

```r
# Must document:
# - All exported functions
# - Complex algorithms or formulas
# - Non-obvious parameter interactions
# - Examples of typical usage

# Can skip documentation:
# - Simple internal helpers
# - Obvious parameter meanings
# - Functions that just call other functions
```

### roxygen2 Documentation

```r
#' Process and summarize data
#'
#' @description
#' Takes a data frame and computes summary statistics
#' for specified variables.
#'
#' @param data A data frame or tibble.
#' @param vars <[`tidy-select`][dplyr::dplyr_tidy_select]> Columns to summarize.
#' @param .by <[`data-masking`][dplyr::dplyr_data_masking]> Optional grouping variable.
#'
#' @return A tibble with summary statistics.
#'
#' @examples
#' mtcars |> process_data(mpg, .by = cyl)
#'
#' @export
process_data <- function(data, vars, .by = NULL) {
  # ...
}
```

## NEWS.md

- Add a `NEWS.md` bullet for each user-facing change.
- Skip bullets for tiny documentation edits or purely internal refactors.
- Mention the function name early when a bullet is function-specific.
- Mention the related issue when available.
- Keep each bullet on one line.
- Order bullets alphabetically by function name, with general bullets first.
- Keep the wording user-facing rather than implementation-focused.

## Package Structure

### Recommended Directory Layout

```
mypackage/
  DESCRIPTION
  NAMESPACE
  LICENSE
  README.md
  R/
    utils.R           # Internal utilities
    validation.R      # Input validation
    core.R            # Core functionality
    methods.R         # S3/S7 methods
    zzz.R             # .onLoad, .onAttach
  man/                # Generated by roxygen2
  tests/
    testthat/
    testthat.R
  vignettes/
    getting-started.Rmd
  inst/
    extdata/          # Example data files
  data/               # Package data (lazy-loaded)
  data-raw/           # Scripts to create package data
```

### DESCRIPTION Best Practices

```
Package: mypackage
Title: What The Package Does (One Line)
Version: 0.1.0
Authors@R:
    person("First", "Last", email = "email@example.com",
           role = c("aut", "cre"))
Description: A longer description that spans multiple lines.
    Use four spaces for continuation lines.
License: MIT + file LICENSE
Encoding: UTF-8
Roxygen: list(markdown = TRUE)
RoxygenNote: 7.2.3
Imports:
    dplyr (>= 1.1.0),
    rlang (>= 1.0.0)
Suggests:
    testthat (>= 3.0.0)
Config/testthat/edition: 3
```

## Release Checklist

```r
# Before release:
devtools::check()         # Must pass with 0 errors, warnings, notes
devtools::test()          # All tests pass
devtools::document()      # Documentation up to date
urlchecker::url_check()   # All URLs valid
spelling::spell_check_package()  # No typos

# Update version
usethis::use_version("minor")  # or "major", "patch"

# Update NEWS.md with changes

# Final checks
devtools::check(remote = TRUE, manual = TRUE)
```

Before release, also confirm that examples, URLs, pkgdown topics, and test snapshots are current.
If the package uses lifecycle stages or deprecations, confirm that badges, warnings, and NEWS entries stay aligned.

## Common Package Development Mistakes

```r
# Avoid - Using library() in package code
library(dplyr)  # Never in package code!

# Good - Use namespace qualification
dplyr::filter(data, x > 0)

# Or import in NAMESPACE via roxygen2
#' @importFrom dplyr filter mutate

# Avoid - Modifying global state
options(my_option = TRUE)  # Side effect!

# Good - Restore state if you must modify
old_opts <- options(my_option = TRUE)
on.exit(options(old_opts), add = TRUE)

# Avoid - Hardcoded paths
read.csv("/home/user/data.csv")

# Good - Use system.file for package data
system.file("extdata", "data.csv", package = "mypackage")
```
