---
name: r-skill-changelog-sync
description: Sync installed Codex R skills with current upstream package changes by checking official changelog sources such as CRAN package pages, CRAN NEWS pages, and pkgdown news sites. Use when an R-focused skill may be stale, when package guidance mentions old versions or deprecated APIs, or when refreshing skills for packages like dplyr, tidyr, purrr, stringr, rlang, tibble, or other CRAN packages after a release.
---

# R Skill Changelog Sync

## Overview

Refresh an installed skill from upstream package changes without rewriting it from scratch. Gather authoritative version and changelog data first, then update only the guidance that is now stale, newly stable, newly deprecated, or materially improved by the release.

Use `scripts/fetch_r_pkg_changelog.py` to build a current snapshot before editing any skill text. Read [references/update-workflow.md](references/update-workflow.md) for the editing rubric and [references/package-map-template.md](references/package-map-template.md) when you want a repeatable mapping from skills to packages.

## Workflow

1. Identify the target skill directory and the packages it depends on.
For example, `modern-r` depends on packages such as `dplyr`, `rlang`, `purrr`, `stringr`, `tidyr`, and `tibble`.
2. Run the snapshot script for the relevant package or packages.
Prefer official sources only: CRAN package page first, then CRAN NEWS or pkgdown news discovered from that page.
3. Compare the snapshot against the installed skill text.
Look for old version anchors, experimental APIs that are now stable, newly deprecated functions, and newly recommended replacements.
4. Update the skill conservatively.
Preserve durable guidance. Only patch statements that are outdated, incomplete, or contradicted by the changelog.
5. Keep the skill compact.
Summarize release changes into agent-usable rules rather than pasting long release notes.
6. Validate by re-running the snapshot script or re-reading the edited sections.

## Default Commands

Use the helper script like this:

```bash
python scripts/fetch_r_pkg_changelog.py --package dplyr --format markdown
python scripts/fetch_r_pkg_changelog.py --package dplyr --package rlang --format markdown
python scripts/fetch_r_pkg_changelog.py --package dplyr --limit 8 --write /tmp/dplyr-update.md
```

If you are updating an installed skill in `~/.codex/skills`, run the script first, then patch the target `SKILL.md` or `references/*.md` with `apply_patch`.

## What To Update

Good candidates for edits:

- version anchors such as `dplyr 1.1+` that should become `dplyr 1.2+`
- statements about experimental features that are now stable
- recommendations that should switch to newly preferred helpers
- references to deprecated functions that now have a clearer replacement
- performance guidance when the changelog documents meaningful speed or memory improvements

## What Not To Update

Avoid churn:

- do not rewrite a whole skill because one package added a minor helper
- do not mirror full NEWS files into the skill
- do not treat every new function as immediately central guidance
- do not promote experimental features unless the changelog or docs indicate a stable recommendation
- do not remove existing advice unless the official changelog or documentation clearly supersedes it

## Editing Heuristics

When patching a skill:

1. Prefer updating `references/` files for detailed API guidance.
2. Keep `SKILL.md` focused on triggering, workflow, and durable defaults.
3. Mention specific versions only when the threshold matters for behavior or recommendations.
4. Add a source note or "last checked" line only if it helps future maintenance.
5. Convert changelog details into concise rules, examples, or anti-patterns.

## Example

For `modern-r`, a `dplyr` update might lead to edits like:

- change `dplyr 1.1+` to `dplyr 1.2+`
- note that `.by` and `reframe()` are stable rather than experimental
- add `filter_out()` as a readable row-dropping helper
- mention `when_any()` and `when_all()` where row filtering patterns are discussed
- mark `case_match()` guidance as superseded when `recode_values()` or `replace_values()` are the official replacement

## References

Read [references/update-workflow.md](references/update-workflow.md) for the detailed process.
Read [references/package-map-template.md](references/package-map-template.md) when you want a reusable skill-to-package map.
