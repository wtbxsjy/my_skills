# Skill 来源与更新

本仓库中的每个 skill 都对应一个上游 GitHub 仓库。升级上游后，运行 `bash update-skills.sh` 即可把所有 skill 同步到最新版本。

- 映射数据文件：[SOURCES.tsv](./SOURCES.tsv)（供 `update-skills.sh` 读取）
- 一键更新脚本：[update-skills.sh](./update-skills.sh)
- 用法：`bash update-skills.sh` 全量同步；`bash update-skills.sh taste-skill` 只同步某个 skill

## 源仓库汇总

### https://github.com/posit-dev/skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/alt-text` | `main` | `alt-text` |  |
| `skills/brand-yml` | `main` | `brand-yml` |  |
| `skills/cli` | `main` | `r-lib/cli` |  |
| `skills/cran-extrachecks` | `main` | `r-lib/cran-extrachecks` |  |
| `skills/create-release-checklist` | `main` | `open-source/create-release-checklist` |  |
| `skills/critical-code-reviewer` | `main` | `posit-dev/critical-code-reviewer` |  |
| `skills/describe-design` | `main` | `posit-dev/describe-design` |  |
| `skills/ggsql` | `main` | `ggsql/ggsql` |  |
| `skills/implement` | `main` | `posit-dev/implement` |  |
| `skills/lifecycle` | `main` | `r-lib/lifecycle` |  |
| `skills/mirai` | `main` | `r-lib/mirai` |  |
| `skills/pr-create` | `main` | `github/pr-create` |  |
| `skills/pr-threads-address` | `main` | `github/pr-threads-address` |  |
| `skills/pr-threads-resolve` | `main` | `github/pr-threads-resolve` |  |
| `skills/quarto-authoring` | `main` | `quarto/quarto-authoring` |  |
| `skills/r-cli-app` | `main` | `r-lib/r-cli-app` |  |
| `skills/r-package-development` | `main` | `r-lib/r-package-development` |  |
| `skills/release-post` | `main` | `open-source/release-post` |  |
| `skills/shiny-bslib` | `main` | `shiny/shiny-bslib` |  |
| `skills/shiny-bslib-theming` | `main` | `shiny/shiny-bslib-theming` |  |
| `skills/testing-r-packages` | `main` | `r-lib/testing-r-packages` |  |
| `skills/working-on` | `main` | `posit-dev/working-on` |  |

### https://github.com/tidymodels/skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/add-dials-parameter` | `main` | `developers/add-dials-parameter` |  |
| `skills/add-parsnip-engine` | `main` | `developers/add-parsnip-engine` |  |
| `skills/add-parsnip-model` | `main` | `developers/add-parsnip-model` |  |
| `skills/add-recipe-step` | `main` | `developers/add-recipe-step` |  |
| `skills/add-yardstick-metric` | `main` | `developers/add-yardstick-metric` |  |
| `skills/tabular-data-ml` | `main` | `users/tabular-data-ml` |  |

