# Skill 来源与更新

本仓库中的每个 skill 都对应一个上游 GitHub 仓库。升级上游后，运行 `bash update-skills.sh` 即可把所有 skill 同步到最新版本。

- 映射数据文件：[SOURCES.tsv](./SOURCES.tsv)（供 `update-skills.sh` 读取）
- 一键更新脚本：[update-skills.sh](./update-skills.sh)
- 用法：`bash update-skills.sh` 全量同步；`bash update-skills.sh <skill名>` 只同步某个 skill

## 源仓库汇总

### https://github.com/posit-dev/skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/alt-text` | `main` | `alt-text` |  |
| `skills/brand-yml` | `main` | `brand-yml` |  |
| `skills/cli` | `main` | `r-lib/r-cli` |  |
| `skills/cran-extrachecks` | `main` | `r-lib/r-cran-extrachecks` |  |
| `skills/create-release-checklist` | `main` | `open-source/create-release-checklist` |  |
| `skills/critical-code-reviewer` | `main` | `posit-dev/critical-code-reviewer` |  |
| `skills/describe-design` | `main` | `posit-dev/describe-design` |  |
| `skills/ggsql` | `main` | `ggsql/ggsql` |  |
| `skills/implement` | `main` | `posit-dev/implement` |  |
| `skills/lifecycle` | `main` | `r-lib/r-lifecycle` |  |
| `skills/mirai` | `main` | `r-lib/r-mirai` |  |
| `skills/pr-create` | `main` | `github/pr-create` |  |
| `skills/pr-threads-address` | `main` | `github/pr-threads-address` |  |
| `skills/pr-threads-resolve` | `main` | `github/pr-threads-resolve` |  |
| `skills/quarto-authoring` | `main` | `quarto/quarto-authoring` |  |
| `skills/r-cli-app` | `main` | `r-lib/r-cli-app` |  |
| `skills/r-package-development` | `main` | `r-lib/r-package-development` |  |
| `skills/release-post` | `main` | `open-source/release-post` |  |
| `skills/shiny-bslib` | `main` | `shiny/shiny-bslib` |  |
| `skills/shiny-bslib-theming` | `main` | `shiny/shiny-bslib-theming` |  |
| `skills/testing-r-packages` | `main` | `r-lib/r-testthat` |  |
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

### CUSTOM

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/attach-db` | `CUSTOM` | `CUSTOM` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/duckdb-docs` | `CUSTOM` | `CUSTOM` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/install-duckdb` | `CUSTOM` | `CUSTOM` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/query` | `CUSTOM` | `CUSTOM` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/read-file` | `CUSTOM` | `CUSTOM` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/read-memories` | `CUSTOM` | `CUSTOM` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/kb-ops` | `CUSTOM` | `CUSTOM` | 本地知识库运维（自定义，无公开源） |
| `skills/gt-xlsx-roundtrip` | `CUSTOM` | `CUSTOM` | forgts + gtxlsx 在 Excel 与 gt 表格间往返转换（自定义，无公开源） |
| `skills/convert-file` | `CUSTOM` | `CUSTOM` | 格式转换，导入自 duckdb/duckdb-skills@7feda8e 并增补 DuckDB 2.0 |
| `skills/s3-explore` | `CUSTOM` | `CUSTOM` | 对象存储探索，导入自 duckdb/duckdb-skills@7feda8e 并增补 DuckDB 2.0 |
| `skills/spatial` | `CUSTOM` | `CUSTOM` | 空间数据，导入自 duckdb/duckdb-skills@7feda8e 并增补 DuckDB 2.0 |
| `skills/duckdb-2-0` | `CUSTOM` | `CUSTOM` | DuckDB 2.0 更新汇总、迁移与 agent mode 指南（自写） |
| `skills/nextflow-agents` | `CUSTOM` | `CUSTOM` | Nextflow agent 原语（docs.seqera.io/nextflow/agent 与官方示例整理，自写） |
| `skills/nf-core-agents-md` | `CUSTOM` | `CUSTOM` | nf-core 官方 AGENTS.md 规则（nf-core/agents，MIT）整理，自写 |
| `skills/nextflow-skills-guide` | `CUSTOM` | `CUSTOM` | Nextflow / nf-core 相关 skill 导航（自写） |

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

### https://github.com/vercel-labs/skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/find-skills` | `main` | `skills/find-skills` | skills.sh 官方（npx skills） |

### https://github.com/getkrafter/resume-toolkit

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/score` | `master` | `skills/score` | Krafter resume-toolkit |

### https://github.com/ailabs-393/ai-labs-claude-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/travel-planner` | `main` | `packages/skills/travel-planner` |  |

