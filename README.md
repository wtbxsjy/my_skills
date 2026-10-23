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
| [**cli**](https://github.com/posit-dev/skills/tree/main/r-lib/r-cli) | Comprehensive R package for command-line interface styling, semantic messaging, and user communication.... | posit-dev/skills |
| [**cran-extrachecks**](https://github.com/posit-dev/skills/tree/main/r-lib/r-cran-extrachecks) | Prepare R packages for CRAN submission by checking for common ad-hoc requirements not caught by devtools::check().... | posit-dev/skills |
| [**create-release-checklist**](https://github.com/posit-dev/skills/tree/main/open-source/create-release-checklist) | Create a release checklist and GitHub issue for an R package. Use when the user asks to "create a release checklist" or "start a release" for an R... | posit-dev/skills |
| [**gt-xlsx-roundtrip**](./skills/gt-xlsx-roundtrip) | 在带格式的 Excel 电子表格（.xlsx）与 R 语言 gt 表格对象之间双向转换，使用 forgts（电子表格 → gt）和 gtxlsx（gt → 电子表格）。... | 自定义 |
| [**lifecycle**](https://github.com/posit-dev/skills/tree/main/r-lib/r-lifecycle) | Guidance for managing R package lifecycle according to tidyverse principles using the lifecycle package.... | posit-dev/skills |
| [**mirai**](https://github.com/posit-dev/skills/tree/main/r-lib/r-mirai) | Help users write correct R code for async, parallel, and distributed computing using mirai.... | posit-dev/skills |
| [**r-bayes**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-bayes) | Patterns for Bayesian inference in R using brms, including multilevel models, DAG validation, and marginal effects.... | ab604/claude-code-r-skills |
| [**r-cli-app**](https://github.com/posit-dev/skills/tree/main/r-lib/r-cli-app) | Build command-line apps in R using the Rapp package. Use when creating a CLI tool in R, adding argument parsing to an R script,... | posit-dev/skills |
| [**r-oop**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-oop) | R object-oriented programming guide for S7, S3, S4, and vctrs. Use when designing R classes or choosing an OOP system. | ab604/claude-code-r-skills |
| [**r-package-development**](https://github.com/posit-dev/skills/tree/main/r-lib/r-package-development) | R package development with devtools, testthat, and roxygen2. Use when the user is working on an R package, running tests, writing documentation,... | posit-dev/skills |
| [**r-performance**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-performance) | R performance best practices including profiling, benchmarking, vctrs, and optimization strategies. Use when optimizing R code. | ab604/claude-code-r-skills |
| [**r-style-guide**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/r-style-guide) | R style guide covering naming conventions, spacing, layout, and function design best practices. Use when writing R code. | ab604/claude-code-r-skills |
| [**release-post**](https://github.com/posit-dev/skills/tree/main/open-source/release-post) | Create professional package release blog posts following Tidyverse or Shiny blog conventions.... | posit-dev/skills |
| [**rlang-patterns**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/rlang-patterns) | rlang metaprogramming patterns for data-masking, injection operators, and dynamic dots. Use when writing functions that use tidy evaluation. | ab604/claude-code-r-skills |
| [**shiny-bslib**](https://github.com/posit-dev/skills/tree/main/shiny/shiny-bslib) | Build modern Shiny dashboards and applications using bslib (Bootstrap 5). Use when creating new Shiny apps, modernizing legacy apps (fluidPage,... | posit-dev/skills |
| [**shiny-bslib-theming**](https://github.com/posit-dev/skills/tree/main/shiny/shiny-bslib-theming) | Advanced theming for Shiny apps using bslib and Bootstrap 5. Use when customizing app appearance with bs_theme(), Bootswatch themes, custom colors,... | posit-dev/skills |
| [**tdd-workflow**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/tdd-workflow) | Test-driven development workflow for R using testthat. Use when writing new features, fixing bugs, or refactoring code.... | ab604/claude-code-r-skills |
| [**testing-r-packages**](https://github.com/posit-dev/skills/tree/main/r-lib/r-testthat) | Best practices for writing R package tests with testthat version 3+.... | posit-dev/skills |
| [**tidyverse-patterns**](https://github.com/ab604/claude-code-r-skills/tree/main/.claude/skills/tidyverse-patterns) | Modern tidyverse patterns for R including pipes, joins, grouping, purrr, and stringr. Use when writing tidyverse R code. | ab604/claude-code-r-skills |

### Quarto / 发布与写作

| Skill | 描述 | 来源 |
|---|---|---|
| [**academic-humanizer**](https://github.com/AIScientists-Dev/academic-humanizer) | Improve the clarity and voice of AI-assisted academic writing (papers, theses, rebuttals) and funding proposals (NSF Project Summary/Description,... | AIScientists-Dev/academic-humanizer |
| [**alt-text**](https://github.com/posit-dev/skills/tree/main/alt-text) | Generate and improve accessible alt text for data visualizations and images in R packages and Quarto documents. Use when the user wants to add,... | posit-dev/skills |
| [**brand-yml**](https://github.com/posit-dev/skills/tree/main/brand-yml) | Create and use brand.yml files for consistent branding across Shiny apps and Quarto documents. Covers: (1) Creating new _brand.yml files,... | posit-dev/skills |
| [**quarto-alt-text**](https://github.com/ai-integr8tor/posit-dev-skills/tree/add-py-shiny-dashboard-skills/quarto/quarto-alt-text) | Generate accessible alt text for data visualizations in Quarto documents. Use when the user wants to add, improve,... | ai-integr8tor/posit-dev-skills |
| [**quarto-authoring**](https://github.com/posit-dev/skills/tree/main/quarto/quarto-authoring) | Use when the user is explicitly working with Quarto, .qmd files, _quarto.yml, Quarto projects, or Quarto features such as callouts,... | posit-dev/skills |
| [**quarto-talks**](https://github.com/alfredo-hs/quarto-talks) | Turn source material into a restrained Quarto RevealJS talk using the quarto-talks format. Use for papers, manuscripts, documents, figures, code,... | alfredo-hs/quarto-talks |

### 数据科学 / 机器学习 / 数据查询

| Skill | 描述 | 来源 |
|---|---|---|
| [**attach-db**](./skills/attach-db) | Attach a DuckDB database file for use with /duckdb-skills:query. Explores the schema (tables, columns,... | 自定义 |
| [**convert-file**](./skills/convert-file) | Convert any data file to another format: CSV, Parquet, JSON, Excel, GeoJSON, and more. Use when the user says "convert to parquet", "save as xlsx",... | 自定义 |
| [**duckdb-2-0**](./skills/duckdb-2-0) | DuckDB 2.0 (LTS "Cinnamon Teal", released 2026-10-21) for agents: check the installed version, use the CLI agent mode (compact Markdown output,... | 自定义 |
| [**duckdb-docs**](./skills/duckdb-docs) | Search DuckDB and DuckLake documentation and blog posts. Returns relevant doc chunks for a question or keyword using full-text search against a loc... | 自定义 |
| [**ggsql**](https://github.com/posit-dev/skills/tree/main/ggsql/ggsql) | Write ggsql queries — a grammar of graphics for SQL. Use when the user wants to create, modify, or understand a ggsql visualization query. | posit-dev/skills |
| [**install-duckdb**](./skills/install-duckdb) | Install or update DuckDB extensions. Each argument is either a plain extension name (installs from core) or name@repo (e.g. magic@community).... | 自定义 |
| [**query**](./skills/query) | Run SQL queries against the attached DuckDB database or ad-hoc against files. Accepts raw SQL or natural language questions.... | 自定义 |
| [**read-file**](./skills/read-file) | Read any data file (CSV, JSON, Parquet, Avro, Excel, spatial, SQLite) or remote URL (S3, HTTPS). Use when user references a data file,... | 自定义 |
| [**read-memories**](./skills/read-memories) | Search past Claude Code session logs to recall prior decisions, patterns, or unresolved work. Use when user says "do you remember",... | 自定义 |
| [**s3-explore**](./skills/s3-explore) | Explore and query data on S3, Cloudflare R2, GCS, MinIO, or any S3-compatible storage. Use when the user mentions an s3://, r2://, gs://,... | 自定义 |
| [**scvi-tools**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scvi-tools) | Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with s... | anthropics/knowledge-work-plugins |
| [**single-cell-rna-qc**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/single-cell-rna-qc) | Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive v... | anthropics/knowledge-work-plugins |
| [**spatial**](./skills/spatial) | Answer questions about spatial data using DuckDB. Use when the user mentions locations, coordinates, lat/lng, distances, maps, addresses, "near",... | 自定义 |
| [**tabular-data-ml**](https://github.com/tidymodels/skills/tree/main/users/tabular-data-ml) | Build machine learning models using tidymodels for tabular data | tidymodels/skills |

### 生物医药 / 文献数据库

| Skill | 描述 | 来源 |
|---|---|---|
| [**alphafold-database-fetch-and-analyze**](https://github.com/google-deepmind/science-skills/tree/main/skills/alphafold_database_fetch_and_analyze) | Retrieve and analyze AlphaFold predicted structures for a protein.... | google-deepmind/science-skills |
| [**alphagenome-single-variant-analysis**](https://github.com/google-deepmind/science-skills/tree/main/skills/alphagenome_single_variant_analysis) | Analyzes genetic variant effects on gene expression (RNA-seq), chromatin accessibility (DNASE), histone marks (ChIP),... | google-deepmind/science-skills |
| [**chembl-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/chembl_database) | Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved drugs, and chemical structures.... | google-deepmind/science-skills |
| [**clinical-trials-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/clinical_trials_database) | Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by condition, drug, location, status,... | google-deepmind/science-skills |
| [**clinvar-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/clinvar_database) | Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Benign, VUS), clinical evidence rationales,... | google-deepmind/science-skills |
| [**credentials**](https://github.com/google-deepmind/science-skills/tree/main/skills/credentials) | Instructions for handling API keys and credentials safely, verifying their presence,... | google-deepmind/science-skills |
| [**dbsnp-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/dbsnp_database) | Use when you want to look up, map, and search for short genetic variants (SNPs, indels) in NCBI's dbSNP database. Resolves between rsIDs,... | google-deepmind/science-skills |
| [**embl-ebi-ols**](https://github.com/google-deepmind/science-skills/tree/main/skills/embl_ebi_ols) | Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, definitions,... | google-deepmind/science-skills |
| [**encode-ccres-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/encode_ccres_database) | Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API,... | google-deepmind/science-skills |
| [**ensembl-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/ensembl_database) | Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or protein sequences, retrieve gene structures (exons),... | google-deepmind/science-skills |
| [**foldseek-structural-search**](https://github.com/google-deepmind/science-skills/tree/main/skills/foldseek_structural_search) | Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API.... | google-deepmind/science-skills |
| [**gnomad-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/gnomad_database) | Query the Genome Aggregation Database (gnomAD). Use when determining the rarity or allele frequency of specific genetic variants,... | google-deepmind/science-skills |
| [**gtex-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/gtex_database) | Use when you want to retrieve quantitative RNA expression data and variant eQTL information from the GTEx (Genotype-Tissue Expression) Project acro... | google-deepmind/science-skills |
| [**human-protein-atlas-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/human_protein_atlas_database) | Use when you want to retrieve semi-quantitative protein expression and spatial localisation data from the Human Protein Atlas (HPA). | google-deepmind/science-skills |
| [**interpro-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/interpro_database) | Identify domains, families, and sites in proteins; find all proteins in a family or sharing a domain; explore species distribution for a domain; an... | google-deepmind/science-skills |
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
| [**protein-sequence-msa**](https://github.com/google-deepmind/science-skills/tree/main/skills/protein_sequence_msa) | Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need to align multiple sequences to assess similarity,... | google-deepmind/science-skills |
| [**protein-sequence-similarity-search**](https://github.com/google-deepmind/science-skills/tree/main/skills/protein_sequence_similarity_search) | Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback).... | google-deepmind/science-skills |
| [**pubchem-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/pubchem_database) | Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics.... | google-deepmind/science-skills |
| [**pubmed-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/pubmed_database) | Search PubMed for scientific literature, including published clinical trials. Fetch abstracts and full text.... | google-deepmind/science-skills |
| [**pymol**](https://github.com/google-deepmind/science-skills/tree/main/skills/pymol) | Visualize, analyze, and render protein and molecular structures using PyMOL. Use when the user wants to create images of protein structures,... | google-deepmind/science-skills |
| [**quickgo-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/quickgo_database) | Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this when you need to map genes to biological processes,... | google-deepmind/science-skills |
| [**reactome-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/reactome_database) | Query the Reactome database (Analysis and Content Services). Use when the user asks about pathway analysis, gene list enrichment,... | google-deepmind/science-skills |
| [**string-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/string_database) | Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology.... | google-deepmind/science-skills |
| [**ucsc-conservation-and-tfbs**](https://github.com/google-deepmind/science-skills/tree/main/skills/ucsc_conservation_and_tfbs) | Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding Sites (TFBS) from the UCSC Genome Browser.... | google-deepmind/science-skills |
| [**unibind-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/unibind_database) | Queries the UniBind database for experimentally validated transcription factor (TF) binding sites.... | google-deepmind/science-skills |
| [**uniprot-database**](https://github.com/google-deepmind/science-skills/tree/main/skills/uniprot_database) | Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and UniRef. Use when searching for proteins,... | google-deepmind/science-skills |
| [**uv**](https://github.com/google-deepmind/science-skills/tree/main/skills/uv) | Checks whether the uv Python package manager is installed and installs it if missing. Ensures uv is on PATH.... | google-deepmind/science-skills |
| [**workflow-skill-creator**](https://github.com/google-deepmind/science-skills/tree/main/skills/workflow_skill_creator) | Distills a completed user workflow or interaction into a reusable agent skill. Use when the user asks to turn their workflow, interaction,... | google-deepmind/science-skills |

### 开发 / 工程 / 工作流

| Skill | 描述 | 来源 |
|---|---|---|
| [**claude-automation-recommender**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup/skills/claude-automation-recommender) | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers).... | anthropics/claude-plugins-official |
| [**claude-md-improver**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management/skills/claude-md-improver) | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files.... | anthropics/claude-plugins-official |
| [**cpp-pro**](https://github.com/Jeffallan/claude-skills/tree/main/skills/cpp-pro) | Writes, optimizes, and debugs C++ applications using modern C++20/23 features, template metaprogramming, and high-performance systems techniques.... | Jeffallan/claude-skills |
| [**critical-code-reviewer**](https://github.com/posit-dev/skills/tree/main/posit-dev/critical-code-reviewer) | Rigorously review code or pull requests for correctness, security, accessibility, maintainability, tests, and edge cases.... | posit-dev/skills |
| [**describe-design**](https://github.com/posit-dev/skills/tree/main/posit-dev/describe-design) | Research a codebase and create architectural documentation describing how features or systems work.... | posit-dev/skills |
| [**implement**](https://github.com/posit-dev/skills/tree/main/posit-dev/implement) | Orchestrates implementation of a plan file by delegating work to subagents in parallel. Verifies git branch state, tracks progress,... | posit-dev/skills |
| [**instrument-data-to-allotrope**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/instrument-data-to-allotrope) | Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV.... | anthropics/knowledge-work-plugins |
| [**karpathy-guidelines**](https://github.com/BurukalaManiReethika/Karpathy-Inspired-Claude-Code-Guidelines/tree/main/skills/karpathy-guidelines) | Six principles for better Claude Code behavior — think before coding, keep it simple, make surgical changes, define success criteria,... | BurukalaManiReethika/Karpathy-Inspired-Claude-Code-Guidelines |
| [**nextflow-development**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/nextflow-development) | Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES,... | anthropics/knowledge-work-plugins |
| [**playwright-cli**](https://github.com/microsoft/playwright-cli/tree/main/skills/playwright-cli) | Automate browser interactions, test web pages and work with Playwright tests. | microsoft/playwright-cli |
| [**pr-create**](https://github.com/posit-dev/skills/tree/main/github/pr-create) | Creates a pull request from current changes, monitors GitHub CI, and debugs any failures until CI passes. Activate when the user says "create pr",... | posit-dev/skills |
| [**pr-threads-address**](https://github.com/posit-dev/skills/tree/main/github/pr-threads-address) | Address PR review feedback by systematically working through every unresolved PR review thread on the current branch's PR - analyze each comment,... | posit-dev/skills |
| [**pr-threads-resolve**](https://github.com/posit-dev/skills/tree/main/github/pr-threads-resolve) | Bulk resolve unresolved PR review threads on the current branch’s PR — typically after threads have been addressed manually or via /pr-threads-address | posit-dev/skills |
| [**rust-skills**](https://github.com/leonardomso/rust-skills) | Comprehensive Rust coding guidelines with 265 rules across 26 categories. Use when writing, reviewing, or refactoring Rust code. Covers ownership,... | leonardomso/rust-skills |
| [**scientific-problem-selection**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scientific-problem-selection) | This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects,... | anthropics/knowledge-work-plugins |
| [**session-report**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report/skills/session-report) | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills,... | anthropics/claude-plugins-official |
| [**start**](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/start) | Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature,... | anthropics/knowledge-work-plugins |
| [**working-on**](https://github.com/posit-dev/skills/tree/main/posit-dev/working-on) | Set a tracking document as the source of truth for the current feature or task. Use when starting work on a feature, bug fix,... | posit-dev/skills |

### 前端 / 设计

| Skill | 描述 | 来源 |
|---|---|---|
| [**brandkit**](https://github.com/nexu-io/open-design/tree/main/skills/brandkit) | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks,... | nexu-io/open-design |
| [**brutalist-skill**](https://github.com/nexu-io/open-design/tree/main/skills/brutalist-skill) | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast,... | nexu-io/open-design |
| [**frontend-design**](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography,... | anthropics/skills |
| [**frontend-dev**](https://github.com/minimax-ai/skills/tree/main/skills/frontend-dev) | Full-stack frontend development combining premium UI design, cinematic animations, AI-generated media assets, persuasive copywriting,... | minimax-ai/skills |
| [**frontend-slides**](https://github.com/zarazhangrui/frontend-slides) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation,... | zarazhangrui/frontend-slides |
| [**fullstack-dev**](https://github.com/minimax-ai/skills/tree/main/skills/fullstack-dev) | Full-stack backend architecture and frontend-backend integration guide. TRIGGER when: building a full-stack app, creating REST API with frontend,... | minimax-ai/skills |
| [**gpt-tasteskill**](https://github.com/nexu-io/open-design/tree/main/skills/gpt-tasteskill) | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure,... | nexu-io/open-design |
| [**guizang-ppt-skill**](https://github.com/op7418/guizang-ppt-skill) | 生成横向翻页网页 PPT（单 HTML 文件），含 WebGL 背景、演讲者视图、观众屏同步、讲稿备注、章节幕封、数据大字报、图片网格等模板。... | op7418/guizang-ppt-skill |
| [**image-to-code-skill**](https://github.com/nexu-io/open-design/tree/main/skills/image-to-code-skill) | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself,... | nexu-io/open-design |
| [**imagegen-frontend-mobile**](https://github.com/nexu-io/open-design/tree/main/skills/imagegen-frontend-mobile) | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android,... | nexu-io/open-design |
| [**imagegen-frontend-web**](https://github.com/nexu-io/open-design/tree/main/skills/imagegen-frontend-web) | Elite frontend image-direction skill for generating premium, conversion-aware website design references.... | nexu-io/open-design |
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
| [**diagram-design**](https://github.com/cathrynlavery/diagram-design/tree/main/skills/diagram-design) | Create branded architecture, architecture delta, IT current-state, flowchart, sequence, state machine, ER/data model, timeline, swimlane, quadrant,... | cathrynlavery/diagram-design |
| [**excalidraw-diagram-generator**](https://github.com/github/awesome-copilot/tree/main/skills/excalidraw-diagram-generator) | Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make a flowchart", "visualize a process",... | github/awesome-copilot |
| [**fireworks-tech-graph**](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | Create precise SVG technical diagrams, export PNG or offline HTML, and animate supported semantic SVGs to GIF. Use for architecture, UML, agent,... | yizhiyanhua-ai/fireworks-tech-graph |
| [**ggplot2-pub**](https://github.com/zhjx19/ggplot2-pub) | 出版级 ggplot2 图表：在 R 中生成、修复或审查达到论文/报告出版标准的统计图。 当用户要求画图、作图、出图、生成图表、论文 figure、按审稿意见改图（字太小/标签重叠/配色乱）、 或用 ggsave 导出图片时使用。... | zhjx19/ggplot2-pub |
| [**lieflat-charts**](https://github.com/larashero3-dotcom/lieflat-charts) | 一套模板驱动的数据可视化与报告生成 skill，既能严格从 Lupi、Basics、Glance、Maps 与 Interactive gallery 的真实实现生成 HTML 图表，也能从 12 套中英文整页报告模板生成可发布的 HTML 报告；以 Mono 为保底，能按数据语义自动选择内置... | larashero3-dotcom/lieflat-charts |

### 文档 / 办公

| Skill | 描述 | 来源 |
|---|---|---|
| [**gif-sticker-maker**](https://github.com/minimax-ai/skills/tree/main/skills/gif-sticker-maker) | Convert photos (people, pets, objects, logos) into 4 animated GIF stickers with captions. Use when: user wants to create cartoon stickers,... | minimax-ai/skills |
| [**minimax-docx**](https://github.com/minimax-ai/skills/tree/main/skills/minimax-docx) | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). Three pipelines: (A) create new documents from scratch,... | minimax-ai/skills |
| [**minimax-pdf**](https://github.com/minimax-ai/skills/tree/main/skills/minimax-pdf) | Use this skill when visual quality and design identity matter for a PDF. CREATE (generate from scratch): "make a PDF", "generate a report",... | minimax-ai/skills |
| [**minimax-xlsx**](https://github.com/minimax-ai/skills/tree/main/skills/minimax-xlsx) | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). Use when the user asks to create, build, modify,... | minimax-ai/skills |
| [**ppt-master**](https://github.com/hugohe3/ppt-master/tree/main/skills/ppt-master) | AI-driven presentation workflow for generating editable PPTX decks and slides, reconstructing page visuals,... | hugohe3/ppt-master |
| [**pptx-generator**](https://github.com/minimax-ai/skills/tree/main/skills/pptx-generator) | Generate, edit, and read PowerPoint presentations. Create from scratch with PptxGenJS (cover, TOC, content, section divider, summary slides),... | minimax-ai/skills |

### 学术写作 / 文献综述

| Skill | 描述 | 来源 |
|---|---|---|
| [**literature-review**](https://github.com/taoyunudt/literature-review-skill) | 帮助用户撰写高质量的文献综述类论文。提供从选题、文献检索、评估筛选、结构规划到最终写作的全流程指导。适用于需要撰写独立文献综述论文或学术论文中文献综述部分的用户。 | taoyunudt/literature-review-skill |
| [**paper-abstract**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-abstract) | Paper 摘要提炼命令（正文→摘要提炼器）。当用户已有论文正文要写摘要、提炼摘要、凝练摘要、生成 abstract、整理论文摘要、学位论文摘要、期刊投稿摘要、关键词，或说"帮我写摘要""从正文提炼摘要""摘要怎么写""我的论文摘要""abstract 帮我弄一下""关键词帮我选几个"时使用—... | cabbage2000-lab/paper-tutor-skills |
| [**paper-anchor**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-anchor) | 文献支撑补齐命令（论断—支撑对照器）。当导师或审稿人说"这段缺文献支撑""文献综述不足""缺少与已有研究的对比"， 或用户要给已写好的论断补引用、问"这句话需要引用吗""哪些段落没引用""帮我找支撑这个观点的文献""我这个论断有没有文献支持" 时使用——即使用户只说"帮我补文献""这段要不要加... | cabbage2000-lab/paper-tutor-skills |
| [**paper-daily**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-daily) | Paper 每日学术雷达命令（抢发检测 + 新发泛读）。当用户手头有研究想法（RQ / 方法 / 想投的会议）、想确认是不是已被人抢发、或想每天泛读该方向新发论文时使用——即使用户只说"今天 arXiv 有什么新论文""这个方向最近有什么新论文""我被人抢发了吗""这个 idea 还能做吗""... | cabbage2000-lab/paper-tutor-skills |
| [**paper-disclose**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-disclose) | Paper AI 使用说明生成命令（披露汇编器）。当用户要写论文投稿的 AI 使用说明、AI 使用披露、AI 辅助声明、学位论文 AIGC 使用报告,... | cabbage2000-lab/paper-tutor-skills |
| [**paper-doctor**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-doctor) | Paper 环境就绪度体检命令。当用户要检查 Paper 核验/检索环境能不能用、数据源通不通、凭证配没配、运行环境是否满足要求，或说 doctor / 体检 / 自检 / 环境检查 / 能不能用 / 跑不跑得起来 / 为什么核验不了 时使用——即使用户只说"这个工具到底能不能用"也应使用。... | cabbage2000-lab/paper-tutor-skills |
| [**paper-draft**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-draft) | Paper 分段正文共写命令（段落正文初稿共写器）。当用户已有论文大纲（/paper-outline 产物或手写大纲）、要逐段展开正文、起草段落、写论文正文、把大纲要点展开成段，或说"帮我把这段引言写一下""这段正文怎么展开""基于大纲写一段方法""我有大纲了、想写正文"时使用——即使用户只说... | cabbage2000-lab/paper-tutor-skills |
| [**paper-figure**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-figure) | Paper 图表可视化辅助命令（B 诊断 + C 设计建议双模式自适应）。当用户要查图表、图表诊断、图表设计、画图建议、该用什么图、图注怎么写、配色选什么、色盲友好、坐标轴规范、误差棒标注，或说"帮我看看这张图""图表有什么问题""我该画什么图""配色怎么选""figure 帮我查一下""画图... | cabbage2000-lab/paper-tutor-skills |
| [**paper-help**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-help) | Paper 命令导航器。当用户问 Paper 能做什么、有哪些命令、该用哪个命令，或说 help / 帮助 / 怎么用 / 命令一览 / 不知道从哪开始时使用——即使用户只说"我想写论文但不知道用什么"也应使用。... | cabbage2000-lab/paper-tutor-skills |
| [**paper-import**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-import) | Paper 题录导入命令（题录整理器 + 题录-草稿一致性核对器）。当用户有从知网/Zotero/EndNote 导出的题录要批量整理、整理参考文献、题录入库、做题录与草稿引用的一致性核对、查哪些草稿引用有对应题录、查题录与草稿字段差异，或说"帮我整理题录""知网题录导入""Zotero 题录... | cabbage2000-lab/paper-tutor-skills |
| [**paper-init**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-init) | 为研究项目搭建标准科研工作目录的脚手架命令。当用户要开始一个新研究项目或新论文、想初始化或规范科研项目的目录结构、要搭多项目科研工作区，或提到 paper-init、科研工作目录时使用——即使用户只是说"帮我建个放论文材料的文件夹"也应使用。... | cabbage2000-lab/paper-tutor-skills |
| [**paper-logic**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-logic) | Paper 论证链检查命令（结构对应检查器）。当用户已有论文大纲、要查论证逻辑、查 RQ 与方法结果结论是否对应、查论证链是否闭环、查论文逻辑结构，或说"帮我查查论证有没有问题""我的逻辑完整吗""RQ 和结论对应吗""方法能不能回答我的问题""结论有没有超出结果"时使用——即使用户只说"帮我... | cabbage2000-lab/paper-tutor-skills |
| [**paper-method**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-method) | Paper 研究设计参谋命令（方法-RQ 匹配检查器 + 方法类引导器）。当用户已有研究问题（RQ）要定研究方法、检查方法能否回答 RQ、选什么方法类、查方法与 RQ 匹配度、研究设计行不行、涉人类被试要理伦理审查提示清单，或说"帮我设计研究方法""我想用 X 方法你看行不行""问卷能回答我的... | cabbage2000-lab/paper-tutor-skills |
| [**paper-outline**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-outline) | Paper 论文大纲命令（结构草案共写器）。当用户已有研究问题（RQ）和文献笔记、要搭论文骨架、起草章节大纲、写论文结构、整理写作框架，或说"帮我把论文大纲列一下""论文应该怎么组织""章节怎么分""我有 RQ 和文献、想搭个大纲"时使用——即使用户只说"我想列个大纲""帮我想想结构""论文分... | cabbage2000-lab/paper-tutor-skills |
| [**paper-plot**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-plot) | Paper 绘图代码生成命令（内建于 paper-figure，可独立调用）。当用户要生成绘图代码、plot 代码、画图代码、matplotlib 代码、ggplot2 代码、帮我生成图表代码、帮我写画图脚本、生成柱状图代码、散点图代码、折线图代码、箱线图代码、误差线图代码、直方图代码、热图代... | cabbage2000-lab/paper-tutor-skills |
| [**paper-proposal**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-proposal) | Paper 开题报告组装命令（多源汇聚组装器）。当用户要写开题报告、组装学位论文开题材料、按中文学位论文制度节点整理立项文档，或说"帮我组装开题报告""开题报告怎么写""开题要准备什么""选题依据怎么写""文献综述部分帮我整理""研究内容部分怎么填""学位论文开题"时使用——即使用户只说"我要... | cabbage2000-lab/paper-tutor-skills |
| [**paper-review**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-review) | Paper 模拟评审命令（多视角模拟审稿意见器）。当用户要投稿前预演评审、答辩前预演、模拟审稿、预审论文、查审稿人会怎么看、学位论文盲审模拟、期刊审稿模拟、答辩委员追问预演，或说"帮我模拟评审""模拟审稿看看""预审下我的论文""审稿人会提什么意见""盲审会挂吗""答辩委员可能问什么"时使用—... | cabbage2000-lab/paper-tutor-skills |
| [**paper-revise**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-revise) | Paper 修订辅助命令（修订建议对照表 + 逐点回复信起草器）。当用户投稿/答辩后收到审稿意见要写回复信、要逐点回复审稿人、要改稿、要准备 point-by-point response、要 response letter、要修订建议、要把审稿意见逐条回应、或说"帮我写回复信""审稿意见怎么... | cabbage2000-lab/paper-tutor-skills |
| [**paper-screen**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-screen) | Paper 系统综述筛选命令（PRISMA 2020 筛选台账 + 流程图生成器）。当用户要做系统性文献综述、做 PRISMA 筛选、定纳入排除标准、两轮筛选文献、文献去重、要 PRISMA 流程图、要数据提取表、要偏倚风险评估清单、要 PRISMA 报告规范自查，或说"帮我做系统综述""这批... | cabbage2000-lab/paper-tutor-skills |
| [**paper-search**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-search) | 文献检索与综述辅助命令。当用户已有研究问题（RQ）或明确方向，要查文献、做文献综述、找研究缺口（Research Gap）、了解"某方向别人做到哪一步"时使用——即使用户只说"帮我查查这方面的研究""这个领域有哪些论文""有没有人研究过 X""这方面国内外做到什么程度了""帮我搜搜文献""顺着... | cabbage2000-lab/paper-tutor-skills |
| [**paper-style**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-style) | Paper 风格校准命令（全文风格一致性校准 + 个人风格基线 + AIGC 误判申诉特征陈列）。当用户要查全文文风是否一致、要校准各章语体、要建立自己的写作风格基线供后续起草复用、或论文被 AIGC 检测判为 AI 生成要向学校/期刊申诉时使用——即使用户只说"这几章读着不像一个人写的""帮... | cabbage2000-lab/paper-tutor-skills |
| [**paper-submit**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-submit) | Paper 投稿准备命令（投稿材料清单整理器 + 期刊常见投稿要求陈列）。当用户论文写完要投稿、要准备投稿材料、要写 cover letter、要整理投稿 checklist、要查期刊投稿要求、要准备投稿文件包、或说"帮我准备投稿""投稿要交什么""这个期刊要什么材料""投稿清单怎么列""co... | cabbage2000-lab/paper-tutor-skills |
| [**paper-topic**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-topic) | Paper 选题澄清命令（选题导航器）。当用户只有模糊研究方向、说不清要研究什么、想把兴趣聚焦成研究问题（RQ），或已有一个候选题想被检验，或说选题、开题方向、不知道研究什么、帮我想想研究什么、你看这个题行不行、给我几个这个方向常见的研究问题、paper-topic 时使用——即使只说"我想研... | cabbage2000-lab/paper-tutor-skills |
| [**paper-typeset**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-typeset) | Paper 出版链命令（Markdown → LaTeX / DOCX / PDF 转换管线 + GB/T 7714-2015 国标著录）。... | cabbage2000-lab/paper-tutor-skills |
| [**paper-verify**](https://github.com/cabbage2000-lab/paper-tutor-skills/tree/main/skills/paper-verify) | 引用存在性核验命令。当用户要核查参考文献是否真实存在、查引用有没有编造、核实 DOI、 查某条引用是否已撤稿、查元数据（作者/年份/标题）对不对得上、检查参考文献格式 （GB/T 7714）、查论文结论是否夸大超出结果支撑，或说 verify / 核验 / 核对引用 / 查 DOI / 参考文... | cabbage2000-lab/paper-tutor-skills |

### 知识管理 / Obsidian

| Skill | 描述 | 来源 |
|---|---|---|
| [**defuddle**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/defuddle) | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens.... | mdwoicke/obsidian-skills |
| [**ima-skill**](https://github.com/daymade/claude-code-skills/tree/main/ima-copilot) | Installs, troubleshoots, and personalizes the official Tencent IMA skill (a wrapper layer that orchestrates upstream ima-skill,... | daymade/claude-code-skills |
| [**json-canvas**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/json-canvas) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files,... | mdwoicke/obsidian-skills |
| [**kb-ops**](./skills/kb-ops) | 本地知识库运维。当用户要新建知识库、采集资料入库（论文/Zotero/网页/笔记/RSS）、把 raw 记录编译成 wiki 页、校验库契约、看库状态、或排查知识库脚本报错时，使用此 skill。... | 自定义 |
| [**obsidian-bases**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/obsidian-bases) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files,... | mdwoicke/obsidian-skills |
| [**obsidian-cli**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/obsidian-cli) | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more.... | mdwoicke/obsidian-skills |
| [**obsidian-markdown**](https://github.com/mdwoicke/obsidian-skills/tree/main/skills/obsidian-markdown) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax.... | mdwoicke/obsidian-skills |

### 个人技能集（ljg-*）

| Skill | 描述 | 来源 |
|---|---|---|
| [**ljg-blind**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-blind) | 盲区扫描——读昨天你与 AI 的全部对话，照出暴露的思维盲区（不是不懂的知识，是让某类真相一直看不见的思维习惯），再从微信读书挑一本书的一章精准补上，落成一篇完整分析笔记。Use when user says '扫盲区', '盲区', '照盲区', '看看我的思维盲区',... | lijigang/ljg-skills |
| [**ljg-book**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-book) | Explain a whole book to readers without specialist knowledge: what it follows, how its main threads connect, where it ends,... | lijigang/ljg-skills |
| [**ljg-card**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-card) | Content caster (铸). Transforms text into PNG through precise HTML typography and, when the mold needs it, generated raster imagery.... | lijigang/ljg-skills |
| [**ljg-classic**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-classic) | 古文逐字注解、组合排版、章节意旨图与全章解读生成器。把原文、字词注、句义注、无字顶部配图和章节解读排成一张可读的长 PNG。USE WHEN 用户调用 ljg-classic OR 要求给文言文、古诗文、经史子集做逐字注解、彩色夹注、章节解读、古文讲义图、章节配图。... | lijigang/ljg-skills |
| [**ljg-constraint**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-constraint) | 给一个领域、专业、角色、产品或争论找出真正框住它的几条约束，判明它们属于世界/规则/解释（硬/软/自设），看这组约束如何定义身份、补全问题、框出解空间并解释实际行为；尤其用于区分目标相同但约束不同导致的方案分歧，识别被误当硬事实的旧解释。USE WHEN 用户说 '约束', '找约束',... | lijigang/ljg-skills |
| [**ljg-explain**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-explain) | 把概念、公式、机制与原理讲到能辨认、能推导、能迁移：用通俗中文接通具体情境、判别依据、运作过程和成立条件。USE WHEN 用户调用 ljg-explain、说「通俗易懂地讲解」「讲透这个概念或公式」「费曼讲解」「ELI5」，或希望从零理解一个知识点并能用于新情境。... | lijigang/ljg-skills |
| [**ljg-invest**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-invest) | 投资分析。给一个项目（公司名、BP、创始人对话记录），写一份深度投资分析报告。不走传统投资分析的路——核心判断只有一个：这个项目是不是一台「秩序创造机器」。Use when user says '投资报告', '投资分析', '分析这个项目', '写投资报告',... | lijigang/ljg-skills |
| [**ljg-is**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-is) | 把一个名词或概念写成可使用的理解：先用普通话讲清它是什么、与相邻概念差在哪里，再说明它怎样运作、会改写什么判断，最后给出面对它时的行动抓手。USE WHEN 用户问 X 是什么、怎么理解、意味着什么、为什么重要、以后怎样判断或使用；尤其适合技术概念、制度、产品、角色、方法、规范与实践。... | lijigang/ljg-skills |
| [**ljg-learn**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-learn) | Deep concept anatomist that deconstructs any concept through 8 exploration dimensions (history, dialectics, phenomenology, linguistics,... | lijigang/ljg-skills |
| [**ljg-paper**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-paper) | Explain research papers to readers without a specialist background: what the paper studies, what the authors contribute, how the findings follow,... | lijigang/ljg-skills |
| [**ljg-present**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-present) | Unix 气质的演讲设计与保真排版。把 Org/Markdown 提纲或经授权提炼的讲稿制成单文件离线 HTML；以语义角色选择巨句、对照、Unicode 关系图、证据与章节版式。默认深色，支持讲稿层、原生图表与翻页笔。... | lijigang/ljg-skills |
| [**ljg-push**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-push) | 把 ~/.agents/skills/ljg-* 里所有更新过的 skills 同步到 github repo (ljg-skills)，先推 master 分支（org-mode 输出风格），再切 md 分支（markdown 输出风格）做基础 markdown 化后推。... | lijigang/ljg-skills |
| [**ljg-qa**](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-qa) | 信息提问机。给一篇文章/论文/书，把核心观点抽成 Q-A 对——Question 切要害，不教科书；Answer 简洁清晰，有形式化收口，逻辑链完整。读者顺 Q 链走过，每个 A 砸下一枚钉子，复现作者整套推理。Use when user says '问答', 'Q&A', 'QA',... | lijigang/ljg-skills |
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
| [**travel-planner**](https://github.com/ailabs-393/ai-labs-claude-skills/tree/main/packages/skills/travel-planner) | This skill should be used whenever users need help planning trips, creating travel itineraries, managing travel budgets,... | ailabs-393/ai-labs-claude-skills |
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

### 自定义 Skills（无公开源）

| Skill | 描述 | 来源 |
|---|---|---|
| [**modern-r**](./skills/modern-r) | Modernize and review existing R code using current idioms and migration priorities across tidyverse, tidy evaluation, style, and performance.... | 自定义 |
| [**r-skill-changelog-sync**](./skills/r-skill-changelog-sync) | Sync installed Codex R skills with current upstream package changes by checking official changelog sources such as CRAN package pages,... | 自定义 |

## Skill 来源与更新

每个 skill 都对应一个上游 GitHub 仓库（完整映射见 [SOURCES.md](./SOURCES.md) / [SOURCES.tsv](./SOURCES.tsv)）。上游发布新版本后：

```bash
bash update-skills.sh              # 同步全部 skills/ 与 plugin-skills/
bash update-skills.sh taste-skill  # 只同步某一个 skill
git add -A && git commit -m "Update skills" && git push
```

## 多环境同步策略

1. **Skills**：通过 Git 管理，`.cc-switch` 在新机器上做符号链接激活
2. **Plugins**：`setup.ps1` / `setup.sh` 自动安装
3. **Settings**：`settings.template.json` 作为模板，本地密钥保存在 `settings.local.json`（不提交）
4. **Hooks**：通过 plugin 管理，配置文件备份在 `config/hooks/`

## Contributing

- 添加新 skill：放入 `skills/<name>/`，并在 `SOURCES.tsv` 中登记上游仓库后提交
- 同步上游更新：运行 `bash update-skills.sh` 后提交
- 自定义 skill（无公开源）：保留在仓库中，并在 `SOURCES.tsv` 中标注 `CUSTOM`