### https://github.com/google-deepmind/science-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/alphafold-database-fetch-and-analyze` | `main` | `skills/alphafold_database_fetch_and_analyze` |  |
| `skills/alphagenome-single-variant-analysis` | `main` | `skills/alphagenome_single_variant_analysis` |  |
| `skills/chembl-database` | `main` | `skills/chembl_database` |  |
| `skills/clinical-trials-database` | `main` | `skills/clinical_trials_database` |  |
| `skills/clinvar-database` | `main` | `skills/clinvar_database` |  |
| `skills/credentials` | `main` | `skills/credentials` |  |
| `skills/dbsnp-database` | `main` | `skills/dbsnp_database` |  |
| `skills/embl-ebi-ols` | `main` | `skills/embl_ebi_ols` |  |
| `skills/encode-ccres-database` | `main` | `skills/encode_ccres_database` |  |
| `skills/ensembl-database` | `main` | `skills/ensembl_database` |  |
| `skills/foldseek-structural-search` | `main` | `skills/foldseek_structural_search` |  |
| `skills/gnomad-database` | `main` | `skills/gnomad_database` |  |
| `skills/gtex-database` | `main` | `skills/gtex_database` |  |
| `skills/human-protein-atlas-database` | `main` | `skills/human_protein_atlas_database` |  |
| `skills/interpro-database` | `main` | `skills/interpro_database` |  |
| `skills/jaspar-database` | `main` | `skills/jaspar_database` |  |
| `skills/literature-search-arxiv` | `main` | `skills/literature_search_arxiv` |  |
| `skills/literature-search-biorxiv` | `main` | `skills/literature_search_biorxiv` |  |
| `skills/literature-search-europepmc` | `main` | `skills/literature_search_europepmc` |  |
| `skills/literature-search-openalex` | `main` | `skills/literature_search_openalex` |  |
| `skills/ncbi-sequence-fetch` | `main` | `skills/ncbi_sequence_fetch` |  |
| `skills/openfda-database` | `main` | `skills/openfda_database` |  |
| `skills/opentargets-database` | `main` | `skills/opentargets_database` |  |
| `skills/pdb-database` | `main` | `skills/pdb_database` |  |
| `skills/predictingthepast` | `main` | `skills/predictingthepast` |  |
| `skills/protein-sequence-msa` | `main` | `skills/protein_sequence_msa` |  |
| `skills/protein-sequence-similarity-search` | `main` | `skills/protein_sequence_similarity_search` |  |
| `skills/pubchem-database` | `main` | `skills/pubchem_database` |  |
| `skills/pubmed-database` | `main` | `skills/pubmed_database` |  |
| `skills/pymol` | `main` | `skills/pymol` |  |
| `skills/quickgo-database` | `main` | `skills/quickgo_database` |  |
| `skills/reactome-database` | `main` | `skills/reactome_database` |  |
| `skills/string-database` | `main` | `skills/string_database` |  |
| `skills/ucsc-conservation-and-tfbs` | `main` | `skills/ucsc_conservation_and_tfbs` |  |
| `skills/unibind-database` | `main` | `skills/unibind_database` |  |
| `skills/uniprot-database` | `main` | `skills/uniprot_database` |  |
| `skills/uv` | `main` | `skills/uv` |  |
| `skills/workflow-skill-creator` | `main` | `skills/workflow_skill_creator` |  |

### https://github.com/anthropics/skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/frontend-design` | `main` | `skills/frontend-design` |  |
| `skills/skill-creator` | `main` | `skills/skill-creator` |  |

### https://github.com/duckdb/duckdb-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/attach-db` | `main` | `skills/attach-db` |  |
| `skills/duckdb-docs` | `main` | `skills/duckdb-docs` |  |
| `skills/install-duckdb` | `main` | `skills/install-duckdb` |  |
| `skills/query` | `main` | `skills/query` |  |
| `skills/read-file` | `main` | `skills/read-file` |  |
| `skills/read-memories` | `main` | `skills/read-memories` |  |

### https://github.com/anthropics/knowledge-work-plugins

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/instrument-data-to-allotrope` | `main` | `bio-research/skills/instrument-data-to-allotrope` |  |
| `skills/nextflow-development` | `main` | `bio-research/skills/nextflow-development` |  |
| `skills/scientific-problem-selection` | `main` | `bio-research/skills/scientific-problem-selection` |  |
| `skills/scvi-tools` | `main` | `bio-research/skills/scvi-tools` |  |
| `skills/single-cell-rna-qc` | `main` | `bio-research/skills/single-cell-rna-qc` |  |
| `skills/start` | `main` | `bio-research/skills/start` |  |

### https://github.com/mdwoicke/obsidian-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/defuddle` | `main` | `skills/defuddle` |  |
| `skills/json-canvas` | `main` | `skills/json-canvas` |  |
| `skills/obsidian-bases` | `main` | `skills/obsidian-bases` |  |
| `skills/obsidian-cli` | `main` | `skills/obsidian-cli` |  |
| `skills/obsidian-markdown` | `main` | `skills/obsidian-markdown` |  |

### https://github.com/minimax-ai/skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/frontend-dev` | `main` | `skills/frontend-dev` |  |
| `skills/fullstack-dev` | `main` | `skills/fullstack-dev` |  |
| `skills/gif-sticker-maker` | `main` | `skills/gif-sticker-maker` |  |
| `skills/minimax-docx` | `main` | `skills/minimax-docx` |  |
| `skills/minimax-pdf` | `main` | `skills/minimax-pdf` |  |
| `skills/minimax-xlsx` | `main` | `skills/minimax-xlsx` |  |
| `skills/pptx-generator` | `main` | `skills/pptx-generator` |  |

### https://github.com/daymade/claude-code-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/ima-skill` | `main` | `ima-copilot` |  |