### https://github.com/lijigang/ljg-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/ljg-blind` | `master` | `skills/ljg-blind` |  |
| `skills/ljg-book` | `master` | `skills/ljg-book` |  |
| `skills/ljg-card` | `master` | `skills/ljg-card` |  |
| `skills/ljg-classic` | `master` | `skills/ljg-classic` |  |
| `skills/ljg-constraint` | `master` | `skills/ljg-constraint` |  |
| `skills/ljg-invest` | `master` | `skills/ljg-invest` |  |
| `skills/ljg-is` | `master` | `skills/ljg-is` |  |
| `skills/ljg-learn` | `master` | `skills/ljg-learn` |  |
| `skills/ljg-paper` | `master` | `skills/ljg-paper` |  |
| `skills/ljg-explain` | `master` | `skills/ljg-explain` |  |
| `skills/ljg-present` | `master` | `skills/ljg-present` |  |
| `skills/ljg-push` | `master` | `skills/ljg-push` |  |
| `skills/ljg-qa` | `master` | `skills/ljg-qa` |  |
| `skills/ljg-rank` | `master` | `skills/ljg-rank` |  |
| `skills/ljg-read` | `master` | `skills/ljg-read` |  |
| `skills/ljg-relationship` | `master` | `skills/ljg-relationship` |  |
| `skills/ljg-roundtable` | `master` | `skills/ljg-roundtable` |  |
| `skills/ljg-structure` | `master` | `skills/ljg-structure` |  |
| `skills/ljg-think` | `master` | `skills/ljg-think` |  |
| `skills/ljg-word` | `master` | `skills/ljg-word` |  |
| `skills/ljg-writes` | `master` | `skills/ljg-writes` |  |

### https://github.com/larashero3-dotcom/lieflat-charts

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/lieflat-charts` | `main` | `.` | 模板驱动数据可视化/报告生成 skill（moxt.ai） |

### https://github.com/cathrynlavery/diagram-design

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/diagram-design` | `main` | `skills/diagram-design` | Diagram Design（cathrynlavery，MIT） |

### https://github.com/zhjx19/ggplot2-pub

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/ggplot2-pub` | `main` | `.` | 出版级 ggplot2 作图 skill（zhjx19/ggplot2-pub，MIT） |

### https://github.com/AIScientists-Dev/academic-humanizer

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/academic-humanizer` | `main` | `.` | 学术写作与基金申请书的表达与语气润色（MIT） |

### https://github.com/taoyunudt/literature-review-skill

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/literature-review` | `main` | `.` | 文献综述写作 skill（taoyunudt，MIT） |

### https://github.com/cabbage2000-lab/paper-tutor-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/_shared` | `main` | `skills/_shared` | 学术辅导套件共享层（cabbage2000-lab，PolyForm Noncommercial 1.0.0） |
| `skills/paper-abstract` | `main` | `skills/paper-abstract` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-anchor` | `main` | `skills/paper-anchor` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-daily` | `main` | `skills/paper-daily` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-disclose` | `main` | `skills/paper-disclose` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-doctor` | `main` | `skills/paper-doctor` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-draft` | `main` | `skills/paper-draft` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-figure` | `main` | `skills/paper-figure` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-help` | `main` | `skills/paper-help` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-import` | `main` | `skills/paper-import` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-init` | `main` | `skills/paper-init` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-logic` | `main` | `skills/paper-logic` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-method` | `main` | `skills/paper-method` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-outline` | `main` | `skills/paper-outline` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-plot` | `main` | `skills/paper-plot` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-proposal` | `main` | `skills/paper-proposal` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-review` | `main` | `skills/paper-review` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-revise` | `main` | `skills/paper-revise` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-screen` | `main` | `skills/paper-screen` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-search` | `main` | `skills/paper-search` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-style` | `main` | `skills/paper-style` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-submit` | `main` | `skills/paper-submit` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-topic` | `main` | `skills/paper-topic` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-typeset` | `main` | `skills/paper-typeset` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |
| `skills/paper-verify` | `main` | `skills/paper-verify` | 学术辅导套件（cabbage2000-lab，PolyForm Noncommercial 1.0.0，仅非商业用途） |

