# Modern R Guide

Use this reference when you need examples or exact recommendations for contemporary tidyverse-oriented R work. The guidance below has been refreshed against `dplyr` 1.2.0.

## Core Principles

1. Prefer modern tidyverse APIs and R-native syntax.
2. Write readable code before optimizing.
3. Profile before changing code for speed.
4. Keep interfaces explicit about whether they accept expressions or strings.

## Tidyverse Defaults

### Prefer current `dplyr` 1.2+ guidance

Treat `.by` and `reframe()` as stable parts of modern `dplyr`, not experimental features. When updating older guidance, also consider whether `filter_out()`, `when_any()`, `when_all()`, and the newer recoding helpers make the code clearer.

### Prefer `|>` over `%>%`

Use the native pipe in new or meaningfully revised code unless the surrounding file intentionally standardizes on `%>%`.

```r
data |>
  filter(year >= 2020) |>
  summarise(mean_value = mean(value, na.rm = TRUE))
```

### Prefer `join_by()` for joins

Use `join_by()` instead of character vectors, especially when keys differ or when conditions are more complex than equality.

```r
transactions |>
  inner_join(companies, by = join_by(company == id))

transactions |>
  inner_join(companies, by = join_by(company == id, year >= since))

transactions |>
  inner_join(companies, by = join_by(company == id, closest(year >= since)))
```

When match assumptions matter, consider:

```r
inner_join(x, y, by = join_by(id), multiple = "error")
inner_join(x, y, by = join_by(id), unmatched = "error")
```

### Prefer `.by` for one-off grouping

Use `.by` when a grouping only matters for one verb and you want to avoid persistent grouping state. In `dplyr` 1.2.0, `.by` is stable.

```r
sales |>
  summarise(total = sum(revenue), .by = c(company, year))

sales |>
  mutate(share = revenue / sum(revenue), .by = company)
```

Use `group_by()` only when the grouped state intentionally spans multiple downstream verbs.

### Use `filter_out()` for row-dropping logic

Prefer `filter_out()` when you are specifying rows to drop rather than rows to keep. It often reads more directly than a negated `filter()` condition and behaves more clearly around missing values.

```r
df |>
  filter_out(count == 0)
```

### Use `when_any()` and `when_all()` for multi-condition filtering

Prefer `when_any()` and `when_all()` when you want repeated `|` or `&` behavior across multiple conditions inside `filter()` or `filter_out()`.

```r
countries |>
  filter(when_any(
    name %in% c("US", "CA") & between(score, 200, 300),
    name %in% c("PR", "RU") & between(score, 100, 200)
  ))
```

### Prefer `across()`, `pick()`, and `reframe()`

```r
df |>
  summarise(across(where(is.numeric), mean, na.rm = TRUE), .by = group)

df |>
  summarise(n_metrics = ncol(pick(starts_with("metric_"))))

df |>
  reframe(q = quantile(x, c(0.25, 0.5, 0.75)), .by = group)
```

## Tidyeval and rlang

Pick one interface style and implement it cleanly.

### Bare-column interface: use `{{ }}`

```r
summ_mean <- function(data, group, value) {
  data |>
    summarise(mean = mean({{ value }}, na.rm = TRUE), .by = {{ group }})
}
```

### String interface: use `.data[[ ]]` and `all_of()`

```r
summ_mean_chr <- function(data, group, value) {
  data |>
    summarise(mean = mean(.data[[value]], na.rm = TRUE), .by = all_of(group))
}
```

Use `.env` when an environment value could be confused with a column.

```r
threshold <- 10

df |>
  filter(.data$value > .env$threshold)
```

Use `!!` and `!!!` only when explicit injection is truly needed. Do not reach for them before simpler `{{ }}` or `.data[[ ]]` patterns.

### Prefer newer recoding helpers when appropriate

For modern `dplyr`, `replace_when()`, `recode_values()`, and `replace_values()` may be clearer than older `case_match()` or `recode()`-style guidance, especially when updating values from a lookup table or expressing explicit replacements.

## purrr

Prefer type-stable mapping and modern list binding helpers.

```r
means <- split(df$value, df$group) |>
  purrr::map_dbl(mean, na.rm = TRUE)

model_metrics <- resamples |>
  purrr::map(\(x) fit_model(x)) |>
  list_rbind()
```

Prefer `walk()` for side effects and `map_*()` when the return type should be predictable. Avoid `sapply()` in package or production code because it can change output type unexpectedly.

## stringr

Prefer `stringr` for a consistent string API with pipe-friendly argument order.

```r
text |>
  stringr::str_to_lower() |>
  stringr::str_trim() |>
  stringr::str_replace_all("pattern", "replacement")
```

Good defaults:

- `str_detect()` for logical tests
- `str_extract()` for extraction
- `str_replace()` and `str_replace_all()` for replacement
- `str_split()` for splitting
- `str_glue()` for templated strings

Use `fixed()`, `regex()`, or `coll()` when you need to make matching semantics explicit.

## Package and Project Practices

Prefer:

- `pak` for package installation and dependency resolution
- `renv` for project-local dependency management
- small exported APIs with predictable return types
- tests for wrappers around data-masking interfaces and joins

When editing package code, check namespace usage, tests, and lifecycle implications before changing public interfaces.

## Performance Workflow

Follow this order:

1. Confirm that performance matters for the task.
2. Measure with `bench`, `profvis`, or representative timing.
3. Improve the algorithm, data shape, or repeated work first.
4. Prefer vectorization, preallocation, and reduced copies.
5. Re-measure after the change.

Typical improvements:

- replace repeated `bind_rows()` inside loops with list accumulation then `list_rbind()`
- avoid repeated joins inside per-row or per-group loops
- move invariant calculations outside loops
- use type-stable mapping functions
- remember that `if_else()`, `case_when()`, and `coalesce()` improved materially in `dplyr` 1.2.0, so old warnings about their performance may now be stale

## Common Anti-Patterns

Avoid these unless compatibility requires them:

- `%>%` in newly modernized code
- `by = c("a" = "b")` when `join_by()` is available
- `group_by(...) |> summarise(...) |> ungroup()` for one-off grouped summaries
- `sapply()` when output type matters
- ambiguous tidyeval that mixes strings, bare names, and injected symbols without a clear contract
- using `filter()` with hard-to-read negated logic when `filter_out()` expresses the intent directly
- optimizing code before confirming a bottleneck

## Output Style

When generating or revising code, prefer:

- meaningful object and function names
- short pipelines with one conceptual step per verb
- explicit `na.rm = TRUE` where missing values are expected
- comments only when they explain intent or a non-obvious constraint