### https://github.com/anthropics/claude-plugins-official

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/claude-automation-recommender` | `main` | `plugins/claude-code-setup/skills/claude-automation-recommender` |  |
| `skills/claude-md-improver` | `main` | `plugins/claude-md-management/skills/claude-md-improver` |  |
| `skills/session-report` | `main` | `plugins/session-report/skills/session-report` |  |
| `skills/writing-rules` | `main` | `plugins/hookify/skills/writing-rules` |  |
| `plugin-skills/claude-code-setup/claude-automation-recommender` | `main` | `plugins/claude-code-setup/skills/claude-automation-recommender` |  |
| `plugin-skills/claude-md-management/claude-md-improver` | `main` | `plugins/claude-md-management/skills/claude-md-improver` |  |
| `plugin-skills/frontend-design/frontend-design` | `main` | `plugins/frontend-design/skills/frontend-design` |  |
| `plugin-skills/hookify/writing-rules` | `main` | `plugins/hookify/skills/writing-rules` |  |
| `plugin-skills/session-report/session-report` | `main` | `plugins/session-report/skills/session-report` |  |
| `plugin-skills/skill-creator/skill-creator` | `main` | `plugins/skill-creator/skills/skill-creator` |  |

### https://github.com/nexu-io/open-design

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/brandkit` | `main` | `skills/brandkit` |  |
| `skills/brutalist-skill` | `main` | `skills/brutalist-skill` |  |
| `skills/gpt-tasteskill` | `main` | `skills/gpt-tasteskill` |  |
| `skills/image-to-code-skill` | `main` | `skills/image-to-code-skill` |  |
| `skills/imagegen-frontend-mobile` | `main` | `skills/imagegen-frontend-mobile` |  |
| `skills/imagegen-frontend-web` | `main` | `skills/imagegen-frontend-web` |  |
| `skills/minimalist-skill` | `main` | `skills/minimalist-skill` |  |
| `skills/output-skill` | `main` | `skills/output-skill` |  |
| `skills/redesign-skill` | `main` | `skills/redesign-skill` |  |
| `skills/soft-skill` | `main` | `skills/soft-skill` |  |
| `skills/stitch-skill` | `main` | `skills/stitch-skill` |  |
| `skills/taste-skill` | `main` | `skills/taste-skill` |  |
| `skills/taste-skill-v1` | `main` | `skills/taste-skill-v1` |  |

### https://github.com/ab604/claude-code-r-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/r-bayes` | `main` | `.claude/skills/r-bayes` |  |
| `skills/r-oop` | `main` | `.claude/skills/r-oop` |  |
| `skills/r-performance` | `main` | `.claude/skills/r-performance` |  |
| `skills/r-style-guide` | `main` | `.claude/skills/r-style-guide` |  |
| `skills/rlang-patterns` | `main` | `.claude/skills/rlang-patterns` |  |
| `skills/tdd-workflow` | `main` | `.claude/skills/tdd-workflow` |  |
| `skills/tidyverse-patterns` | `main` | `.claude/skills/tidyverse-patterns` |  |

### https://github.com/ai-integr8tor/posit-dev-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/quarto-alt-text` | `add-py-shiny-dashboard-skills` | `quarto/quarto-alt-text` | posit-dev/skills 的 fork（含 quarto-alt-text） |

### https://github.com/Jeffallan/claude-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/cpp-pro` | `main` | `skills/cpp-pro` |  |

### https://github.com/BurukalaManiReethika/Karpathy-Inspired-Claude-Code-Guidelines

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/karpathy-guidelines` | `main` | `skills/karpathy-guidelines` |  |

### https://github.com/Cocoon-AI/architecture-diagram-generator

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/architecture-diagram-generator` | `main` | `architecture-diagram` |  |

### https://github.com/github/awesome-copilot

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/excalidraw-diagram-generator` | `main` | `skills/excalidraw-diagram-generator` |  |

### https://github.com/microsoft/playwright-cli

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/playwright-cli` | `main` | `skills/playwright-cli` |  |

### https://github.com/yizhiyanhua-ai/fireworks-tech-graph

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/fireworks-tech-graph` | `main` | `.` |  |

### https://github.com/zarazhangrui/frontend-slides

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/frontend-slides` | `main` | `.` |  |

### https://github.com/op7418/guizang-ppt-skill

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/guizang-ppt-skill` | `main` | `.` |  |

### https://github.com/hugohe3/ppt-master

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/ppt-master` | `main` | `skills/ppt-master` |  |

### https://github.com/leonardomso/rust-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/rust-skills` | `master` | `.` |  |

### https://github.com/alfredo-hs/quarto-talks

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/quarto-talks` | `main` | `.` |  |

## 自定义 Skill（无公开源，不参与自动更新）

| Skill | 说明 |
|---|---|
| `skills/modern-r` | 自定义：R 代码现代化改造指南 |
| `skills/r-skill-changelog-sync` | 自定义：R 包 changelog 同步检查 |