### https://github.com/wtbxsjy/paper-knowledge

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/paper-knowledge-online` | `main` | `skills/paper-knowledge-online` | 论文参考→核验元数据→全文Markdown（CrossRef/arXiv+Sciverse 双源核对；PMC OA/arXiv 抓取，其余 PDF 经 MinerU 解析，MIT） |

### https://github.com/nextflow-io/agent-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `plugin-skills/nextflow-agent-skills/create-workflow` | `master` | `skills/create-workflow` |  |
| `plugin-skills/nextflow-agent-skills/install-nextflow` | `master` | `skills/install-nextflow` |  |
| `plugin-skills/nextflow-agent-skills/launch-workflow` | `master` | `skills/launch-workflow` |  |
| `plugin-skills/nextflow-agent-skills/migrate-nextflow-code` | `master` | `skills/migrate-nextflow-code` |  |
| `plugin-skills/nextflow-agent-skills/run-module` | `master` | `skills/run-module` |  |

### https://github.com/seqeralabs/nextflow-plugin

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `plugin-skills/seqera-nextflow-plugin/audit-conversion-readiness` | `main` | `skills/audit-conversion-readiness` |  |
| `plugin-skills/seqera-nextflow-plugin/build-nextflow-pipeline` | `main` | `skills/build-nextflow-pipeline` |  |
| `plugin-skills/seqera-nextflow-plugin/ce-credentials-setup` | `main` | `skills/ce-credentials-setup` |  |
| `plugin-skills/seqera-nextflow-plugin/create-container` | `main` | `skills/create-container` |  |
| `plugin-skills/seqera-nextflow-plugin/debug-local-run` | `main` | `skills/debug-local-run` |  |
| `plugin-skills/seqera-nextflow-plugin/debug-seqera-failed-run` | `main` | `skills/debug-seqera-failed-run` |  |
| `plugin-skills/seqera-nextflow-plugin/find-alternative-tools` | `main` | `skills/find-alternative-tools` |  |
| `plugin-skills/seqera-nextflow-plugin/install-nextflow` | `main` | `skills/install-nextflow` |  |
| `plugin-skills/seqera-nextflow-plugin/launch-workflow` | `main` | `skills/launch-workflow` |  |
| `plugin-skills/seqera-nextflow-plugin/maintain-nf-core-pipeline` | `main` | `skills/maintain-nf-core-pipeline` |  |
| `plugin-skills/seqera-nextflow-plugin/migrate-from-snakemake` | `main` | `skills/migrate-from-snakemake` |  |
| `plugin-skills/seqera-nextflow-plugin/migrate-nextflow-code` | `main` | `skills/migrate-nextflow-code` |  |
| `plugin-skills/seqera-nextflow-plugin/nextflow-config` | `main` | `skills/nextflow-config` |  |
| `plugin-skills/seqera-nextflow-plugin/nextflow-development` | `main` | `skills/nextflow-development` |  |
| `plugin-skills/seqera-nextflow-plugin/nextflow-history` | `main` | `skills/nextflow-history` |  |
| `plugin-skills/seqera-nextflow-plugin/nextflow-output-patterns` | `main` | `skills/nextflow-output-patterns` |  |
| `plugin-skills/seqera-nextflow-plugin/nextflow-schema` | `main` | `skills/nextflow-schema` |  |
| `plugin-skills/seqera-nextflow-plugin/nf-data-lineage` | `main` | `skills/nf-data-lineage` |  |
| `plugin-skills/seqera-nextflow-plugin/nf-docker-scripts` | `main` | `skills/nf-docker-scripts` |  |
| `plugin-skills/seqera-nextflow-plugin/nf-pipeline-design` | `main` | `skills/nf-pipeline-design` |  |
| `plugin-skills/seqera-nextflow-plugin/nf-plugin-development` | `main` | `skills/nf-plugin-development` |  |
| `plugin-skills/seqera-nextflow-plugin/nf-plugin-legacy-migration` | `main` | `skills/nf-plugin-legacy-migration` |  |
| `plugin-skills/seqera-nextflow-plugin/nf-test` | `main` | `skills/nf-test` |  |
| `plugin-skills/seqera-nextflow-plugin/repair-workflow` | `main` | `skills/repair-workflow` |  |
| `plugin-skills/seqera-nextflow-plugin/run-module` | `main` | `skills/run-module` |  |
| `plugin-skills/seqera-nextflow-plugin/search-existing-modules` | `main` | `skills/search-existing-modules` |  |
| `plugin-skills/seqera-nextflow-plugin/seqera-data-links` | `main` | `skills/seqera-data-links` |  |
| `plugin-skills/seqera-nextflow-plugin/seqerakit` | `main` | `skills/seqerakit` |  |

### https://github.com/edmundmiller/nf-core-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `plugin-skills/nf-core-skills/nf-core-lint` | `main` | `skills/nf-core-lint` |  |
| `plugin-skills/nf-core-skills/nf-core-pipeline` | `main` | `skills/nf-core-pipeline` |  |

### https://github.com/K-Dense-AI/claude-scientific-skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `plugin-skills/scientific-agent-skills/13c-metabolic-flux` | `main` | `skills/13c-metabolic-flux` |  |
| `plugin-skills/scientific-agent-skills/adaptyv` | `main` | `skills/adaptyv` |  |
| `plugin-skills/scientific-agent-skills/aeon` | `main` | `skills/aeon` |  |
| `plugin-skills/scientific-agent-skills/alphagenome` | `main` | `skills/alphagenome` |  |
| `plugin-skills/scientific-agent-skills/analytical-method-validation` | `main` | `skills/analytical-method-validation` |  |
| `plugin-skills/scientific-agent-skills/anndata` | `main` | `skills/anndata` |  |
| `plugin-skills/scientific-agent-skills/arbor` | `main` | `skills/arbor` |  |
| `plugin-skills/scientific-agent-skills/arboreto` | `main` | `skills/arboreto` |  |
| `plugin-skills/scientific-agent-skills/astropy` | `main` | `skills/astropy` |  |
| `plugin-skills/scientific-agent-skills/autoskill` | `main` | `skills/autoskill` |  |
| `plugin-skills/scientific-agent-skills/benchling-integration` | `main` | `skills/benchling-integration` |  |
| `plugin-skills/scientific-agent-skills/bgpt-paper-search` | `main` | `skills/bgpt-paper-search` |  |
| `plugin-skills/scientific-agent-skills/bids` | `main` | `skills/bids` |  |
| `plugin-skills/scientific-agent-skills/biopython` | `main` | `skills/biopython` |  |
| `plugin-skills/scientific-agent-skills/bioservices` | `main` | `skills/bioservices` |  |
| `plugin-skills/scientific-agent-skills/bulk-rnaseq` | `main` | `skills/bulk-rnaseq` |  |
| `plugin-skills/scientific-agent-skills/cantera` | `main` | `skills/cantera` |  |
| `plugin-skills/scientific-agent-skills/cellprofiler` | `main` | `skills/cellprofiler` |  |
| `plugin-skills/scientific-agent-skills/cellxgene-census` | `main` | `skills/cellxgene-census` |  |
| `plugin-skills/scientific-agent-skills/cirq` | `main` | `skills/cirq` |  |
| `plugin-skills/scientific-agent-skills/citation-management` | `main` | `skills/citation-management` |  |
| `plugin-skills/scientific-agent-skills/clinical-decision-support` | `main` | `skills/clinical-decision-support` |  |
| `plugin-skills/scientific-agent-skills/clinical-reports` | `main` | `skills/clinical-reports` |  |
| `plugin-skills/scientific-agent-skills/cobrapy` | `main` | `skills/cobrapy` |  |
| `plugin-skills/scientific-agent-skills/consciousness-council` | `main` | `skills/consciousness-council` |  |
| `plugin-skills/scientific-agent-skills/dask` | `main` | `skills/dask` |  |
| `plugin-skills/scientific-agent-skills/database-lookup` | `main` | `skills/database-lookup` |  |
| `plugin-skills/scientific-agent-skills/datalad` | `main` | `skills/datalad` |  |
| `plugin-skills/scientific-agent-skills/datamol` | `main` | `skills/datamol` |  |
| `plugin-skills/scientific-agent-skills/deepchem` | `main` | `skills/deepchem` |  |
| `plugin-skills/scientific-agent-skills/deepspot-m` | `main` | `skills/deepspot-m` |  |
| `plugin-skills/scientific-agent-skills/deeptools` | `main` | `skills/deeptools` |  |
| `plugin-skills/scientific-agent-skills/depmap` | `main` | `skills/depmap` |  |
| `plugin-skills/scientific-agent-skills/dhdna-profiler` | `main` | `skills/dhdna-profiler` |  |
| `plugin-skills/scientific-agent-skills/diffdock` | `main` | `skills/diffdock` |  |
| `plugin-skills/scientific-agent-skills/dnanexus-integration` | `main` | `skills/dnanexus-integration` |  |
| `plugin-skills/scientific-agent-skills/esm` | `main` | `skills/esm` |  |
| `plugin-skills/scientific-agent-skills/etetoolkit` | `main` | `skills/etetoolkit` |  |
| `plugin-skills/scientific-agent-skills/exa-search` | `main` | `skills/exa-search` |  |
| `plugin-skills/scientific-agent-skills/experimental-design` | `main` | `skills/experimental-design` |  |
| `plugin-skills/scientific-agent-skills/exploratory-data-analysis` | `main` | `skills/exploratory-data-analysis` |  |
| `plugin-skills/scientific-agent-skills/fictiv` | `main` | `skills/fictiv` |  |
| `plugin-skills/scientific-agent-skills/flowio` | `main` | `skills/flowio` |  |
| `plugin-skills/scientific-agent-skills/flowkit` | `main` | `skills/flowkit` |  |
| `plugin-skills/scientific-agent-skills/fluidsim` | `main` | `skills/fluidsim` |  |
| `plugin-skills/scientific-agent-skills/folklore-variant-evidence` | `main` | `skills/folklore-variant-evidence` |  |
| `plugin-skills/scientific-agent-skills/generate-image` | `main` | `skills/generate-image` |  |
| `plugin-skills/scientific-agent-skills/geniml` | `main` | `skills/geniml` |  |
| `plugin-skills/scientific-agent-skills/genomic-coordinates` | `main` | `skills/genomic-coordinates` |  |
| `plugin-skills/scientific-agent-skills/genomic-intelligence` | `main` | `skills/genomic-intelligence` |  |
| `plugin-skills/scientific-agent-skills/geomaster` | `main` | `skills/geomaster` |  |
| `plugin-skills/scientific-agent-skills/geopandas` | `main` | `skills/geopandas` |  |
| `plugin-skills/scientific-agent-skills/get-available-resources` | `main` | `skills/get-available-resources` |  |
| `plugin-skills/scientific-agent-skills/gget` | `main` | `skills/gget` |  |
| `plugin-skills/scientific-agent-skills/ginkgo-cloud-lab` | `main` | `skills/ginkgo-cloud-lab` |  |
| `plugin-skills/scientific-agent-skills/glycoengineering` | `main` | `skills/glycoengineering` |  |
| `plugin-skills/scientific-agent-skills/gtars` | `main` | `skills/gtars` |  |
| `plugin-skills/scientific-agent-skills/histolab` | `main` | `skills/histolab` |  |
| `plugin-skills/scientific-agent-skills/hugging-science` | `main` | `skills/hugging-science` |  |
| `plugin-skills/scientific-agent-skills/hypogenic` | `main` | `skills/hypogenic` |  |
| `plugin-skills/scientific-agent-skills/hypothesis-generation` | `main` | `skills/hypothesis-generation` |  |
| `plugin-skills/scientific-agent-skills/imaging-data-commons` | `main` | `skills/imaging-data-commons` |  |
| `plugin-skills/scientific-agent-skills/infographics` | `main` | `skills/infographics` |  |
| `plugin-skills/scientific-agent-skills/iso-standards-readiness` | `main` | `skills/iso-standards-readiness` |  |
| `plugin-skills/scientific-agent-skills/lab-hardware-cad` | `main` | `skills/lab-hardware-cad` |  |
| `plugin-skills/scientific-agent-skills/labarchive-integration` | `main` | `skills/labarchive-integration` |  |
| `plugin-skills/scientific-agent-skills/lamindb` | `main` | `skills/lamindb` |  |
| `plugin-skills/scientific-agent-skills/latchbio-integration` | `main` | `skills/latchbio-integration` |  |
| `plugin-skills/scientific-agent-skills/latex-posters` | `main` | `skills/latex-posters` |  |
| `plugin-skills/scientific-agent-skills/liteparse` | `main` | `skills/liteparse` |  |
| `plugin-skills/scientific-agent-skills/literature-review` | `main` | `skills/literature-review` |  |
| `plugin-skills/scientific-agent-skills/mageck` | `main` | `skills/mageck` |  |
| `plugin-skills/scientific-agent-skills/marine-carbonate-chemistry` | `main` | `skills/marine-carbonate-chemistry` |  |
| `plugin-skills/scientific-agent-skills/markdown-mermaid-writing` | `main` | `skills/markdown-mermaid-writing` |  |
| `plugin-skills/scientific-agent-skills/market-research-reports` | `main` | `skills/market-research-reports` |  |
| `plugin-skills/scientific-agent-skills/markitdown` | `main` | `skills/markitdown` |  |
| `plugin-skills/scientific-agent-skills/matchms` | `main` | `skills/matchms` |  |
| `plugin-skills/scientific-agent-skills/matlab` | `main` | `skills/matlab` |  |
| `plugin-skills/scientific-agent-skills/matplotlib` | `main` | `skills/matplotlib` |  |
| `plugin-skills/scientific-agent-skills/medchem` | `main` | `skills/medchem` |  |
| `plugin-skills/scientific-agent-skills/modal` | `main` | `skills/modal` |  |
| `plugin-skills/scientific-agent-skills/molecular-dynamics` | `main` | `skills/molecular-dynamics` |  |
| `plugin-skills/scientific-agent-skills/molfeat` | `main` | `skills/molfeat` |  |
| `plugin-skills/scientific-agent-skills/ncats-arax` | `main` | `skills/ncats-arax` |  |
| `plugin-skills/scientific-agent-skills/networkx` | `main` | `skills/networkx` |  |
| `plugin-skills/scientific-agent-skills/neurokit2` | `main` | `skills/neurokit2` |  |
| `plugin-skills/scientific-agent-skills/neuropixels-analysis` | `main` | `skills/neuropixels-analysis` |  |
| `plugin-skills/scientific-agent-skills/nextflow` | `main` | `skills/nextflow` |  |
| `plugin-skills/scientific-agent-skills/nmrglue` | `main` | `skills/nmrglue` |  |
| `plugin-skills/scientific-agent-skills/nwb-conversion` | `main` | `skills/nwb-conversion` |  |
| `plugin-skills/scientific-agent-skills/omero-integration` | `main` | `skills/omero-integration` |  |
| `plugin-skills/scientific-agent-skills/onekgpd` | `main` | `skills/onekgpd` |  |
| `plugin-skills/scientific-agent-skills/ontology-term-resolution` | `main` | `skills/ontology-term-resolution` |  |
| `plugin-skills/scientific-agent-skills/open-notebook` | `main` | `skills/open-notebook` |  |
| `plugin-skills/scientific-agent-skills/openpiv` | `main` | `skills/openpiv` |  |
| `plugin-skills/scientific-agent-skills/opentrons-integration` | `main` | `skills/opentrons-integration` |  |
| `plugin-skills/scientific-agent-skills/optimize-for-gpu` | `main` | `skills/optimize-for-gpu` |  |
| `plugin-skills/scientific-agent-skills/pacsomatic` | `main` | `skills/pacsomatic` |  |
| `plugin-skills/scientific-agent-skills/paper-lookup` | `main` | `skills/paper-lookup` |  |
| `plugin-skills/scientific-agent-skills/paperclip` | `main` | `skills/paperclip` |  |
| `plugin-skills/scientific-agent-skills/paperzilla` | `main` | `skills/paperzilla` |  |
| `plugin-skills/scientific-agent-skills/parallel-web` | `main` | `skills/parallel-web` |  |
| `plugin-skills/scientific-agent-skills/pathml` | `main` | `skills/pathml` |  |
| `plugin-skills/scientific-agent-skills/pathogen-variant-surveillance` | `main` | `skills/pathogen-variant-surveillance` |  |
| `plugin-skills/scientific-agent-skills/pathway-enrichment` | `main` | `skills/pathway-enrichment` |  |
| `plugin-skills/scientific-agent-skills/peer-review` | `main` | `skills/peer-review` |  |
| `plugin-skills/scientific-agent-skills/pennylane` | `main` | `skills/pennylane` |  |
| `plugin-skills/scientific-agent-skills/phylogenetics` | `main` | `skills/phylogenetics` |  |
| `plugin-skills/scientific-agent-skills/pi-agent` | `main` | `skills/pi-agent` |  |
| `plugin-skills/scientific-agent-skills/pkpd-modeling` | `main` | `skills/pkpd-modeling` |  |
| `plugin-skills/scientific-agent-skills/polars` | `main` | `skills/polars` |  |
| `plugin-skills/scientific-agent-skills/polars-bio` | `main` | `skills/polars-bio` |  |
| `plugin-skills/scientific-agent-skills/pptx-posters` | `main` | `skills/pptx-posters` |  |
| `plugin-skills/scientific-agent-skills/primekg` | `main` | `skills/primekg` |  |
| `plugin-skills/scientific-agent-skills/primer-design` | `main` | `skills/primer-design` |  |
| `plugin-skills/scientific-agent-skills/protocolsio-integration` | `main` | `skills/protocolsio-integration` |  |
| `plugin-skills/scientific-agent-skills/pufferlib` | `main` | `skills/pufferlib` |  |
| `plugin-skills/scientific-agent-skills/pybamm` | `main` | `skills/pybamm` |  |
| `plugin-skills/scientific-agent-skills/pycalphad` | `main` | `skills/pycalphad` |  |
| `plugin-skills/scientific-agent-skills/pydeseq2` | `main` | `skills/pydeseq2` |  |
| `plugin-skills/scientific-agent-skills/pydicom` | `main` | `skills/pydicom` |  |
| `plugin-skills/scientific-agent-skills/pyhealth` | `main` | `skills/pyhealth` |  |
| `plugin-skills/scientific-agent-skills/pylabrobot` | `main` | `skills/pylabrobot` |  |
| `plugin-skills/scientific-agent-skills/pymatgen` | `main` | `skills/pymatgen` |  |
| `plugin-skills/scientific-agent-skills/pymc` | `main` | `skills/pymc` |  |
| `plugin-skills/scientific-agent-skills/pymoo` | `main` | `skills/pymoo` |  |
| `plugin-skills/scientific-agent-skills/pyopenms` | `main` | `skills/pyopenms` |  |
| `plugin-skills/scientific-agent-skills/pysam` | `main` | `skills/pysam` |  |
| `plugin-skills/scientific-agent-skills/pytdc` | `main` | `skills/pytdc` |  |
| `plugin-skills/scientific-agent-skills/pytorch-lightning` | `main` | `skills/pytorch-lightning` |  |
| `plugin-skills/scientific-agent-skills/pyzotero` | `main` | `skills/pyzotero` |  |
| `plugin-skills/scientific-agent-skills/qiime2-amplicon` | `main` | `skills/qiime2-amplicon` |  |
| `plugin-skills/scientific-agent-skills/qiskit` | `main` | `skills/qiskit` |  |
| `plugin-skills/scientific-agent-skills/qutip` | `main` | `skills/qutip` |  |
| `plugin-skills/scientific-agent-skills/rdkit` | `main` | `skills/rdkit` |  |
| `plugin-skills/scientific-agent-skills/relion` | `main` | `skills/relion` |  |
| `plugin-skills/scientific-agent-skills/relsa-severity-assessment` | `main` | `skills/relsa-severity-assessment` |  |
| `plugin-skills/scientific-agent-skills/research-grants` | `main` | `skills/research-grants` |  |
| `plugin-skills/scientific-agent-skills/research-lookup` | `main` | `skills/research-lookup` |  |
| `plugin-skills/scientific-agent-skills/rowan` | `main` | `skills/rowan` |  |
| `plugin-skills/scientific-agent-skills/scanpy` | `main` | `skills/scanpy` |  |
| `plugin-skills/scientific-agent-skills/scholar-evaluation` | `main` | `skills/scholar-evaluation` |  |
| `plugin-skills/scientific-agent-skills/scientific-brainstorming` | `main` | `skills/scientific-brainstorming` |  |
| `plugin-skills/scientific-agent-skills/scientific-critical-thinking` | `main` | `skills/scientific-critical-thinking` |  |
| `plugin-skills/scientific-agent-skills/scientific-schematics` | `main` | `skills/scientific-schematics` |  |
| `plugin-skills/scientific-agent-skills/scientific-slides` | `main` | `skills/scientific-slides` |  |
| `plugin-skills/scientific-agent-skills/scientific-visualization` | `main` | `skills/scientific-visualization` |  |
| `plugin-skills/scientific-agent-skills/scientific-writing` | `main` | `skills/scientific-writing` |  |
| `plugin-skills/scientific-agent-skills/scikit-bio` | `main` | `skills/scikit-bio` |  |
| `plugin-skills/scientific-agent-skills/scikit-learn` | `main` | `skills/scikit-learn` |  |
| `plugin-skills/scientific-agent-skills/scikit-survival` | `main` | `skills/scikit-survival` |  |
| `plugin-skills/scientific-agent-skills/scvelo` | `main` | `skills/scvelo` |  |
| `plugin-skills/scientific-agent-skills/scvi-tools` | `main` | `skills/scvi-tools` |  |
| `plugin-skills/scientific-agent-skills/seaborn` | `main` | `skills/seaborn` |  |
| `plugin-skills/scientific-agent-skills/shap` | `main` | `skills/shap` |  |
| `plugin-skills/scientific-agent-skills/simpy` | `main` | `skills/simpy` |  |
| `plugin-skills/scientific-agent-skills/stable-baselines3` | `main` | `skills/stable-baselines3` |  |
| `plugin-skills/scientific-agent-skills/statistical-analysis` | `main` | `skills/statistical-analysis` |  |
| `plugin-skills/scientific-agent-skills/statistical-power` | `main` | `skills/statistical-power` |  |
| `plugin-skills/scientific-agent-skills/statsmodels` | `main` | `skills/statsmodels` |  |
| `plugin-skills/scientific-agent-skills/sympy` | `main` | `skills/sympy` |  |
| `plugin-skills/scientific-agent-skills/tamarind` | `main` | `skills/tamarind` |  |
| `plugin-skills/scientific-agent-skills/tellurium` | `main` | `skills/tellurium` |  |
| `plugin-skills/scientific-agent-skills/tiledbvcf` | `main` | `skills/tiledbvcf` |  |
| `plugin-skills/scientific-agent-skills/timesfm-forecasting` | `main` | `skills/timesfm-forecasting` |  |
| `plugin-skills/scientific-agent-skills/torch-geometric` | `main` | `skills/torch-geometric` |  |
| `plugin-skills/scientific-agent-skills/torchdrug` | `main` | `skills/torchdrug` |  |
| `plugin-skills/scientific-agent-skills/transformers` | `main` | `skills/transformers` |  |
| `plugin-skills/scientific-agent-skills/treatment-plans` | `main` | `skills/treatment-plans` |  |
| `plugin-skills/scientific-agent-skills/umap-learn` | `main` | `skills/umap-learn` |  |
| `plugin-skills/scientific-agent-skills/uncertainty-and-units` | `main` | `skills/uncertainty-and-units` |  |
| `plugin-skills/scientific-agent-skills/usfiscaldata` | `main` | `skills/usfiscaldata` |  |
| `plugin-skills/scientific-agent-skills/vaex` | `main` | `skills/vaex` |  |
| `plugin-skills/scientific-agent-skills/venue-templates` | `main` | `skills/venue-templates` |  |
| `plugin-skills/scientific-agent-skills/waypoint-bio` | `main` | `skills/waypoint-bio` |  |
| `plugin-skills/scientific-agent-skills/what-if-oracle` | `main` | `skills/what-if-oracle` |  |
| `plugin-skills/scientific-agent-skills/zarr-python` | `main` | `skills/zarr-python` |  |

### https://github.com/HKUSTDial/Supervisor-Skills

| 本仓库目录 | 上游分支 | 上游路径 | 备注 |
|---|---|---|---|
| `skills/benchmark-paper-template` | `main` | `skills/benchmark-paper-template` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/deep-research` | `main` | `skills/deep-research` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/figure-designer` | `main` | `skills/figure-designer` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/idea-evaluator` | `main` | `skills/idea-evaluator` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/intro-drafter` | `main` | `skills/intro-drafter` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/paper-polish` | `main` | `skills/paper-polish` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/paper-writer` | `main` | `skills/paper-writer` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/pre-submission-reviewer` | `main` | `skills/pre-submission-reviewer` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/rebuttal-guidance` | `main` | `skills/rebuttal-guidance` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/tech-paper-template` | `main` | `skills/tech-paper-template` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/vibe-research-workflow` | `main` | `skills/vibe-research-workflow` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |
| `skills/drawio-reconstruction` | `main` | `skills/drawio-reconstruction` | CC BY-NC-SA 4.0，description 已按本仓库规范精简，见 licenses/Supervisor-Skills-NOTICE.md |

## 自定义 Skill（无公开源，不参与自动更新）

| Skill | 说明 |
|---|---|
| `skills/modern-r` | 自定义：R 代码现代化改造指南 |
| `skills/r-skill-changelog-sync` | 自定义：R 包 changelog 同步检查 |
| `skills/kb-ops` | 自定义：本地知识库运维（kb-template 脚手架） |
| `skills/gt-xlsx-roundtrip` | 自定义：forgts + gtxlsx 在 Excel 与 gt 表格间往返转换 |
| `skills/attach-db` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/duckdb-docs` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/install-duckdb` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/query` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/read-file` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/read-memories` | 派生自 duckdb/duckdb-skills@7feda8e，增补 DuckDB 2.0（agent mode 等） |
| `skills/convert-file` | 导入自 duckdb/duckdb-skills@7feda8e 并增补 DuckDB 2.0 |
| `skills/s3-explore` | 导入自 duckdb/duckdb-skills@7feda8e 并增补 DuckDB 2.0 |
| `skills/spatial` | 导入自 duckdb/duckdb-skills@7feda8e 并增补 DuckDB 2.0 |
| `skills/duckdb-2-0` | 自定义：DuckDB 2.0 更新汇总、迁移与 agent mode 指南 |
| `skills/nextflow-agents` | 自定义：Nextflow agent 原语（docs.seqera.io/nextflow/agent 与官方示例整理） |
| `skills/nf-core-agents-md` | 自定义：nf-core 官方 AGENTS.md 规则（nf-core/agents，MIT）整理 |
| `skills/nextflow-skills-guide` | 自定义：Nextflow / nf-core 相关 skill 导航 |
