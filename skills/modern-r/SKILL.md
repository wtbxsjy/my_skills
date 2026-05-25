---
name: modern-r
description: Modernize and review existing R code using current idioms and migration priorities across tidyverse, tidy evaluation, style, and performance. Use when refactoring legacy `.R`, `.Rmd`, `.qmd`, or package code; when deciding how to update older R patterns safely; or when you need a broad modernization pass rather than a narrow syntax, style, or package-workflow question.
---

# Modern R

## Overview

Apply current R conventions with a bias toward readable, pipe-friendly, type-stable code. Prefer modern tidyverse idioms, explicit data-masking patterns, and measured optimization over stylistic churn or premature micro-tuning.

Load [references/modern-r-guide.md](references/modern-r-guide.md) when you need examples or exact patterns for joins, `.by`, tidy evaluation, `purrr`, `stringr`, package workflows, or performance guidance.

## Skill Boundaries

Use this skill when the task spans multiple concerns or starts with questions like "modernize", "refactor", "update this old R code", or "what should this code look like now?"

Prefer narrower skills when the task is mostly one topic:

- Use `tidyverse-patterns` for concrete `dplyr`, `purrr`, `stringr`, join, grouping, and tidyeval syntax choices.
- Use `r-style-guide` for naming, spacing, layout, comments, and file organization.
- Use `r-package-development` for package scaffolding, documentation, tests, `DESCRIPTION`, `pkgdown`, `NEWS.md`, and release workflow.
- Use `r-performance` when the main goal is profiling or optimization rather than general modernization.

## Default Approach

When writing or editing R:

1. Preserve the existing project style unless the user asks for broader modernization.
2. Prefer native pipe `|>` over `%>%` in new or substantially revised code.
3. Prefer `dplyr` 1.2+ features such as `join_by()`, stable `.by` and `reframe()`, `pick()`, `filter_out()`, and explicit join quality controls.
4. Use `{{ }}`, `.data[[ ]]`, `.env`, and `across()` deliberately rather than mixing data-masking and string-based access ad hoc.
5. Prefer type-stable and explicit code over clever shortcuts.
6. Only optimize after identifying an actual bottleneck or when the user explicitly asks for performance work.

## Modernization Priorities

When modernizing legacy R, improve in this order:

1. Fix correctness risks first.
Current joins, grouped summaries, NSE, and string handling should be unambiguous and testable.
2. Remove outdated or superseded idioms.
Replace old join syntax, unnecessary persistent grouping, and `map_dfr()`-style superseded patterns when touching related code.
3. Improve API clarity.
Refactor helper functions to use `{{ }}` for user-supplied expressions or `.data[[var]]` for character inputs.
4. Improve readability.
Use clear naming, small transformations, and explicit grouping scope.
5. Optimize only where it matters.

## Review Checklist

Use this checklist when reviewing R code:

1. Pipes: Prefer `|>` unless the surrounding file intentionally uses `%>%`.
2. Joins: Prefer `join_by()` and consider `multiple=` or `unmatched=` when assumptions matter.
3. Grouping: Prefer `.by` for one-off summaries or mutations instead of `group_by()` followed by `ungroup()`.
4. Tidyeval: Match the interface to the input type.
If callers pass bare column names, use `{{ }}`.
If callers pass strings, use `.data[[var]]` or `all_of(vars)`.
5. Column-wise work: Prefer `across()` and `pick()` over manual repetition.
6. Iteration: Prefer `purrr::map_*()` or vectorized code over `sapply()` and ad hoc loops when types matter.
7. Strings: Prefer `stringr` for consistency and pipe-friendly APIs.
8. Performance: Prefer profiling, preallocation, vectorization, and algorithmic improvements before low-level tuning.

## Refactoring Patterns

Apply these transformations when they are safe and local:

```r
# Prefer native pipe in modernized code
df |>
  filter(flag) |>
  summarise(n = dplyr::n())

# Prefer .by for per-operation grouping
df |>
  summarise(avg = mean(value, na.rm = TRUE), .by = group)

# Prefer join_by()
x |>
  left_join(y, by = join_by(id))

# Prefer embrace for bare-column arguments
summ_mean <- function(data, var) {
  data |>
    summarise(mean = mean({{ var }}, na.rm = TRUE))
}

# Prefer .data for string inputs
summ_mean_chr <- function(data, var) {
  data |>
    summarise(mean = mean(.data[[var]], na.rm = TRUE))
}
```

## Boundaries

Do not force modernization that would create broad noisy diffs unless the user asks for a sweep. Do not swap in tidyverse patterns if the codebase is intentionally base-R-first, data.table-first, or constrained by older R versions. If package or version constraints are unclear, make the smallest safe change and state the assumption.

## Reference

Read [references/modern-r-guide.md](references/modern-r-guide.md) for:

- tidyverse modernization examples
- `rlang` and tidy evaluation patterns
- `purrr` and `stringr` recommendations
- style and package development guidance
- performance workflow and anti-patterns
