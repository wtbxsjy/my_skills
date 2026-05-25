# Update Workflow

Use this workflow to refresh an installed R-related skill from official upstream package changes.

## 1. Identify Packages

Start by listing the packages that materially shape the skill.

Examples:

- `modern-r`: `dplyr`, `rlang`, `purrr`, `stringr`, `tidyr`, `tibble`
- `r-package-development`: `pak`, `renv`, `testthat`, `usethis`, `devtools`
- `r-performance`: `bench`, `profvis`, `vctrs`, `data.table` if explicitly covered

Ignore weak or incidental dependencies that do not drive the skill's recommendations.

## 2. Build an Upstream Snapshot

Run:

```bash
python scripts/fetch_r_pkg_changelog.py --package dplyr --package rlang --format markdown
```

The script fetches:

- current version and release date from the CRAN package page
- official homepage URL when available
- NEWS URL from the CRAN package page when available
- a compact set of recent changelog bullets

Use the official URLs from the script output as the basis for edits.

## 3. Compare With Installed Skill Text

Look for:

- stale version thresholds
- obsolete warnings about features that are now stable
- missing recommended helpers introduced in the latest release
- deprecated or defunct functions that the skill still treats as current
- performance advice that should reflect new implementation changes

## 4. Patch Conservatively

Prefer small, durable changes:

- update threshold wording such as `1.1+` to `1.2+`
- revise one section instead of rewriting the entire skill
- add one short example if the new API is likely to be used often
- move detailed release-specific notes into `references/`

## 5. Keep Human Review In The Loop

Use automation for retrieval and summarization, not blind replacement.

A good update:

- cites official sources
- changes only the affected guidance
- keeps the skill compact
- remains useful after the next minor release

## 6. Suggested Follow-Up

After patching:

1. Re-open the edited file and sanity-check that the guidance still reads coherently.
2. Re-run the snapshot for the same package if you changed any source links or version wording.
3. If multiple installed skills depend on the same package, consider updating them together.
