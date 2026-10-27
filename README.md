<h1 align="center">My Claude Code Skills</h1>

<p align="center">
  Claude Code 环境 Skills / Plugins / Settings / Hooks 统一管理仓库 · 全部 skill 可一键从上游同步更新
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>
  <img src="https://img.shields.io/github/stars/wtbxsjy/my_skills?style=flat-square&label=Stars" alt="Stars">
  <img src="https://img.shields.io/github/license/wtbxsjy/my_skills?style=flat-square" alt="License">
</p>

---

## Contents

- [快速开始](#快速开始)
- [Skill Library](#skill-library)
  - [R / Tidyverse / Bioconductor](#r-tidyverse-bioconductor)
  - [Quarto / 发布与写作](#quarto-发布与写作)
  - [数据科学 / 机器学习 / 数据查询](#数据科学-机器学习-数据查询)
  - [生物医药 / 文献数据库](#生物医药-文献数据库)
  - [开发 / 工程 / 工作流](#开发-工程-工作流)
  - [Nextflow / nf-core 工作流](#nextflow-nf-core-工作流)
  - [科学研究 Agent Skills（K-Dense）](#科学研究-agent-skillsk-dense)
  - [前端 / 设计](#前端-设计)
  - [图表 / 可视化](#图表-可视化)
  - [文档 / 办公](#文档-办公)
  - [学术写作 / 文献综述](#学术写作-文献综述)
  - [知识管理 / Obsidian](#知识管理-obsidian)
  - [个人技能集（ljg-*）](#个人技能集ljg-)
  - [Meta / 效率工具](#meta-效率工具)
  - [插件附带 Skills](#插件附带-skills)
  - [自定义 Skills（无公开源）](#自定义-skills无公开源)
- [Skill 来源与更新](#skill-来源与更新)
- [多环境同步策略](#多环境同步策略)
- [Contributing](#contributing)

---

## 快速开始

在新机器上同步环境：

```bash
git clone https://github.com/wtbxsjy/my_skills.git
cd my_skills
bash setup.sh        # Linux / macOS（Windows 用 setup.ps1）
```

## Skill Library

### R / Tidyverse / Bioconductor

| Skill | 描述 | 来源 |
|---|---|---|
| [**add-dials-parameter**](https://github.com/tidymodels/skills/tree/main/developers/add-dials-parameter) | Guide for creating new dials parameters for hyperparameter tuning. | tidymodels/skills |
| [**add-parsnip-engine**](https://github.com/tidymodels/skills/tree/main/developers/add-parsnip-engine) | Add new computational engines to existing parsnip models. Use when | tidymodels/skills |
| [**add-parsnip-model**](https://github.com/tidymodels/skills/tree/main/developers/add-parsnip-model) | Create entirely new model specifications for the parsnip package. | tidymodels/skills |
| [**add-recipe-step**](https://github.com/tidymodels/skills/tree/main/developers/add-recipe-step) | Create a new preprocessing step for the recipes package following | tidymodels/skills |
| [**add-yardstick-metric**](https://github.com/tidymodels/skills/tree/main/developers/add-yardstick-metric) | Guide for creating new yardstick metrics. Use when a developer | tidymodels/skills |
| [**cli**](https://github.com/posit-dev/skills/tree/main/r-lib/r-cli) | Style R command-line output with the cli package: inline markup and color, cli_abort/cli_warn/cli_inform, progress bars,... | posit-dev/skills |
| [**cran-extrachecks**](https://github.com/posit-dev/skills/tree/main/r-lib/r-cran-extrachecks) | Prepare an R package for CRAN submission: catch ad-hoc requirements devtools::check() misses — documentation, DESCRIPTION fields, URLs, examples,... | posit-dev/skills |
| [**create-release-checklist**](https://github.com/posit-dev/skills/tree/main/open-source/create-release-checklist) | Create a release checklist and GitHub issue for an R package. Use when the user asks to "create a release checklist" or "start a release" for an R... | posit-dev/skills |
| [**gt-xlsx-roundtrip**](./skills/gt-xlsx-roundtrip) | 在带格式的 Excel 电子表格（.xlsx）与 R 语言 gt 表格对象之间双向转换，使用 forgts（电子表格 → gt）和 gtxlsx（gt → 电子表格）。... | 自定义 |
| [**lifecycle**](https://github.com/posit-dev/skills/tree/main/r-lib/r-lifecycle) | Manage R package lifecycle with the lifecycle package: deprecate or rename functions and arguments, supersede, mark experimental,... | posit-dev/skills |
| [**mirai**](https://github.com/posit-dev/skills/tree/main/r-lib/r-mirai) | Help users write correct R code for async, parallel, and distributed computing using mirai.... | posit-dev/skills |
| [**r-bayes**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-bayes) | Patterns for Bayesian inference in R using brms, including multilevel models, DAG validation, and marginal effects.... | ab604/claude-code-r-skills |
| [**r-cli-app**](https://github.com/posit-dev/skills/tree/main/r-lib/r-cli-app) | Build command-line apps in R using the Rapp package. Use when creating a CLI tool in R, adding argument parsing to an R script,... | posit-dev/skills |
| [**r-oop**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-oop) | R object-oriented programming guide for S7, S3, S4, and vctrs. Use when designing R classes or choosing an OOP system. | ab604/claude-code-r-skills |
| [**r-package-development**](https://github.com/posit-dev/skills/tree/main/r-lib/r-package-development) | R package development with devtools, testthat, and roxygen2. Use when the user is working on an R package, running tests, writing documentation,... | posit-dev/skills |
| [**r-performance**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-performance) | R performance best practices including profiling, benchmarking, vctrs, and optimization strategies. Use when optimizing R code. | ab604/claude-code-r-skills |
| [**r-style-guide**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-style-guide) | R style guide covering naming conventions, spacing, layout, and function design best practices. Use when writing R code. | ab604/claude-code-r-skills |
| [**release-post**](https://github.com/posit-dev/skills/tree/main/open-source/release-post) | Write package release blog posts in Tidyverse (hugodown) or Shiny (Quarto) style: turn NEWS/changelog into a release announcement,... | posit-dev/skills |
| [**rlang-patterns**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/rlang-patterns) | rlang metaprogramming patterns for data-masking, injection operators, and dynamic dots. Use when writing functions that use tidy evaluation. | ab604/claude-code-r-skills |
| [**shiny-bslib**](https://github.com/posit-dev/skills/tree/main/shiny/shiny-bslib) | Build modern Shiny dashboards with bslib (Bootstrap 5): page layouts, grid, cards, value boxes, nav, sidebars, filling layouts, theming,... | posit-dev/skills |
| [**shiny-bslib-theming**](https://github.com/posit-dev/skills/tree/main/shiny/shiny-bslib-theming) | Advanced theming for Shiny apps using bslib and Bootstrap 5. Use when customizing app appearance with bs_theme(), Bootswatch themes, custom colors,... | posit-dev/skills |
| [**tdd-workflow**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/tdd-workflow) | Test-driven development workflow for R using testthat. Use when writing new features, fixing bugs, or refactoring code.... | ab604/claude-code-r-skills |
| [**testing-r-packages**](https://github.com/posit-dev/skills/tree/main/r-lib/r-testthat) | Best practices for writing R package tests with testthat version 3+.... | posit-dev/skills |
| [**tidyverse-patterns**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/tidyverse-patterns) | Modern tidyverse patterns for R including pipes, joins, grouping, purrr, and stringr. Use when writing tidyverse R code. | ab604/claude-code-r-skills |

### Quarto / 发布与写作

| Skill | 描述 | 来源 |
|---|---|---|
| [**academic-humanizer**](https://github.com/AIScientists-Dev/academic-humanizer) | Improve clarity and voice of AI-assisted academic writing and grant proposals: preserve scholarly conventions,... | AIScientists-Dev/academic-humanizer |
| [**alt-text**](https://github.com/posit-dev/skills/tree/main/alt-text) | Generate and improve accessible alt text for data visualizations and images in R packages and Quarto documents. Use when the user wants to add,... | posit-dev/skills |
| [**brand-yml**](https://github.com/posit-dev/skills/tree/main/brand-yml) | Create and use brand.yml files for consistent branding across Shiny apps and Quarto documents. Covers: (1) Creating new _brand.yml files,... | posit-dev/skills |
| [**quarto-alt-text**](https://github.com/ai-integr8tor/posit-dev-skills/tree/add-py-shiny-dashboard-skills/quarto/quarto-alt-text) | Generate accessible alt text for data visualizations in Quarto documents. Use when the user wants to add, improve,... | ai-integr8tor/posit-dev-skills |
| [**quarto-authoring**](https://github.com/posit-dev/skills/tree/main/quarto/quarto-authoring) | Work with Quarto: .qmd files, _quarto.yml, projects, callouts, cross-references, citations, Mermaid, extensions, websites, books,... | posit-dev/skills |
| [**quarto-talks**](https://github.com/alfredo-hs/quarto-talks) | Turn source material into a restrained Quarto RevealJS talk using the quarto-talks format. Use for papers, manuscripts, documents, figures, code,... | alfredo-hs/quarto-talks |

### 数据科学 / 机器学习 / 数据查询

| Skill | 描述 | 来源 |
|---|---|---|
| [**attach-db**](./skills/attach-db) | Attach a DuckDB database file for use with /duckdb-skills:query. Explores the schema (tables, columns,... | 自定义 |
| [**convert-file**](./skills/convert-file) | Convert any data file to another format: CSV, Parquet, JSON, Excel, GeoJSON, and more. Use when the user says "convert to parquet", "save as xlsx",... | 自定义 |
| [**duckdb-2-0**](./skills/duckdb-2-0) | DuckDB 2.0 (LTS) for agents: check version, use CLI agent mode (compact output, result caps, JSON errors), migrate from 1.x (storage v69,... | 自定义 |
| [**duckdb-docs**](./skills/duckdb-docs) | Search DuckDB and DuckLake documentation and blog posts. Returns relevant doc chunks for a question or keyword using full-text search against a loc... | 自定义 |
| [**ggsql**](https://github.com/posit-dev/skills/tree/main/ggsql/ggsql) | Write ggsql queries — a grammar of graphics for SQL. Use when the user wants to create, modify, or understand a ggsql visualization query. | posit-dev/skills |
| [**install-duckdb**](./skills/install-duckdb) | Install or update DuckDB extensions. Each argument is either a plain extension name (installs from core) or name@repo (e.g. magic@community).... | 自定义 |
| [**query**](./skills/query) | Run SQL queries against the attached DuckDB database or ad-hoc against files. Accepts raw SQL or natural language questions.... | 自定义 |
| [**read-file**](./skills/read-file) | Read any data file (CSV, JSON, Parquet, Avro, Excel, spatial, SQLite) or remote URL (S3, HTTPS). Use when user references a data file,... | 自定义 |
| [**read-memories**](./skills/read-memories) | Search past Claude Code session logs to recall prior decisions, patterns, or unresolved work. Use when user says "do you remember",... | 自定义 |
| [**s3-explore**](./skills/s3-explore) | Explore and query data on S3, Cloudflare R2, GCS, MinIO, or any S3-compatible storage. Use when the user mentions an s3://, r2://, gs://,... | 自定义 |
| [**scvi-tools**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scvi-tools) | Deep-learning single-cell analysis with scvi-tools: scVI/scANVI integration, PeakVI (ATAC), totalVI (CITE-seq), MultiVI (multiome),... | anthropics/knowledge-work-plugins |
| [**single-cell-rna-qc**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/single-cell-rna-qc) | Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive v... | anthropics/knowledge-work-plugins |
| [**spatial**](./skills/spatial) | Answer spatial questions with DuckDB: coordinates, distances, maps, addresses, near/within/closest,... | 自定义 |
| [**tabular-data-ml**](https://github.com/tidymodels/skills/tree/main/users/tabular-data-ml) | Build machine learning models using tidymodels for tabular data | tidymodels/skills |

### 生物医药 / 文献数据库

| Skill | 描述 | 来源 |
|---|---|---|
| [**alphafold-database-fetch-and-analyze**](https://github.com/google-deepmind/science-skills/tree/main/skills/alphafold_database_fetch_and_analyze) | Retrieve and analyze AlphaFold predicted structures for a protein.... | google-deepmind/science-skills |
| [**alphagenome-single-variant-analysis**](https://github.com/google-deepmind/science-skills/tree/main/skills/alphagenome_single_variant_analysis) | Analyze genetic variant effects with the AlphaGenome API: expression, chromatin accessibility,... | google-deepmind/science-skills |
| [**chembl-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/chembl_database) | Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved drugs, and chemical structures.... | google-deepmind/science-skills |
| [**clinical-trials-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/clinical_trials_database) | Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by condition, drug, location, status,... | google-deepmind/science-skills |
| [**clinvar-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/clinvar_database) | Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Benign, VUS), clinical evidence rationales,... | google-deepmind/science-skills |
| [**credentials**](https://github.com/google-deepmind/science-skills/tree/main/skills/credentials) | Instructions for handling API keys and credentials safely, verifying their presence,... | google-deepmind/science-skills |
| [**dbsnp-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/dbsnp_database) | Use when you want to look up, map, and search for short genetic variants (SNPs, indels) in NCBI's dbSNP database. Resolves between rsIDs,... | google-deepmind/science-skills |
| [**embl-ebi-ols**](https://github.com/google-deepmind/science-skills/tree/main/skills/embl_ebi_ols) | Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, definitions,... | google-deepmind/science-skills |
| [**encode-ccres-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/encode_ccres_database) | Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API,... | google-deepmind/science-skills |
| [**ensembl-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/ensembl_database) | Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or protein sequences, retrieve gene structures (exons),... | google-deepmind/science-skills |
| [**foldseek-structural-search**](https://github.com/google-deepmind/science-skills/tree/main/skills/foldseek_structural_search) | Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API.... | google-deepmind/science-skills |
| [**gnomad-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/gnomad_database) | Query gnomAD: variant rarity and allele frequency, gene constraint (pLI, LOEUF), variants in a region or gene, structural variants.... | google-deepmind/science-skills |
| [**gtex-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/gtex_database) | Use when you want to retrieve quantitative RNA expression data and variant eQTL information from the GTEx (Genotype-Tissue Expression) Project acro... | google-deepmind/science-skills |
| [**human-protein-atlas-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/human_protein_atlas_database) | Use when you want to retrieve semi-quantitative protein expression and spatial localisation data from the Human Protein Atlas (HPA). | google-deepmind/science-skills |
| [**interpro-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/interpro_database) | Find protein domains, families and sites; list proteins in a family or sharing a domain; species distribution; annotate genomes with InterPro/Pfam... | google-deepmind/science-skills |
| [**jaspar-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/jaspar_database) | Query the JASPAR database for Transcription Factor (TF) binding profiles.... | google-deepmind/science-skills |
| [**literature-search-arxiv**](https://github.com/google-deepmind/science-skills/tree/main/skills/literature_search_arxiv) | Search for scientific papers, preprints, and publications on arXiv. Extract metadata, abstracts,... | google-deepmind/science-skills |
| [**literature-search-biorxiv**](https://github.com/google-deepmind/science-skills/tree/main/skills/literature_search_biorxiv) | Browse, filter, and download life sciences, biology, and medical preprints from bioRxiv and medRxiv. Supports fetching paper metadata by DOI,... | google-deepmind/science-skills |
| [**literature-search-europepmc**](https://github.com/google-deepmind/science-skills/tree/main/skills/literature_search_europepmc) | Search Europe PMC for scientific literature and download open-access full texts and PDFs. Retrieve full-text XML/plain text by PMCID,... | google-deepmind/science-skills |
| [**literature-search-openalex**](https://github.com/google-deepmind/science-skills/tree/main/skills/literature_search_openalex) | Query the OpenAlex scholarly database for research papers, authors, institutions, topics, sources, publishers, funders, geo-locations,... | google-deepmind/science-skills |
| [**ncbi-sequence-fetch**](https://github.com/google-deepmind/science-skills/tree/main/skills/ncbi_sequence_fetch) | Retrieve protein and nucleotide sequences from NCBI databases using E-utilities. Supports direct accession lookup, CDS translation,... | google-deepmind/science-skills |
| [**openfda-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/openfda_database) | Query, search, and download data from the openFDA API for drugs, devices, foods, tobacco, cosmetics, animal and veterinary products, substances,... | google-deepmind/science-skills |
| [**opentargets-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/opentargets_database) | Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs,... | google-deepmind/science-skills |
| [**pdb-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/pdb_database) | Use when you want to search for or download experimentally-determined 3D structures for biomolecules (proteins, nucleic acids, bound ligands).... | google-deepmind/science-skills |
| [**predictingthepast**](https://github.com/google-deepmind/science-skills/tree/main/skills/predictingthepast) | Ancient text restoration, attribution, dating, contextualization, and embedding via Aeneas (Latin) / Ithaca (Ancient Greek).... | google-deepmind/science-skills |
| [**protein-sequence-msa**](https://github.com/google-deepmind/science-skills/tree/main/skills/protein_sequence_msa) | Align protein sequences with EBI Clustal Omega (up to 4000 sequences, 4 MB): assess similarity, domain and residue conservation.... | google-deepmind/science-skills |
| [**protein-sequence-similarity-search**](https://github.com/google-deepmind/science-skills/tree/main/skills/protein_sequence_similarity_search) | Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback).... | google-deepmind/science-skills |
| [**pubchem-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/pubchem_database) | Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics.... | google-deepmind/science-skills |
| [**pubmed-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/pubmed_database) | Search PubMed for literature and clinical trials: fetch abstracts and full text, link papers to genes/proteins/compounds (PubChem),... | google-deepmind/science-skills |
| [**pymol**](https://github.com/google-deepmind/science-skills/tree/main/skills/pymol) | Visualize, align and render protein/molecular structures in PyMOL: images, superposition, distances and contacts, highlight binding sites,... | google-deepmind/science-skills |
| [**quickgo-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/quickgo_database) | Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this when you need to map genes to biological processes,... | google-deepmind/science-skills |
| [**reactome-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/reactome_database) | Query the Reactome database (Analysis and Content Services). Use when the user asks about pathway analysis, gene list enrichment,... | google-deepmind/science-skills |
| [**string-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/string_database) | Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology.... | google-deepmind/science-skills |
| [**ucsc-conservation-and-tfbs**](https://github.com/google-deepmind/science-skills/tree/main/skills/ucsc_conservation_and_tfbs) | Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding Sites (TFBS) from the UCSC Genome Browser.... | google-deepmind/science-skills |
| [**unibind-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/unibind_database) | Queries the UniBind database for experimentally validated transcription factor (TF) binding sites.... | google-deepmind/science-skills |
| [**uniprot-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/uniprot_database) | Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and UniRef. Use when searching for proteins,... | google-deepmind/science-skills |
| [**uv**](https://github.com/google-deepmind/science-skills/tree/main/skills/uv) | Checks whether the uv Python package manager is installed and installs it if missing. Ensures uv is on PATH.... | google-deepmind/science-skills |
| [**workflow-skill-creator**](https://github.com/google-deepmind/science-skills/tree/main/skills/workflow_skill_creator) | Distill a completed workflow or interaction into a reusable agent skill. Use when the user says make this a skill,... | google-deepmind/science-skills |

### 开发 / 工程 / 工作流

| Skill | 描述 | 来源 |
|---|---|---|
| [**claude-automation-recommender**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup/skills/claude-automation-recommender) | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers).... | anthropics/claude-plugins-official |
| [**claude-md-improver**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management/skills/claude-md-improver) | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files.... | anthropics/claude-plugins-official |
| [**cpp-pro**](https://github.com/Jeffallan/claude-skills/tree/main/skills/cpp-pro) | Writes, optimizes, and debugs C++ applications using modern C++20/23 features, template metaprogramming, and high-performance systems techniques.... | Jeffallan/claude-skills |
| [**critical-code-reviewer**](https://github.com/posit-dev/skills/tree/main/posit-dev/critical-code-reviewer) | Rigorously review code or pull requests for correctness, security, accessibility, maintainability, tests, and edge cases.... | posit-dev/skills |
| [**describe-design**](https://github.com/posit-dev/skills/tree/main/posit-dev/describe-design) | Research a codebase and write architecture documentation: how a feature works, system overview, code structure for onboarding,... | posit-dev/skills |
| [**implement**](https://github.com/posit-dev/skills/tree/main/posit-dev/implement) | Orchestrates implementation of a plan file by delegating work to subagents in parallel. Verifies git branch state, tracks progress,... | posit-dev/skills |
| [**instrument-data-to-allotrope**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/instrument-data-to-allotrope) | Convert lab instrument output (PDF, CSV, Excel, TXT) to Allotrope Simple Model JSON or flattened CSV: auto-detect instrument type,... | anthropics/knowledge-work-plugins |
| [**karpathy-guidelines**](https://github.com/BurukalaManiReethika/Karpathy-Inspired-Claude-Code-Guidelines/tree/main/skills/karpathy-guidelines) | Six principles for better Claude Code behavior — think before coding, keep it simple, make surgical changes, define success criteria,... | BurukalaManiReethika/Karpathy-Inspired-Claude-Code-Guidelines |
| [**playwright-cli**](https://github.com/microsoft/playwright-cli/tree/main/skills/playwright-cli) | Automate browser interactions, test web pages and work with Playwright tests. | microsoft/playwright-cli |
| [**pr-create**](https://github.com/posit-dev/skills/tree/main/github/pr-create) | Create a pull request from current changes, watch GitHub CI and debug failures until it passes; stops when CI is green and returns the PR link.... | posit-dev/skills |
| [**pr-threads-address**](https://github.com/posit-dev/skills/tree/main/github/pr-threads-address) | Address PR review feedback by systematically working through every unresolved PR review thread on the current branch's PR - analyze each comment,... | posit-dev/skills |
| [**pr-threads-resolve**](https://github.com/posit-dev/skills/tree/main/github/pr-threads-resolve) | Bulk resolve unresolved PR review threads on the current branch’s PR — typically after threads have been addressed manually or via /pr-threads-address | posit-dev/skills |
| [**rust-skills**](https://github.com/leonardomso/rust-skills) | Comprehensive Rust coding guidelines with 265 rules across 26 categories. Use when writing, reviewing, or refactoring Rust code. Covers ownership,... | leonardomso/rust-skills |
| [**scientific-problem-selection**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scientific-problem-selection) | Help scientists pick and pressure-test research problems: pitch a new idea, work through a stuck project, evaluate risks,... | anthropics/knowledge-work-plugins |
| [**session-report**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report/skills/session-report) | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills,... | anthropics/claude-plugins-official |
| [**start**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/start) | Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature,... | anthropics/knowledge-work-plugins |
| [**working-on**](https://github.com/posit-dev/skills/tree/main/posit-dev/working-on) | Set a tracking document as the source of truth for the current feature or task. Use when starting work on a feature, bug fix,... | posit-dev/skills |

### Nextflow / nf-core 工作流

| Skill | 描述 | 来源 |
|---|---|---|
| [**create-workflow**](https://github.com/nextflow-io/agent-skills/tree/master/skills/create-workflow) | INVOKE THIS SKILL IMMEDIATELY when user asks to: write/create/build a Nextflow pipeline or workflow, create any bioinformatics pipeline (RNA-seq,... | nextflow-io/agent-skills |
| [**install-nextflow**](https://github.com/nextflow-io/agent-skills/tree/master/skills/install-nextflow) | Install or upgrade Nextflow on the user's machine. Use when the user wants to install Nextflow, check their current Nextflow version,... | nextflow-io/agent-skills |
| [**launch-workflow**](https://github.com/nextflow-io/agent-skills/tree/master/skills/launch-workflow) | Launch Nextflow pipeline executions on cloud and HPC clusters via Seqera Platform.... | nextflow-io/agent-skills |
| [**migrate-nextflow-code**](https://github.com/nextflow-io/agent-skills/tree/master/skills/migrate-nextflow-code) | Migrate a Nextflow pipeline to new language patterns. | nextflow-io/agent-skills |
| [**run-module**](https://github.com/nextflow-io/agent-skills/tree/master/skills/run-module) | Run Nextflow Registry modules natively using `nextflow module` commands. Use when running, listing, or getting info about Nextflow modules,... | nextflow-io/agent-skills |
| [**nf-core-lint**](https://github.com/edmundmiller/nf-core-skills/tree/main/skills/nf-core-lint) | Run and interpret `nf-core pipelines lint` to validate a Nextflow pipeline against nf-core community guidelines.... | edmundmiller/nf-core-skills |
| [**nf-core-pipeline**](https://github.com/edmundmiller/nf-core-skills/tree/main/skills/nf-core-pipeline) | Create, lint, and modify nf-core pipelines following community standards.... | edmundmiller/nf-core-skills |
| [**audit-conversion-readiness**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/audit-conversion-readiness) | Read-only first-pass audit of source material (scripts, notebooks, Snakemake/WDL/CWL workflows,... | seqeralabs/nextflow-plugin |
| [**build-nextflow-pipeline**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/build-nextflow-pipeline) | Plan and scaffold a new Nextflow DSL2 pipeline from source material — scripts, repositories, Jupyter/R notebooks, papers,... | seqeralabs/nextflow-plugin |
| [**ce-credentials-setup**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/ce-credentials-setup) | Set up Nextflow Platform compute environments (Seqera Compute, AWS Batch, Kubernetes) and the cloud or cluster credentials they need.... | seqeralabs/nextflow-plugin |
| [**create-container**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/create-container) | Build, claim, or recommend a verified container for a bioinformatics tool — and prove it runs the intended command on representative test data befo... | seqeralabs/nextflow-plugin |
| [**debug-local-run**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/debug-local-run) | Debug a local Nextflow pipeline run. Analyzes .nextflow.log, work directories, and task error logs to identify failures and suggest fixes.... | seqeralabs/nextflow-plugin |
| [**debug-seqera-failed-run**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/debug-seqera-failed-run) | Debug failed Nextflow Platform pipeline runs. Fetches workflow details, failed tasks, and logs to identify root causes and suggest fixes.... | seqeralabs/nextflow-plugin |
| [**find-alternative-tools**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/find-alternative-tools) | Given a named bioinformatics analysis step (e.g. "multiple sequence alignment", "somatic variant calling", "protein structure prediction",... | seqeralabs/nextflow-plugin |
| [**install-nextflow**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/install-nextflow) | Install or upgrade Nextflow on the user's machine. Use when the user wants to install Nextflow, check their current Nextflow version,... | seqeralabs/nextflow-plugin |
| [**launch-workflow**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/launch-workflow) | Launch Nextflow pipeline executions on cloud and HPC clusters via Nextflow Platform.... | seqeralabs/nextflow-plugin |
| [**maintain-nf-core-pipeline**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/maintain-nf-core-pipeline) | Maintain an existing nf-core pipeline: work on the `dev` branch, resolve outstanding template-sync PRs, update shared modules from upstream,... | seqeralabs/nextflow-plugin |
| [**migrate-from-snakemake**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/migrate-from-snakemake) | Convert Snakemake workflows to idiomatic Nextflow DSL2 pipelines with a test-first, modular migration loop. Trigger: "snakemake to nextflow",... | seqeralabs/nextflow-plugin |
| [**migrate-nextflow-code**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/migrate-nextflow-code) | Migrate Nextflow pipeline code while preserving behavior. Use for version upgrades including 25.04 compatibility, strict syntax errors,... | seqeralabs/nextflow-plugin |
| [**nextflow-config**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nextflow-config) | Generate and explain Nextflow configuration files. Use when user asks to create, modify, debug, or understand nextflow.config files.... | seqeralabs/nextflow-plugin |
| [**nextflow-development**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nextflow-development) | Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES,... | seqeralabs/nextflow-plugin |
| [**nextflow-history**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nextflow-history) | Analyze local Nextflow run history and cache. Use when user asks about their recent local runs, wants to see what pipelines they've executed,... | seqeralabs/nextflow-plugin |
| [**nextflow-output-patterns**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nextflow-output-patterns) | Use this skill when writing or reviewing any Nextflow workflow that aggregates per-sample outputs into a combined file,... | seqeralabs/nextflow-plugin |
| [**nextflow-schema**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nextflow-schema) | Generate canonical nextflow_schema.json, optional nextflow_schema.minimal.json, and sample sheet schema files for Nextflow pipelines.... | seqeralabs/nextflow-plugin |
| [**nf-data-lineage**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nf-data-lineage) | Explore Nextflow data lineage to trace where outputs came from and what inputs produced them.... | seqeralabs/nextflow-plugin |
| [**nf-docker-scripts**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nf-docker-scripts) | Guide users on how to manage scripts in Nextflow processes and Docker images. Covers shared helper commands, template directive, inline scripts,... | seqeralabs/nextflow-plugin |
| [**nf-pipeline-design**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nf-pipeline-design) | Make sure to use this skill whenever you are designing, writing, reviewing,... | seqeralabs/nextflow-plugin |
| [**nf-plugin-development**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nf-plugin-development) | Create Nextflow plugins using the official nf-plugin-template and publish to the Nextflow plugin registry. Covers extension points (operators,... | seqeralabs/nextflow-plugin |
| [**nf-plugin-legacy-migration**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nf-plugin-legacy-migration) | Migrate legacy Nextflow plugins to the new plugin registry format.... | seqeralabs/nextflow-plugin |
| [**nf-test**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/nf-test) | Testing Nextflow pipelines with nf-test. Use when setting up nf-test, writing pipeline tests, testing modules/subworkflows,... | seqeralabs/nextflow-plugin |
| [**repair-workflow**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/repair-workflow) | Repair or debug an existing Nextflow workflow or pipeline. Use when the user asks to fix, debug, or improve an existing workflow,... | seqeralabs/nextflow-plugin |
| [**run-module**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/run-module) | Run Nextflow Registry modules natively using `nextflow module` commands. Use when running, listing, or getting info about Nextflow modules. | seqeralabs/nextflow-plugin |
| [**search-existing-modules**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/search-existing-modules) | Given a bioinformatics tool name (e.g. MAFFT, Boltz, bcftools, salmon),... | seqeralabs/nextflow-plugin |
| [**seqera-data-links**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/seqera-data-links) | Add, list, inspect, browse, update, and delete data links in Nextflow Platform workspaces. Use when asked to connect S3/GCS/Azure storage,... | seqeralabs/nextflow-plugin |
| [**seqerakit**](https://github.com/seqeralabs/nextflow-plugin/tree/main/skills/seqerakit) | Write seqerakit YAML configuration files for automating Nextflow Platform setup. Covers pipelines, launch, compute-envs, datasets, credentials,... | seqeralabs/nextflow-plugin |
| [**nextflow-agents**](./skills/nextflow-agents) | Write, run and debug Nextflow agent blocks (26.10+, preview): LLM steps inside a pipeline with typed I/O, prompt, tools, skills, caching,... | 自定义 |
| [**nextflow-development**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/nextflow-development) | Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES,... | anthropics/knowledge-work-plugins |
| [**nextflow-skills-guide**](./skills/nextflow-skills-guide) | Map of every Nextflow / nf-core skill in this repository and which one to use: build, convert, migrate, test, debug,... | 自定义 |
| [**nf-core-agents-md**](./skills/nf-core-agents-md) | Apply the official nf-core AI-agent rules (AGENTS.md) when creating or editing an nf-core Nextflow pipeline: template structure, modules, configs,... | 自定义 |

### 科学研究 Agent Skills（K-Dense）

| Skill | 描述 | 来源 |
|---|---|---|
| [**13c-metabolic-flux**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/13c-metabolic-flux) | Estimates intracellular metabolic fluxes from steady-state carbon-13 isotope-tracing measurements using validated atom maps,... | K-Dense-AI/claude-scientific-skills |
| [**adaptyv**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/adaptyv) | Uses the Adaptyv Bio Foundry API and Python SDK to design protein characterization experiments, estimate costs, submit sequences,... | K-Dense-AI/claude-scientific-skills |
| [**aeon**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/aeon) | This skill should be used for time series machine learning tasks including classification, regression, clustering, forecasting, anomaly detection,... | K-Dense-AI/claude-scientific-skills |
| [**alphagenome**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/alphagenome) | Looks up precomputed AlphaGenome Atlas effects for any GRCh38 single-nucleotide variant (AVI score with Phred and 18 SHAP feature attributions,... | K-Dense-AI/claude-scientific-skills |
| [**analytical-method-validation**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/analytical-method-validation) | Plans, executes, and documents validation, verification, and transfer of analytical procedures under the governing framework - ICH Q2(R2) and Q14,... | K-Dense-AI/claude-scientific-skills |
| [**anndata**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/anndata) | Handles annotated matrices in single-cell analysis, .h5ad and Zarr files, and integration with the scverse ecosystem.... | K-Dense-AI/claude-scientific-skills |
| [**arbor**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/arbor) | Applies Arbor Hypothesis Tree Refinement to research artifacts with repeatable evaluators, including model training, agent harnesses,... | K-Dense-AI/claude-scientific-skills |
| [**arboreto**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/arboreto) | Infers candidate gene regulatory networks from bulk or single-cell expression data using AertsLab Arboreto GRNBoost2 and GENIE3.... | K-Dense-AI/claude-scientific-skills |
| [**astropy**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/astropy) | Core Python library for astronomy and astrophysics workflows that need Astropy APIs, including units/quantities, coordinates, FITS I/O, tables,... | K-Dense-AI/claude-scientific-skills |
| [**autoskill**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/autoskill) | Analyzes user-requested Screenpipe history windows to detect repeated research workflows, match existing scientific skills,... | K-Dense-AI/claude-scientific-skills |
| [**benchling-integration**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/benchling-integration) | Benchling Python SDK and REST API integration for registry entities, inventory, ELN entries, workflows, Benchling Apps,... | K-Dense-AI/claude-scientific-skills |
| [**bgpt-paper-search**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/bgpt-paper-search) | Searches BGPT scientific papers by topic or DOI and retrieves claim-level evidence extracted from full text, including experiments,... | K-Dense-AI/claude-scientific-skills |
| [**bids**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/bids) | Organizes, queries, validates, and converts Brain Imaging Data Structure (BIDS) datasets.... | K-Dense-AI/claude-scientific-skills |
| [**biopython**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/biopython) | Provides Biopython workflows for sequence manipulation, file parsing (FASTA/GenBank/PDB), phylogenetics,... | K-Dense-AI/claude-scientific-skills |
| [**bioservices**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/bioservices) | Provides a Python interface to bioinformatics services including UniProt, KEGG, ChEMBL, Reactome, QuickGO, and UniChem.... | K-Dense-AI/claude-scientific-skills |
| [**bulk-rnaseq**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/bulk-rnaseq) | Prepares bulk RNA-seq FASTQ, Salmon, STAR or featureCounts output for gene-level differential expression.... | K-Dense-AI/claude-scientific-skills |
| [**cantera**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/cantera) | Runs Cantera homogeneous chemical reactors and evaluates ignition delay with mechanism provenance, conservation checks, and numerical refinement.... | K-Dense-AI/claude-scientific-skills |
| [**cellprofiler**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/cellprofiler) | Runs reproducible CellProfiler microscopy pipelines for nuclear segmentation, cell counts, and per-object fluorescence measurements.... | K-Dense-AI/claude-scientific-skills |
| [**cellxgene-census**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/cellxgene-census) | Queries the CZ CELLxGENE Census programmatically for versioned public single-cell and spatial transcriptomics data.... | K-Dense-AI/claude-scientific-skills |
| [**cirq**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/cirq) | Google quantum computing framework. Use when targeting Google Quantum AI hardware, designing noise-aware circuits,... | K-Dense-AI/claude-scientific-skills |
| [**citation-management**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/citation-management) | Comprehensive citation management for academic research. Search OpenAlex, PubMed, and Google Scholar for papers, extract accurate metadata,... | K-Dense-AI/claude-scientific-skills |
| [**clinical-decision-support**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/clinical-decision-support) | Prepares and validates research-only clinical decision-support evaluation, evidence-profile, cohort, survival, biomarker/model, privacy,... | K-Dense-AI/claude-scientific-skills |
| [**clinical-reports**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/clinical-reports) | Creates safety-bounded draft structures and runs local deterministic checks for clinical case, diagnostic, trial, safety,... | K-Dense-AI/claude-scientific-skills |
| [**cobrapy**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/cobrapy) | Performs constraint-based metabolic modeling with COBRApy, including FBA, pFBA, FVA, gene knockouts, flux sampling, growth media,... | K-Dense-AI/claude-scientific-skills |
| [**consciousness-council**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/consciousness-council) | Structures a multi-perspective council exercise for decisions, research trade-offs, and creative challenges. Simulates thinking archetypes,... | K-Dense-AI/claude-scientific-skills |
| [**dask**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/dask) | Scales pandas, NumPy, and custom Python research workflows beyond memory or across clusters with Dask. Covers DataFrames, Arrays, Bags, Futures,... | K-Dense-AI/claude-scientific-skills |
| [**database-lookup**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/database-lookup) | Queries documented public database APIs with explicit endpoints, filters, pagination, and provenance. Used when a scientific, regulatory,... | K-Dense-AI/claude-scientific-skills |
| [**datalad**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/datalad) | Retrieves, versions, and publishes scientific datasets with DataLad and git-annex, and captures computational provenance with datalad run, rerun,... | K-Dense-AI/claude-scientific-skills |
| [**datamol**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/datamol) | Pythonic wrapper around RDKit with simplified interface and sensible defaults. Preferred for standard drug discovery including SMILES parsing,... | K-Dense-AI/claude-scientific-skills |
| [**deepchem**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/deepchem) | Builds molecular property prediction and MoleculeNet workflows with DeepChem, including SMILES featurization, scaffold or grouped holdouts,... | K-Dense-AI/claude-scientific-skills |
| [**deepspot-m**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/deepspot-m) | Generates transcriptome-wide virtual spatial transcriptomics from H&E histology with DeepSpot-M.... | K-Dense-AI/claude-scientific-skills |
| [**deeptools**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/deeptools) | NGS analysis toolkit. BAM to bigWig conversion, QC (correlation, PCA, fingerprints), heatmaps/profiles (TSS, peaks), for ChIP-seq, RNA-seq,... | K-Dense-AI/claude-scientific-skills |
| [**depmap**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/depmap) | Retrieves and analyzes Cancer Dependency Map (DepMap) release data, including CRISPR Chronos gene effects, cancer model annotations,... | K-Dense-AI/claude-scientific-skills |
| [**dhdna-profiler**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/dhdna-profiler) | Applies the DHDNA framework as an exploratory rubric for reasoning and writing patterns in supplied text. Used for explicit requests for DHDNA,... | K-Dense-AI/claude-scientific-skills |
| [**diffdock**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/diffdock) | Predicts protein-small-molecule binding poses with DiffDock and DiffDock-L from PDB or sequence plus SMILES/SDF/MOL2. Covers batch docking,... | K-Dense-AI/claude-scientific-skills |
| [**dnanexus-integration**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/dnanexus-integration) | Builds and operates reproducible genomics workloads on DNAnexus with the dx CLI, dxpy, apps/applets, native workflows, dxCompiler, and Nextflow.... | K-Dense-AI/claude-scientific-skills |
| [**esm**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/esm) | Uses the Biohub esm Python SDK for ESM3 protein generation, ESMC embeddings, and ESMFold2 all-atom folding.... | K-Dense-AI/claude-scientific-skills |
| [**etetoolkit**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/etetoolkit) | Analyzes, manipulates, compares, annotates, and visualizes phylogenetic or other hierarchical trees with ETE 4. Supports Newick/Nexus tree I/O,... | K-Dense-AI/claude-scientific-skills |
| [**exa-search**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/exa-search) | Searches scientific and technical web content with Exa and extracts page or PDF text from URLs in batches.... | K-Dense-AI/claude-scientific-skills |
| [**experimental-design**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/experimental-design) | Designs experiments and studies BEFORE data is collected — choosing a design, randomizing, blocking,... | K-Dense-AI/claude-scientific-skills |
| [**exploratory-data-analysis**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/exploratory-data-analysis) | Performs bounded, local exploratory analysis of explicitly supported scientific files. Supports redacted CSV/TSV/JSON profiles; optional NumPy,... | K-Dense-AI/claude-scientific-skills |
| [**fictiv**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/fictiv) | Operates Fictiv (app.fictiv.com), the on-demand manufacturing platform, end to end in the user's browser. Covers uploading CAD parts,... | K-Dense-AI/claude-scientific-skills |
| [**flowio**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/flowio) | Reads, inspects, and writes Flow Cytometry Standard (FCS) 2.0, 3.0, and 3.1 files with FlowIO.... | K-Dense-AI/claude-scientific-skills |
| [**flowkit**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/flowkit) | Analyzes flow cytometry data with FlowKit, including spillover compensation, logicle and biexponential transforms, hierarchical gating,... | K-Dense-AI/claude-scientific-skills |
| [**fluidsim**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/fluidsim) | Plans, configures, inspects, restarts, and analyzes bounded FluidSim computational-fluid-dynamics simulations with explicit numerical-validity and... | K-Dense-AI/claude-scientific-skills |
| [**folklore-variant-evidence**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/folklore-variant-evidence) | Retrieves ClinGen gene-disease validity assertions for a public gene or disease,... | K-Dense-AI/claude-scientific-skills |
| [**generate-image**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/generate-image) | Generates or edits images with AI models through the OpenRouter Image API (Gemini, Seedream, Recraft, GPT-Image, Riverflow). Use for photos,... | K-Dense-AI/claude-scientific-skills |
| [**geniml**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/geniml) | Supports audited local Geniml genomic-interval workflows: validate BED and universe contracts, plan Region2Vec or scEmbed runs,... | K-Dense-AI/claude-scientific-skills |
| [**genomic-coordinates**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/genomic-coordinates) | Converts genomic intervals between coordinate conventions, normalises and compares variant representations,... | K-Dense-AI/claude-scientific-skills |
| [**genomic-intelligence**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/genomic-intelligence) | Predicts regulatory features, gene structure, and expression directly from DNA sequence using Genomic Intelligence's hosted transformer DNA languag... | K-Dense-AI/claude-scientific-skills |
| [**geomaster**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/geomaster) | Supports geospatial research workflows for remote sensing, vector and raster GIS, spatial statistics, terrain and network analysis,... | K-Dense-AI/claude-scientific-skills |
| [**geopandas**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/geopandas) | Guidance and local audit tools for Python workflows that directly use GeoPandas GeoSeries, GeoDataFrame, spatial operations, or vector-data I/O. | K-Dense-AI/claude-scientific-skills |
| [**get-available-resources**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/get-available-resources) | Detects host inventory and effective CPU, memory, disk, scheduler, container,... | K-Dense-AI/claude-scientific-skills |
| [**gget**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/gget) | Queries 20+ bioinformatics resources through CLI/Python. Supports quick lookups of gene info, BLAST/BLAT, viral sequence downloads,... | K-Dense-AI/claude-scientific-skills |
| [**ginkgo-cloud-lab**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/ginkgo-cloud-lab) | Guides protocol selection, input preparation, pricing checks, and browser ordering on Ginkgo Bioworks Cloud Lab (cloud.ginkgo.bio).... | K-Dense-AI/claude-scientific-skills |
| [**glycoengineering**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/glycoengineering) | Analyzes and engineers protein glycosylation by scanning canonical N-glycosylation sequons, describing S/T-rich regions,... | K-Dense-AI/claude-scientific-skills |
| [**gtars**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/gtars) | Supports Gtars for local genomic interval models and set algebra, overlaps and counts, consensus and coverage, tokenization, fragment processing,... | K-Dense-AI/claude-scientific-skills |
| [**histolab**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/histolab) | Extracts and preprocesses whole-slide histology image tiles with Histolab. Use for WSI inspection, tissue masks,... | K-Dense-AI/claude-scientific-skills |
| [**hugging-science**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/hugging-science) | Discovers and evaluates scientific datasets, models, methodology posts, and Spaces through the Hugging Science catalog.... | K-Dense-AI/claude-scientific-skills |
| [**hypogenic**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/hypogenic) | Plans and audits use of ChicagoHAI HypoGeniC/HypoRefine for LLM-assisted hypothesis generation from labeled text datasets.... | K-Dense-AI/claude-scientific-skills |
| [**hypothesis-generation**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/hypothesis-generation) | Formulates evidence-bounded scientific questions, candidate hypotheses, rival explanations, causal or associational claims,... | K-Dense-AI/claude-scientific-skills |
| [**imaging-data-commons**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/imaging-data-commons) | Queries and downloads public cancer imaging data from NCI Imaging Data Commons. Supports IDC collection discovery, DICOM access, radiology (CT, MR,... | K-Dense-AI/claude-scientific-skills |
| [**infographics**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/infographics) | Creates and reviews infographics with Nano Banana 2 via OpenRouter. Use for statistical summaries, timelines, comparisons, processes,... | K-Dense-AI/claude-scientific-skills |
| [**iso-standards-readiness**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/iso-standards-readiness) | Prepares and structurally reviews readiness evidence for ISO management-system and laboratory-competence standards - ISO 13485 medical device QMS,... | K-Dense-AI/claude-scientific-skills |
| [**lab-hardware-cad**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/lab-hardware-cad) | Designs custom laboratory hardware as parametric build123d models and exports fabrication artifacts as STEP, STL,... | K-Dense-AI/claude-scientific-skills |
| [**labarchive-integration**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/labarchive-integration) | Integrates with the official LabArchives ELN REST-like API and Inventory API v1. Supports regional endpoint selection, signed-request construction,... | K-Dense-AI/claude-scientific-skills |
| [**lamindb**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/lamindb) | Manages biological datasets and models with LaminDB, including artifact registration, lineage tracking, schema validation,... | K-Dense-AI/claude-scientific-skills |
| [**latchbio-integration**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/latchbio-integration) | Builds, registers, debugs, and operates bioinformatics workflows on Latch using the Python SDK, CLI, Latch Data and Registry, Nextflow, Snakemake,... | K-Dense-AI/claude-scientific-skills |
| [**latex-posters**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/latex-posters) | Creates research posters in LaTeX using beamerposter, tikzposter, or baposter. Use for conference posters, academic presentations,... | K-Dense-AI/claude-scientific-skills |
| [**liteparse**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/liteparse) | Local document and PDF parsing that returns spatial text with bounding boxes. Use for extracting text from PDFs, DOCX, Office files,... | K-Dense-AI/claude-scientific-skills |
| [**literature-review**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/literature-review) | Conducts systematic, scoping, and narrative literature reviews using PubMed, arXiv, bioRxiv, Semantic Scholar, and other appropriate sources.... | K-Dense-AI/claude-scientific-skills |
| [**mageck**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/mageck) | Analyzes pooled CRISPR screen FASTQ reads and guide-count matrices with MAGeCK, validates guide libraries and contrasts,... | K-Dense-AI/claude-scientific-skills |
| [**marine-carbonate-chemistry**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/marine-carbonate-chemistry) | Solves seawater carbonate chemistry with PyCO2SYS for chemical oceanography, ocean acidification, and marine carbon-cycle research.... | K-Dense-AI/claude-scientific-skills |
| [**markdown-mermaid-writing**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/markdown-mermaid-writing) | Writes scientific Markdown documentation and Mermaid diagrams for workflows, relationships, timelines, and schemas. Provides syntax references,... | K-Dense-AI/claude-scientific-skills |
| [**market-research-reports**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/market-research-reports) | Builds evidence-traceable market research reports and assumption-driven market sizing or forecast scenarios. Use for market definition,... | K-Dense-AI/claude-scientific-skills |
| [**markitdown**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/markitdown) | Converts heterogeneous documents and selected URIs to Markdown with Microsoft MarkItDown for text analysis, search, and LLM/RAG ingestion.... | K-Dense-AI/claude-scientific-skills |
| [**matchms**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/matchms) | Processes, cleans, compares, and searches tandem mass spectra with matchms. Use for MS/MS file I/O, metadata harmonization, peak filtering,... | K-Dense-AI/claude-scientific-skills |
| [**matlab**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/matlab) | Builds, reviews, migrates, and plans MATLAB or GNU Octave numerical workflows. Use for arrays, tabular/time data, tests, projects, graphics,... | K-Dense-AI/claude-scientific-skills |
| [**matplotlib**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/matplotlib) | Creates and customizes scientific plots with Matplotlib. Used for fine-grained control over plot elements, novel plot types,... | K-Dense-AI/claude-scientific-skills |
| [**medchem**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/medchem) | Applies medicinal chemistry filters for compound triage, using drug-likeness rules (Lipinski, Veber, CNS), structural alert catalogs (PAINS, NIBR,... | K-Dense-AI/claude-scientific-skills |
| [**modal**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/modal) | Modal is a serverless cloud platform for running Python on demand, including on-demand GPUs. Use when deploying or serving AI/ML models,... | K-Dense-AI/claude-scientific-skills |
| [**molecular-dynamics**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/molecular-dynamics) | Runs and analyzes molecular dynamics simulations with OpenMM and MDAnalysis. Sets up protein/small molecule systems, defines force fields,... | K-Dense-AI/claude-scientific-skills |
| [**molfeat**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/molfeat) | Featurizes small molecules with Molfeat for QSAR/QSPR, chemical similarity, virtual screening, and molecular ML. Covers ECFP/MACCS fingerprints,... | K-Dense-AI/claude-scientific-skills |
| [**ncats-arax**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/ncats-arax) | Queries the NCATS Translator ARAX production API for bounded, typed,... | K-Dense-AI/claude-scientific-skills |
| [**networkx**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/networkx) | Creates, analyzes, and visualizes complex networks and graphs in Python with NetworkX. Use when working with network/graph data structures,... | K-Dense-AI/claude-scientific-skills |
| [**neurokit2**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/neurokit2) | Builds and audits reproducible NeuroKit2 research workflows for physiological time-series preprocessing, event/interval analysis,... | K-Dense-AI/claude-scientific-skills |
| [**neuropixels-analysis**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/neuropixels-analysis) | Analyzes Neuropixels extracellular recordings end-to-end with SpikeInterface. Covers loading SpikeGLX/Open Ephys/NWB data, preprocessing,... | K-Dense-AI/claude-scientific-skills |
| [**nextflow**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/nextflow) | Builds, runs, and debugs Nextflow DSL2 pipelines and nf-core workflows. Use for Nextflow, nf-core, .nf files, nextflow.config,... | K-Dense-AI/claude-scientific-skills |
| [**nmrglue**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/nmrglue) | Processes calibrated one-dimensional complex NMR free-induction decays with nmrglue into phased spectra, peak candidates,... | K-Dense-AI/claude-scientific-skills |
| [**nwb-conversion**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/nwb-conversion) | Converts neuroscience acquisition data to Neurodata Without Borders files with NeuroConv and PyNWB, preserves metadata and timebases,... | K-Dense-AI/claude-scientific-skills |
| [**omero-integration**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/omero-integration) | Inspects and automates microscopy data workflows against OMERO.server with omero-py, BlitzGateway, OMERO CLI, tables, annotations, ROIs, rendering,... | K-Dense-AI/claude-scientific-skills |
| [**onekgpd**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/onekgpd) | Queries the 1000 Genomes Project dataset (3,202 whole-genome-sequenced individuals, GRCh38) at the level of individual participants.... | K-Dense-AI/claude-scientific-skills |
| [**ontology-term-resolution**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/ontology-term-resolution) | Resolves free-text scientific labels to ontology term IDs and validates existing CURIEs against the EBI Ontology Lookup Service (OLS4).... | K-Dense-AI/claude-scientific-skills |
| [**open-notebook**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/open-notebook) | Organizes research with the self-hosted Open Notebook alternative to NotebookLM. Supports source ingestion (PDFs, web pages, audio, video,... | K-Dense-AI/claude-scientific-skills |
| [**openpiv**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/openpiv) | Performs Particle Image Velocimetry (PIV) analysis with OpenPIV. Use when extracting velocity fields from PIV image pairs,... | K-Dense-AI/claude-scientific-skills |
| [**opentrons-integration**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/opentrons-integration) | Authors, reviews, migrates, simulates, and troubleshoots official Opentrons Python Protocol API v2 protocols for Flex and OT-2 robots.... | K-Dense-AI/claude-scientific-skills |
| [**optimize-for-gpu**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/optimize-for-gpu) | GPU-accelerates scientific Python on NVIDIA hardware and verifies that the result is correct and faster.... | K-Dense-AI/claude-scientific-skills |
| [**pacsomatic**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pacsomatic) | Prepares and launches nf-core/pacsomatic matched tumor-normal PacBio HiFi genomics workflows from unaligned BAM inputs.... | K-Dense-AI/claude-scientific-skills |
| [**paper-lookup**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/paper-lookup) | Searches 18 scholarly APIs for papers, preprints, citations, open-access full text, repository records, and journal OA status,... | K-Dense-AI/claude-scientific-skills |
| [**paperclip**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/paperclip) | Searches and reads biomedical papers, FDA/PMDA/EMA documents, clinical trials, and protein records with the GXL Paperclip CLI and Python SDK.... | K-Dense-AI/claude-scientific-skills |
| [**paperzilla**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/paperzilla) | Reads projects, searches project feeds, and retrieves recommendations and canonical papers in Paperzilla through the pz CLI.... | K-Dense-AI/claude-scientific-skills |
| [**parallel-web**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/parallel-web) | Uses Parallel CLI for web search, URL extraction, deep research, structured data enrichment, entity discovery, and recurring web monitoring.... | K-Dense-AI/claude-scientific-skills |
| [**pathml**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pathml) | Supports local computational pathology research with PathML: slide loading and tiling, preprocessing and QC, h5path storage,... | K-Dense-AI/claude-scientific-skills |
| [**pathogen-variant-surveillance**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pathogen-variant-surveillance) | Queries public GenSpectrum LAPIS data for pathogen genomic surveillance, current lineage nomenclature, weekly sequence proportions,... | K-Dense-AI/claude-scientific-skills |
| [**pathway-enrichment**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pathway-enrichment) | Performs pathway and gene-set enrichment analysis on gene lists or ranked gene data and interprets the results.... | K-Dense-AI/claude-scientific-skills |
| [**peer-review**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/peer-review) | Prepares evidence-bounded, constructive peer-review drafts and structured manuscript assessments.... | K-Dense-AI/claude-scientific-skills |
| [**pennylane**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pennylane) | Builds and differentiates PennyLane quantum circuits, hybrid PyTorch or JAX models, molecular VQE and QAOA workflows.... | K-Dense-AI/claude-scientific-skills |
| [**phylogenetics**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/phylogenetics) | Builds and analyzes phylogenetic trees using MAFFT multiple sequence alignment, IQ-TREE maximum likelihood with ModelFinder and branch support,... | K-Dense-AI/claude-scientific-skills |
| [**pi-agent**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pi-agent) | Builds with and operates Pi, the minimal terminal coding harness. Use for installing Pi,... | K-Dense-AI/claude-scientific-skills |
| [**pkpd-modeling**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pkpd-modeling) | Pharmacokinetic and pharmacodynamic modelling and simulation - non-compartmental analysis, compartmental and population PK,... | K-Dense-AI/claude-scientific-skills |
| [**polars**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/polars) | High-performance DataFrame library for Python ETL, analytics, and pandas migration.... | K-Dense-AI/claude-scientific-skills |
| [**polars-bio**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/polars-bio) | Performs genomic interval overlap, nearest, merge, coverage, complement and subtraction on Polars DataFrames, and reads or writes BED, VCF, BCF,... | K-Dense-AI/claude-scientific-skills |
| [**pptx-posters**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pptx-posters) | Creates and audits editable scientific posters in macro-free PowerPoint (.pptx) from author-approved local content and assets.... | K-Dense-AI/claude-scientific-skills |
| [**primekg**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/primekg) | Queries a pinned Precision Medicine Knowledge Graph (PrimeKG) CSV for typed gene, drug, disease, and phenotype nodes, direct associations,... | K-Dense-AI/claude-scientific-skills |
| [**primer-design**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/primer-design) | Designs and audits PCR and RT-qPCR primers with Primer3, explicit thermodynamic conditions, reference-based off-target amplification searches,... | K-Dense-AI/claude-scientific-skills |
| [**protocolsio-integration**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/protocolsio-integration) | Reads, validates, and safely exports protocols.io data with current official REST/MCP contracts, or creates non-executing mutation plans.... | K-Dense-AI/claude-scientific-skills |
| [**pufferlib**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pufferlib) | Version-aware guidance for PufferLib reinforcement-learning environments, vectorization, policies, PuffeRL training, evaluation,... | K-Dense-AI/claude-scientific-skills |
| [**pybamm**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pybamm) | Simulates lithium-ion battery charge, discharge and rest experiments with PyBaMM, records parameter-set provenance,... | K-Dense-AI/claude-scientific-skills |
| [**pycalphad**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pycalphad) | Computes finite-temperature CALPHAD equilibria, phase fractions, and phase compositions from thermodynamic TDB databases using pycalphad.... | K-Dense-AI/claude-scientific-skills |
| [**pydeseq2**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pydeseq2) | Performs bulk RNA-seq differential expression analysis with PyDESeq2, including count validation, formula designs, explicit contrasts, Wald tests,... | K-Dense-AI/claude-scientific-skills |
| [**pydicom**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pydicom) | Reads, inspects, writes, transforms, and preflights local DICOM datasets and pixel data. Applies to DICOM metadata, transfer syntaxes,... | K-Dense-AI/claude-scientific-skills |
| [**pyhealth**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pyhealth) | Builds and validates PyHealth clinical machine-learning pipelines for EHR, signals, imaging, and medical codes. Use for PyHealth dataset loading,... | K-Dense-AI/claude-scientific-skills |
| [**pylabrobot**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pylabrobot) | Develops and reviews PyLabRobot lab-automation resources, liquid-handling plans, offline simulations, and supported-device integrations.... | K-Dense-AI/claude-scientific-skills |
| [**pymatgen**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pymatgen) | Analyzes, validates, converts, and transforms materials structures and computed materials data with pymatgen. Use for local phase diagrams,... | K-Dense-AI/claude-scientific-skills |
| [**pymc**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pymc) | Builds and checks Bayesian models with PyMC, including hierarchical models, NUTS MCMC, variational inference, mutable-data predictions,... | K-Dense-AI/claude-scientific-skills |
| [**pymoo**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pymoo) | Solves and validates single-, multi-, and many-objective optimization with pymoo, including NSGA-II, NSGA-III, MOEA/D, constraints,... | K-Dense-AI/claude-scientific-skills |
| [**pyopenms**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pyopenms) | Processes mass spectrometry data with pyOpenMS. Supports proteomics and metabolomics workflows—feature detection, peptide/protein identification,... | K-Dense-AI/claude-scientific-skills |
| [**pysam**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pysam) | Provides Python/HTSlib workflows for genomic files. Used when reading, querying, filtering, or writing SAM/BAM/CRAM, VCF/BCF, FASTA/FASTQ,... | K-Dense-AI/claude-scientific-skills |
| [**pytdc**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pytdc) | Provides Therapeutics Data Commons workflows through PyTDC for registry discovery, dataset access, task-aware splits, evaluator metrics,... | K-Dense-AI/claude-scientific-skills |
| [**pytorch-lightning**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pytorch-lightning) | Deep learning framework (PyTorch Lightning / lightning package). Organize PyTorch code into LightningModules, configure Trainers for multi-GPU/TPU,... | K-Dense-AI/claude-scientific-skills |
| [**pyzotero**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/pyzotero) | Manages Zotero reference libraries using the pyzotero Python client: retrieves, creates, updates, and deletes items, collections, tags,... | K-Dense-AI/claude-scientific-skills |
| [**qiime2-amplicon**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/qiime2-amplicon) | Processes paired-end 16S amplicon reads into QIIME 2 ASVs and taxonomy with retained artifact provenance. Checks paired FASTQ manifests,... | K-Dense-AI/claude-scientific-skills |
| [**qiskit**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/qiskit) | Builds, simulates, transpiles, and executes quantum circuits with Qiskit and IBM Quantum Runtime. Use for Qiskit 2.x circuits and operators,... | K-Dense-AI/claude-scientific-skills |
| [**qutip**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/qutip) | Simulate and audit closed and open quantum-system models with QuTiP 5, including deterministic, trajectory, steady-state, spectral,... | K-Dense-AI/claude-scientific-skills |
| [**rdkit**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/rdkit) | Cheminformatics toolkit for fine-grained molecular control. SMILES/SDF parsing, descriptors (MW, LogP, TPSA), fingerprints, substructure search,... | K-Dense-AI/claude-scientific-skills |
| [**relion**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/relion) | Validates and executes RELION single-particle cryo-EM refinement and half-map postprocessing. Supports STAR optics/acquisition checks,... | K-Dense-AI/claude-scientific-skills |
| [**relsa-severity-assessment**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/relsa-severity-assessment) | Supports multivariate severity assessment and exploratory endpoint-time score forecasting for laboratory animal studies using the RELSA (RELative S... | K-Dense-AI/claude-scientific-skills |
| [**research-grants**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/research-grants) | Supports research proposal preparation and review for NSF, NIH, DOE, DARPA, and Taiwan NSTC, including opportunity-specific requirements, aims,... | K-Dense-AI/claude-scientific-skills |
| [**research-lookup**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/research-lookup) | Compiles current scholarly evidence for a scientific manuscript or research brief when the user explicitly asks to gather literature, references,... | K-Dense-AI/claude-scientific-skills |
| [**rowan**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/rowan) | Rowan is a cloud-native molecular modeling and medicinal-chemistry workflow platform with a Python API. Use for pKa and macropKa prediction,... | K-Dense-AI/claude-scientific-skills |
| [**scanpy**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scanpy) | Performs Scanpy single-cell RNA-seq QC, normalization, HVG selection, PCA/UMAP/t-SNE, clustering, exploratory marker ranking,... | K-Dense-AI/claude-scientific-skills |
| [**scholar-evaluation**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scholar-evaluation) | Provides qualitative-first, evidence-traceable developmental review of scholarly works and audit low-stakes research-assessment rubrics with option... | K-Dense-AI/claude-scientific-skills |
| [**scientific-brainstorming**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scientific-brainstorming) | Facilitates evidence-aware scientific ideation with independent generation, structured discussion, explicit assumptions, transparent evaluation,... | K-Dense-AI/claude-scientific-skills |
| [**scientific-critical-thinking**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scientific-critical-thinking) | Evaluates scientific claims and evidence quality. Applies to experimental design validity, biases and confounders, statistical interpretation,... | K-Dense-AI/claude-scientific-skills |
| [**scientific-schematics**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scientific-schematics) | Generates scientific diagram drafts using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.7 Flash for quality review.... | K-Dense-AI/claude-scientific-skills |
| [**scientific-slides**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scientific-slides) | Builds slide decks and presentations for research talks. Used for making PowerPoint slides, conference presentations, seminar talks,... | K-Dense-AI/claude-scientific-skills |
| [**scientific-visualization**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scientific-visualization) | Creates and audits truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn, or Plotly. Use it for figure design,... | K-Dense-AI/claude-scientific-skills |
| [**scientific-writing**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scientific-writing) | Drafts, revises, and audits scientific manuscripts or reports with explicit evidence provenance, reporting-guideline coverage,... | K-Dense-AI/claude-scientific-skills |
| [**scikit-bio**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scikit-bio) | Biological data toolkit. Sequence analysis, alignments, phylogenetic trees, diversity metrics (alpha/beta, UniFrac), ordination (PCoA), PERMANOVA,... | K-Dense-AI/claude-scientific-skills |
| [**scikit-learn**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scikit-learn) | Supports machine learning in Python with scikit-learn. Applies when working with supervised learning (classification, regression),... | K-Dense-AI/claude-scientific-skills |
| [**scikit-survival**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scikit-survival) | Builds, evaluates, and audits right-censored or competing-risk survival workflows with scikit-survival, including leakage-safe preprocessing,... | K-Dense-AI/claude-scientific-skills |
| [**scvelo**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scvelo) | Performs RNA velocity analysis with scVelo from spliced and unspliced single-cell RNA counts. Fits deterministic or dynamical models,... | K-Dense-AI/claude-scientific-skills |
| [**scvi-tools**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/scvi-tools) | Fits probabilistic models for single-cell omics, including scVI batch integration, scANVI annotation, totalVI CITE-seq,... | K-Dense-AI/claude-scientific-skills |
| [**seaborn**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/seaborn) | Creates Seaborn statistical visualizations with pandas integration for distributions, relationships, categorical comparisons, regression displays,... | K-Dense-AI/claude-scientific-skills |
| [**shap**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/shap) | Explain and audit machine-learning predictions with SHAP. Use for selecting SHAP explainers and maskers,... | K-Dense-AI/claude-scientific-skills |
| [**simpy**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/simpy) | Builds, inspects, tests, and analyzes bounded process-based discrete-event simulations with SimPy. Use for event scheduling, resource queues,... | K-Dense-AI/claude-scientific-skills |
| [**stable-baselines3**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/stable-baselines3) | Trains and evaluates single-agent reinforcement learning with Stable Baselines3 (PPO, SAC, DQN, TD3, DDPG, A2C), Gymnasium custom environments,... | K-Dense-AI/claude-scientific-skills |
| [**statistical-analysis**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/statistical-analysis) | Guided statistical analysis for research data - test selection, assumption checking, effect sizes, power analysis, Bayesian alternatives,... | K-Dense-AI/claude-scientific-skills |
| [**statistical-power**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/statistical-power) | Calculates sample sizes and statistical power for study planning. Applies when someone asks "how many subjects/samples/replicates do I need",... | K-Dense-AI/claude-scientific-skills |
| [**statsmodels**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/statsmodels) | Fits and diagnoses Python statistical models including OLS, GLM, discrete and mixed models, ARIMA and SARIMAX. Supports coefficient inference,... | K-Dense-AI/claude-scientific-skills |
| [**sympy**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/sympy) | Performs exact symbolic mathematics with SymPy for algebra, calculus, equation solving, symbolic linear algebra, physics,... | K-Dense-AI/claude-scientific-skills |
| [**tamarind**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/tamarind) | Provides access to a collection of open-source molecular design and structural biology tools on the Tamarind Bio platform,... | K-Dense-AI/claude-scientific-skills |
| [**tellurium**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/tellurium) | Simulates biochemical kinetic models from SBML or Antimony with Tellurium and libRoadRunner, checks model units,... | K-Dense-AI/claude-scientific-skills |
| [**tiledbvcf**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/tiledbvcf) | Stores and retrieves genomic variant calls with TileDB-VCF. Use for indexed single-sample VCF/BCF ingestion, incremental cohorts,... | K-Dense-AI/claude-scientific-skills |
| [**timesfm-forecasting**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/timesfm-forecasting) | Performs zero-shot time-series forecasting with Google's TimesFM, including regular-grid CSV preparation, quantile forecasts, XReg covariates,... | K-Dense-AI/claude-scientific-skills |
| [**torch-geometric**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/torch-geometric) | Supports PyTorch Geometric (PyG) graph neural networks — node/link/graph classification, message passing (GCN, GAT, GraphSAGE, GIN),... | K-Dense-AI/claude-scientific-skills |
| [**torchdrug**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/torchdrug) | Builds and troubleshoots TorchDrug 0.2.1 workflows for molecular graphs, property prediction, self-supervised pretraining, molecule generation,... | K-Dense-AI/claude-scientific-skills |
| [**transformers**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/transformers) | Hugging Face Transformers for loading Hub models, running pipeline inference, text generation, and Trainer fine-tuning on NLP, vision, audio,... | K-Dense-AI/claude-scientific-skills |
| [**treatment-plans**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/treatment-plans) | Formats and structurally validates local treatment-plan documentation after clinical decisions have already been supplied and verified by authorize... | K-Dense-AI/claude-scientific-skills |
| [**umap-learn**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/umap-learn) | Applies UMAP-learn to nonlinear dimensionality reduction, 2D/3D embeddings, clustering preprocessing, supervised or semi-supervised UMAP, DensMAP,... | K-Dense-AI/claude-scientific-skills |
| [**uncertainty-and-units**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/uncertainty-and-units) | Tracks physical units and propagates measurement uncertainty in scientific calculations using pint and uncertainties.... | K-Dense-AI/claude-scientific-skills |
| [**usfiscaldata**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/usfiscaldata) | Queries the U.S. Treasury Fiscal Data REST API for federal financial data. No API key required. Use for national debt (Debt to the Penny),... | K-Dense-AI/claude-scientific-skills |
| [**vaex**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/vaex) | Processes large tabular scientific datasets with Vaex expressions, filtered views, streamed statistics, binned visualizations,... | K-Dense-AI/claude-scientific-skills |
| [**venue-templates**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/venue-templates) | Prepares journal manuscripts, conference papers, research posters,... | K-Dense-AI/claude-scientific-skills |
| [**waypoint-bio**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/waypoint-bio) | Supports work with Outpost Bio's open microbiome foundation models - the Waypoint checkpoints (Waypoint-6m, Waypoint-45m, Waypoint-170m),... | K-Dense-AI/claude-scientific-skills |
| [**what-if-oracle**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/what-if-oracle) | Supports structured what-if scenario analysis for research planning, experimental contingencies, and scientific project decisions.... | K-Dense-AI/claude-scientific-skills |
| [**zarr-python**](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/skills/zarr-python) | Stores and queries chunked N-D scientific arrays with Zarr-Python 3, including codecs, sharding, S3/GCS storage,... | K-Dense-AI/claude-scientific-skills |

### 前端 / 设计

| Skill | 描述 | 来源 |
|---|---|---|
| [**brandkit**](https://github.com/nexu-io/open-design/tree/main/skills/brandkit) | Generate premium brand-kit imagery: brand-guidelines boards, logo systems, identity decks, visual-world presentations; minimalist, cinematic,... | nexu-io/open-design |
| [**brutalist-skill**](https://github.com/nexu-io/open-design/tree/main/skills/brutalist-skill) | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast,... | nexu-io/open-design |
| [**frontend-design**](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography,... | anthropics/skills |
| [**frontend-dev**](https://github.com/minimax-ai/skills/tree/main/skills/frontend-dev) | Build complete, visually striking web pages: premium UI design, cinematic animations, AI-generated media, conversion copy, generative art.... | minimax-ai/skills |
| [**frontend-slides**](https://github.com/zarazhangrui/frontend-slides) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation,... | zarazhangrui/frontend-slides |
| [**fullstack-dev**](https://github.com/minimax-ai/skills/tree/main/skills/fullstack-dev) | Full-stack architecture guide: apps with REST/JSON APIs, backend services, CRUD/real-time/chat features (Express, Next.js, Node, Python, Go),... | minimax-ai/skills |
| [**gpt-tasteskill**](https://github.com/nexu-io/open-design/tree/main/skills/gpt-tasteskill) | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure,... | nexu-io/open-design |
| [**guizang-ppt-skill**](https://github.com/op7418/guizang-ppt-skill) | 生成横向翻页网页 PPT（单 HTML 文件），含 WebGL 背景、演讲者视图、观众屏同步、讲稿备注、章节幕封、数据大字报、图片网格等模板。... | op7418/guizang-ppt-skill |
| [**image-to-code-skill**](https://github.com/nexu-io/open-design/tree/main/skills/image-to-code-skill) | Image-to-code for Codex web work: generate section-level design images first, analyze them,... | nexu-io/open-design |
| [**imagegen-frontend-mobile**](https://github.com/nexu-io/open-design/tree/main/skills/imagegen-frontend-mobile) | Generate premium app-native mobile screen concepts and flows as images: iOS/Android, clean hierarchy, multi-screen consistency,... | nexu-io/open-design |
| [**imagegen-frontend-web**](https://github.com/nexu-io/open-design/tree/main/skills/imagegen-frontend-web) | Generate premium website design references as images: one horizontal image per section, varied composition and hero scale, one consistent palette.... | nexu-io/open-design |
| [**minimalist-skill**](https://github.com/nexu-io/open-design/tree/main/skills/minimalist-skill) | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. | nexu-io/open-design |
| [**output-skill**](https://github.com/nexu-io/open-design/tree/main/skills/output-skill) | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly.... | nexu-io/open-design |
| [**redesign-skill**](https://github.com/nexu-io/open-design/tree/main/skills/redesign-skill) | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns,... | nexu-io/open-design |
| [**soft-skill**](https://github.com/nexu-io/open-design/tree/main/skills/soft-skill) | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures,... | nexu-io/open-design |
| [**stitch-skill**](https://github.com/nexu-io/open-design/tree/main/skills/stitch-skill) | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium,... | nexu-io/open-design |
| [**taste-skill**](https://github.com/nexu-io/open-design/tree/main/skills/taste-skill) | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction,... | nexu-io/open-design |
| [**taste-skill-v1**](https://github.com/nexu-io/open-design/tree/main/skills/taste-skill-v1) | The original v1 taste-skill, preserved for projects depending on its exact behavior.... | nexu-io/open-design |

### 图表 / 可视化

| Skill | 描述 | 来源 |
|---|---|---|
| [**architecture-diagram-generator**](https://github.com/Cocoon-AI/architecture-diagram-generator/tree/main/architecture-diagram) | Create polished dark-themed architecture diagrams as self-contained HTML+SVG files. Use when the user asks for system, infrastructure, cloud,... | Cocoon-AI/architecture-diagram-generator |
| [**diagram-design**](https://github.com/cathrynlavery/diagram-design/tree/main/skills/diagram-design) | Create branded architecture, flow, sequence, ER, timeline, org-chart, Sankey, Wardley and service-blueprint diagrams (40+ types) as HTML/SVG/PNG,... | cathrynlavery/diagram-design |
| [**drawio-reconstruction**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/drawio-reconstruction) | Rebuild reference images (research figures, architecture diagrams, slides,... | HKUSTDial/Supervisor-Skills |
| [**excalidraw-diagram-generator**](https://github.com/github/awesome-copilot/tree/main/skills/excalidraw-diagram-generator) | Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make a flowchart", "visualize a process",... | github/awesome-copilot |
| [**fireworks-tech-graph**](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | Create precise SVG technical diagrams, export PNG or offline HTML, and animate supported semantic SVGs to GIF. Use for architecture, UML, agent,... | yizhiyanhua-ai/fireworks-tech-graph |
| [**ggplot2-pub**](https://github.com/zhjx19/ggplot2-pub) | 出版级 ggplot2 图表：在 R 中生成、修复或审查达到论文/报告出版标准的统计图。 当用户要求画图、作图、出图、生成图表、论文 figure、按审稿意见改图（字太小/标签重叠/配色乱）、 或用 ggsave 导出图片时使用。... | zhjx19/ggplot2-pub |
| [**lieflat-charts**](https://github.com/larashero3-dotcom/lieflat-charts) | 一套模板驱动的数据可视化与报告生成 skill，既能严格从 Lupi、Basics、Glance、Maps 与 Interactive gallery 的真实实现生成 HTML 图表，也能从 12 套中英文整页报告模板生成可发布的 HTML 报告；以 Mono 为保底，能按数据语义自动选择内置... | larashero3-dotcom/lieflat-charts |

### 文档 / 办公

| Skill | 描述 | 来源 |
|---|---|---|
| [**gif-sticker-maker**](https://github.com/minimax-ai/skills/tree/main/skills/gif-sticker-maker) | Convert photos (people, pets, objects, logos) into 4 animated GIF stickers with captions. Use when: user wants to create cartoon stickers,... | minimax-ai/skills |
| [**minimax-docx**](https://github.com/minimax-ai/skills/tree/main/skills/minimax-docx) | Create, edit and format Word .docx documents with OpenXML SDK: build from scratch, fill or modify existing docs,... | minimax-ai/skills |
| [**minimax-pdf**](https://github.com/minimax-ai/skills/tree/main/skills/minimax-pdf) | Generate print-ready, designed PDFs (reports, proposals, resumes, cover pages), fill PDF form fields,... | minimax-ai/skills |
| [**minimax-xlsx**](https://github.com/minimax-ai/skills/tree/main/skills/minimax-xlsx) | Create, read, analyze, edit or validate Excel files (.xlsx, .xlsm, .csv): build workbooks, edit with zero format loss, recalculate formulas,... | minimax-ai/skills |
| [**ppt-master**](https://github.com/hugohe3/ppt-master/tree/main/skills/ppt-master) | Build editable PPTX decks: generate or reconstruct slides, reusable Brand/Style/Layout/Deck workspaces, fill native templates,... | hugohe3/ppt-master |
| [**pptx-generator**](https://github.com/minimax-ai/skills/tree/main/skills/pptx-generator) | Generate, edit, and read PowerPoint presentations. Create from scratch with PptxGenJS (cover, TOC, content, section divider, summary slides),... | minimax-ai/skills |

### 学术写作 / 文献综述

| Skill | 描述 | 来源 |
|---|---|---|
| [**benchmark-paper-template**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/benchmark-paper-template) | Structure a Benchmark/Evaluation paper with the five-pillar framework (gap, construction pipeline, evaluation, findings,... | HKUSTDial/Supervisor-Skills |
| [**deep-research**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/deep-research) | Survey-grade literature investigation: freeze research questions, search from adversarial perspectives, verify every citation,... | HKUSTDial/Supervisor-Skills |
| [**figure-designer**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/figure-designer) | Design the three core paper figures, Motivated Example (Fig. 1), Solution Overview, Experimental Results: pick paradigm, layout, labels and tool,... | HKUSTDial/Supervisor-Skills |
| [**idea-evaluator**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/idea-evaluator) | Evaluate a draft research idea on Higher/Faster/Stronger/Cheaper/Broader, lifecycle and capability fit,... | HKUSTDial/Supervisor-Skills |
| [**intro-drafter**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/intro-drafter) | Draft a technical paper's Introduction as flowing prose via a six-paragraph logic (background, limitations, problem, challenges, solution,... | HKUSTDial/Supervisor-Skills |
| [**literature-review**](https://github.com/taoyunudt/literature-review-skill) | 帮助用户撰写高质量的文献综述类论文。提供从选题、文献检索、评估筛选、结构规划到最终写作的全流程指导。适用于需要撰写独立文献综述论文或学术论文中文献综述部分的用户。 | taoyunudt/literature-review-skill |
| [**paper-abstract**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-abstract) | Paper 摘要提炼：从已完成的论文正文提炼摘要与关键词，每句可追溯回出处、不夸大结果、不代写正文。用户说写摘要、提炼摘要、abstract、关键词、学位论文摘要时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-anchor**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-anchor) | Paper 文献支撑补齐：统计引用密度定位零引用段，按五类摘出论断并检索真实候选，摆字段级比对供你判定。导师说缺文献支撑、这段要不要加引用、文献综述不足时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-daily**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-daily) | Paper 每日学术雷达：抢发检测与新发论文泛读，arXiv 自动轨加多源补充轨。用户问今天 arXiv 有什么新论文、这个 idea 还能做吗、最近一周新论文时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-disclose**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-disclose) | Paper AI 使用说明：只读 .paper/ 真实留痕，按四级辅助级别汇编可对外披露的 AI 使用说明，不编造留痕。用户说要交 AI 披露、AIGC 误判申诉、列一下用了哪些 AI 时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-doctor**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-doctor) | Paper 环境体检：一条命令查运行环境、数据源 API、网络、凭证、缓存五维就绪度，只体检不代修。用户说 doctor、体检、自检、能不能用、为什么核验不了时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-draft**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-draft) | Paper 分段正文共写：基于大纲与文献笔记逐段起草，每段挂真实锚点、无支撑处标注。用户说这段正文怎么写、基于大纲写正文、这一段写不下去时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-figure**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-figure) | Paper 图表诊断与设计建议：图类、图注、配色、坐标轴、色盲友好的常见选项陈列，摆事实不推荐。用户问图表有什么问题、该画什么图、配色怎么选、figure 帮我看看时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-help**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-help) | Paper 命令导航：问清你想做什么，推荐 1-3 个最匹配命令并说明理由，只导航不代执行。用户问 Paper 能做什么、有哪些命令、该用哪个命令、怎么用时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-import**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-import) | Paper 题录整理：导入知网、Zotero、EndNote 题录并核对题录与草稿引用的一致性，字段缺失标占位、不凭记忆补全。用户说整理题录、参考文献整理、引用管理时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-init**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-init) | Paper 项目脚手架：为新研究项目建标准科研工作目录（README、.gitignore、project.paper.yaml），方案确认前零创建。用户说新建研究项目、初始化论文目录时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-logic**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-logic) | Paper 论证链检查：核对 RQ 到方法、结果、结论的结构对应与闭环，只核结构不核真伪、不下价值判断。用户问论文逻辑完整吗、RQ 和结论对应吗、结论有没有超出结果时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-method**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-method) | Paper 研究设计参谋：检查方法与 RQ 的匹配维度，或摆方法类常见项供你拍板；涉人类被试强制列伦理审查提示。用户说方法怎么选、问卷能回答我的问题吗、要伦理审查吗时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-outline**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-outline) | Paper 大纲共写：基于 RQ 与文献笔记起草带锚点的章节大纲，无支撑处标纯结构占位，结构由你逐章拍板。用户说把论文大纲列一下、章节怎么分、论文怎么组织时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-plot**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-plot) | Paper 绘图代码生成：柱状、折线、散点、箱线、误差线、直方图、热图的 matplotlib 或 ggplot2 代码，配色取公开色板。用户说生成绘图代码、帮我写画图脚本、给我一个 matplotlib 脚本时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-polish**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/paper-polish) | Polish academic prose while preserving meaning: grammar, flow, tone vs evidence, AI-tone removal,... | HKUSTDial/Supervisor-Skills |
| [**paper-proposal**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-proposal) | Paper 开题报告组装：从 topic、literature、method 产物提取片段，按中文学位论文开题节点摆骨架，自有内容标占位。用户说写开题报告、开题要准备什么、选题依据怎么写时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-review**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-review) | Paper 模拟评审：以期刊审稿、盲审、答辩委员视角陈列常见意见并分项评分，标模拟、不下录用判断，不受理他人在审稿件。用户说模拟评审、预审论文、盲审会挂吗时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-revise**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-revise) | Paper 修订辅助：基于审稿意见出修订对照表与逐点回复信候选措辞，采纳与否由你逐条拍板。用户说写回复信、审稿意见怎么回、逐点回复怎么写、改稿建议时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-screen**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-screen) | Paper 系统综述筛选：PRISMA 2020 筛选台账与流程图，纳入排除由你逐篇拍板，流程图数字由脚本算出。用户说做系统综述、纳排标准怎么定、要 PRISMA 流程图时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-search**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-search) | Paper 文献检索：Crossref、OpenAlex、Semantic Scholar、arXiv 自动检索，中文走知网万方检索方案，支持滚雪球与按作者检索、查 OA 与 PMC 全文。用户说帮我查文献、找研究缺口、谁引用了这篇时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-style**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-style) | Paper 风格校准：由脚本机械算出句长、虚词密度、引用位置等特征并解读，建立个人文风基线，不服务降 AI 率。用户说文风统不统一、这几章不像一个人写的、被判成 AI 怎么办时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-submit**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-submit) | Paper 投稿准备：陈列目标期刊常见要求类目，整理投稿材料清单与 cover letter 要点骨架，不替你选刊。用户说要投稿了、投稿要交什么、cover letter 怎么写时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-topic**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-topic) | Paper 选题澄清：逐层给该方向常见研究问题供你拍板，收敛出你的 RQ，不推荐不排序。用户说不知道研究什么、你看这个题行不行、帮我想研究什么时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-typeset**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-typeset) | Paper 出版链：Markdown 转 LaTeX、DOCX、PDF 并渲染 GB/T 7714 参考文献，只换容器不改一字。用户说投稿要 Word 版、转成 LaTeX、导出 docx、出个 PDF 时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-verify**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-verify) | Paper 引用核验：逐条调真实 API 判六态（已核实、元数据不符、已撤稿、未找到、无法核实、待人工核对），中文文献只标待人工核对，并查结论是否夸大。用户说查引用是不是真的、核对 DOI、投稿前自查时使用。 | cabbage2000-lab/paper-tutor-skills |
| [**paper-writer**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/paper-writer) | Draft paper prose from the author's own materials, from a paragraph to a full manuscript; every claim traces to user input or verified sources,... | HKUSTDial/Supervisor-Skills |
| [**pre-submission-reviewer**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/pre-submission-reviewer) | Pre-submission review of a technical paper across logic, writing details, grammar,... | HKUSTDial/Supervisor-Skills |
| [**rebuttal-guidance**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/rebuttal-guidance) | Peer-review rebuttal guidance, not full rebuttal prose: match the reviewer's mindset, recommend a strategy,... | HKUSTDial/Supervisor-Skills |
| [**tech-paper-template**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/tech-paper-template) | Plan a technical paper's logical skeleton with a thinking-template table (background, limitations, key idea, challenges, modules,... | HKUSTDial/Supervisor-Skills |
| [**vibe-research-workflow**](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/vibe-research-workflow) | Guide AI-assisted research (Vibe Coding, Vibe Figure, Vibe Writing): you keep academic judgment,... | HKUSTDial/Supervisor-Skills |

### 知识管理 / Obsidian

| Skill | 描述 | 来源 |
|---|---|---|
| [**defuddle**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/defuddle) | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens.... | mdwoicke/obsidian-skills |
| [**ima-skill**](https://github.com/daymade/claude-code-skills/tree/main/ima-copilot) | Install, troubleshoot and personalize the official Tencent IMA skill: configure ima-skill and API keys,... | daymade/claude-code-skills |
| [**json-canvas**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/json-canvas) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files,... | mdwoicke/obsidian-skills |
| [**kb-ops**](./skills/kb-ops) | 本地知识库运维。当用户要新建知识库、采集资料入库（论文/Zotero/网页/笔记/RSS）、把 raw 记录编译成 wiki 页、校验库契约、看库状态、或排查知识库脚本报错时，使用此 skill。... | 自定义 |
| [**obsidian-bases**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/obsidian-bases) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files,... | mdwoicke/obsidian-skills |
| [**obsidian-cli**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/obsidian-cli) | Operate an Obsidian vault from the CLI: read, create, search and manage notes, tasks and properties; develop and debug plugins and themes,... | mdwoicke/obsidian-skills |
| [**obsidian-markdown**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/obsidian-markdown) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax.... | mdwoicke/obsidian-skills |

### 个人技能集（ljg-*）

| Skill | 描述 | 来源 |
|---|---|---|
| [**ljg-blind**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-blind) | 盲区扫描：读昨天你与 AI 的全部对话，照出让你看不见某类真相的思维习惯，再从微信读书挑一章精准补上，落成分析笔记。用户说扫盲区、盲区、照盲区时使用，可传日期；不用于深钻观点或降秩。 | lijigang/ljg-skills |
| [**ljg-book**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-book) | 拆书：给书名、PDF、EPUB 或节选，讲清全书跟着什么走、主线怎么连、证据如何改变理解，保留书的具体内容而非只给通用结论，默认存 Org 笔记。用户说拆书、分析这本书、这本书在讲什么、压缩一本书时使用。 | lijigang/ljg-skills |
| [**ljg-card**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-card) | Content caster (铸). Transforms text into PNG through precise HTML typography and, when the mold needs it, generated raster imagery.... | lijigang/ljg-skills |
| [**ljg-classic**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-classic) | 古文逐字注解、组合排版、章节意旨图与全章解读生成器。把原文、字词注、句义注、无字顶部配图和章节解读排成一张可读的长 PNG。USE WHEN 用户调用 ljg-classic OR 要求给文言文、古诗文、经史子集做逐字注解、彩色夹注、章节解读、古文讲义图、章节配图。... | lijigang/ljg-skills |
| [**ljg-constraint**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-constraint) | 给领域/专业/角色/产品/争论找真正框住它的几条约束，判世界/规则/解释（硬/软/自设），看约束如何定义身份、框出解空间。用户说找约束、本质约束、硬约束还是自设约束、边界在哪、constraint 时使用；不用于降秩或纵向深钻。 | lijigang/ljg-skills |
| [**ljg-explain**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-explain) | 把概念、公式、机制与原理讲到能辨认、能推导、能迁移：用通俗中文接通具体情境、判别依据、运作过程和成立条件。USE WHEN 用户调用 ljg-explain、说「通俗易懂地讲解」「讲透这个概念或公式」「费曼讲解」「ELI5」，或希望从零理解一个知识点并能用于新情境。... | lijigang/ljg-skills |
| [**ljg-invest**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-invest) | 投资分析。给一个项目（公司名、BP、创始人对话记录），写一份深度投资分析报告。不走传统投资分析的路——核心判断只有一个：这个项目是不是一台「秩序创造机器」。Use when user says '投资报告', '投资分析', '分析这个项目', '写投资报告',... | lijigang/ljg-skills |
| [**ljg-is**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-is) | 把一个名词或概念写成可使用的理解：先用普通话讲清它是什么、与相邻概念差在哪里，再说明它怎样运作、会改写什么判断，最后给出面对它时的行动抓手。USE WHEN 用户问 X 是什么、怎么理解、意味着什么、为什么重要、以后怎样判断或使用；尤其适合技术概念、制度、产品、角色、方法、规范与实践。... | lijigang/ljg-skills |
| [**ljg-learn**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-learn) | 概念解剖：从历史、辩证、现象学、语言学、形式化、存在主义、美学、元哲学八个维度拆解一个概念，收敛成顿悟，输出 org 笔记。用户说解剖概念、概念解剖、explain concept、/ljg-learn 时使用。 | lijigang/ljg-skills |
| [**ljg-paper**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-paper) | 讲论文：给 arXiv 链接、PDF 或论文题目，讲清研究了什么、作者贡献、结论如何得出、证据没证明什么，默认存 Org 笔记。用户说要读、分析或理解一篇论文时使用；不做复现、正式同行评审或文献综述。 | lijigang/ljg-skills |
| [**ljg-present**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-present) | Unix 气质的演讲设计与保真排版。把 Org/Markdown 提纲或经授权提炼的讲稿制成单文件离线 HTML；以语义角色选择巨句、对照、Unicode 关系图、证据与章节版式。默认深色，支持讲稿层、原生图表与翻页笔。... | lijigang/ljg-skills |
| [**ljg-push**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-push) | 把 ~/.agents/skills/ljg-* 里所有更新过的 skills 同步到 github repo (ljg-skills)，先推 master 分支（org-mode 输出风格），再切 md 分支（markdown 输出风格）做基础 markdown 化后推。... | lijigang/ljg-skills |
| [**ljg-qa**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-qa) | 信息提问机：把文章/论文/书的核心观点抽成 Q-A 对，问题切要害、答案简洁有收口，读者顺着 Q 链复现作者推理。用户说问答、Q&A、QA、提问、抽取问题时使用；不用于 FAQ、术语表或阅读理解题。 | lijigang/ljg-skills |
| [**ljg-rank**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-rank) | 给一个领域，找出背后真正撑着它的几根独立的力。十几个现象砍到不可再少的生成器——砍完能把现象一个个生回来，才算数。Use when user says '降秩', '找秩', '秩是什么', '这个领域靠什么撑着', '背后是什么',... | lijigang/ljg-skills |
| [**ljg-read**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-read) | 用《学习观》的「下上结构」讲透用户提供的文本：从具体情境接通概念、判别依据与有条件的关系，让读者理解原意并能迁移判断；默认直接在对话中展示。USE WHEN 用户说「伴读」「陪我读」「读这篇」「讲透这段」「read with me」或提供文本希望深入浅出地讲解。... | lijigang/ljg-skills |
| [**ljg-relationship**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-relationship) | Relationship analyst combining structural diagnostics (5-layer framework) with psychoanalytic depth (transference, unconscious patterns,... | lijigang/ljg-skills |
| [**ljg-roundtable**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-roundtable) | 一个议题，一场圆桌：主持人请来 3-5 位真实人物，定义开场，逐轮交锋， 每轮收一张 ASCII 结构图，用户用指令控节奏（可/止/深入此节/引入新人物）， 散场后全文存入 org 笔记。Use when user says "圆桌讨论", "圆桌", "roundtable", "辩论",... | lijigang/ljg-skills |
| [**ljg-structure**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-structure) | 找出一段信息中母题级别的结构，把抽象关系展开回具体可见的现象，再用风洞检验关键因果与边界。USE WHEN user says '找结构', '母题是什么', '结构风洞', '背后的结构', '不要只做AB测试',... | lijigang/ljg-skills |
| [**ljg-think**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-think) | 追本之箭——纵向深钻思维工具。给一个观点、现象或问题，像箭一样一路向下钻到不可再分的本质。Use when user says '想透', '追本', '本质是什么', '为什么会这样', '深挖', '钻到底', 'think deep', 'drill down',... | lijigang/ljg-skills |
| [**ljg-word**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-word) | Deep-dive English word mastery tool. Deconstructs a single English word into core semantics and epiphany.... | lijigang/ljg-skills |
| [**ljg-writes**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-writes) | 写作引擎。把一个观点写成可理解、可迁移、经得住反例的 1000-1500 字中文文章。USE WHEN 写文章 OR 优化思想内容 OR 展开观点 OR 改写成逻辑递进的中文。NOT FOR 普通摘要、事实查询或结构风洞（用 ljg-structure）。 | lijigang/ljg-skills |

### Meta / 效率工具

| Skill | 描述 | 来源 |
|---|---|---|
| [**find-skills**](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...",... | vercel-labs/skills |
| [**score**](https://github.com/getkrafter/resume-toolkit/tree/master/skills/score) | Score a resume for quality and ATS keyword match. With a JD, also performs gap analysis and keyword tailoring.... | getkrafter/resume-toolkit |
| [**skill-creator**](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit,... | anthropics/skills |
| [**travel-planner**](https://github.com/ailabs-393/ai-labs-claude-skills/tree/main/packages/skills/travel-planner) | Plan trips: collect budget, style, interests and dietary needs, then produce day-by-day itineraries, budget breakdowns, packing checklists,... | ailabs-393/ai-labs-claude-skills |
| [**writing-rules**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify/skills/writing-rules) | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule",... | anthropics/claude-plugins-official |

### 插件附带 Skills

| Skill | 描述 | 来源 |
|---|---|---|
| [**claude-automation-recommender**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup/skills/claude-automation-recommender) | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers).... | anthropics/claude-plugins-official |
| [**claude-md-improver**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management/skills/claude-md-improver) | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files.... | anthropics/claude-plugins-official |
| [**frontend-design**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design/skills/frontend-design) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography,... | anthropics/claude-plugins-official |
| [**writing-rules**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify/skills/writing-rules) | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule",... | anthropics/claude-plugins-official |
| [**session-report**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report/skills/session-report) | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills,... | anthropics/claude-plugins-official |
| [**skill-creator**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator/skills/skill-creator) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit,... | anthropics/claude-plugins-official |
| [**paper-knowledge-online**](https://github.com/wtbxsjy/paper-knowledge/tree/main/skills/paper-knowledge-online) | Verify and convert paper references (DOI/arXiv/PMID or title) into checked metadata and full-text Markdown: two-source metadata check,... | wtbxsjy/paper-knowledge |

### 自定义 Skills（无公开源）

| Skill | 描述 | 来源 |
|---|---|---|
| [**modern-r**](./skills/modern-r) | Modernize and review existing R code using current idioms and migration priorities across tidyverse, tidy evaluation, style, and performance.... | 自定义 |
| [**r-skill-changelog-sync**](./skills/r-skill-changelog-sync) | Refresh R skills against upstream package changes by checking CRAN package and NEWS pages,... | 自定义 |

## Skill 来源与更新

每个 skill 都对应一个上游 GitHub 仓库（完整映射见 [SOURCES.md](./SOURCES.md) / [SOURCES.tsv](./SOURCES.tsv)）。上游发布新版本后：

```bash
bash update-skills.sh              # 同步全部 skills/ 与 plugin-skills/
bash update-skills.sh taste-skill  # 只同步某一个 skill
git add -A && git commit -m "Update skills" && git push
```

同步会把上游的长 description 一并带回来。`update-skills.sh` 结束时会按 [descriptions.slim.json](./descriptions.slim.json) 自动把精简版写回（需要 `python3`）。
手动精简了某个 skill 的 description 之后，用 `python3 tools/slim-descriptions.py capture <skill-dir>` 登记；`python3 tools/slim-descriptions.py status` 列出不同步的条目和尚未精简的长 description。

## 多环境同步策略

1. **Skills**：通过 Git 管理，`.cc-switch` 在新机器上做符号链接激活
2. **Plugins**：`setup.ps1` / `setup.sh` 自动安装
3. **Settings**：`settings.template.json` 作为模板，本地密钥保存在 `settings.local.json`（不提交）
4. **Hooks**：通过 plugin 管理，配置文件备份在 `config/hooks/`

## Contributing

- 添加新 skill：放入 `skills/<name>/`，并在 `SOURCES.tsv` 中登记上游仓库后提交
- 同步上游更新：运行 `bash update-skills.sh` 后提交（被精简过的 description 会自动写回，上游改写了描述时会提示复核）
- 自定义 skill（无公开源）：保留在仓库中，并在 `SOURCES.tsv` 中标注 `CUSTOM`
