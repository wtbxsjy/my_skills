# Package Map Template

Use a small mapping file or checklist like this when you want repeatable skill maintenance.

```yaml
modern-r:
  - dplyr
  - rlang
  - purrr
  - stringr
  - tidyr
  - tibble

r-performance:
  - bench
  - profvis
  - vctrs

r-package-development:
  - pak
  - renv
  - testthat
  - usethis
```

Guidelines:

- keep only the packages that materially change the skill's advice
- prefer package names over whole ecosystems when only one package matters
- store detailed update history in the skill text, not in the map
