# My Claude Code Skills

Claude Code 环境配置、Skills、Plugins、Settings 和 Hooks 的统一管理仓库。

## 快速开始

在新机器上同步环境，运行：

**Windows (PowerShell):**
```powershell
git clone https://github.com/wtbxsjy/my_skills.git
cd my_skills
.\setup.ps1
```

**Linux / macOS / Git Bash:**
```bash
git clone https://github.com/wtbxsjy/my_skills.git
cd my_skills
bash setup.sh
```

安装后编辑 `~/.claude/settings.json` 填入你的 API keys。

## 仓库结构

```
my_skills/
├── setup.ps1              # Windows 一键安装脚本
├── setup.sh               # Linux/macOS 一键安装脚本
├── config/
│   ├── settings.template.json  # Claude Code 配置模板（不含密钥）
│   ├── cc-switch-settings.json # .cc-switch 配置
│   └── hooks/                  # 各插件的 hooks 配置
│       ├── hookify/
│       ├── security-guidance/
│       ├── ralph-loop/
│       ├── explanatory-output-style/
│       └── learning-output-style/
├── skills/                     # 用户 Skills（来自 .cc-switch 和 .claude）
├── plugin-skills/              # 插件提供的 Skills
├── SOURCES.md                  # 每个 skill 的源 GitHub 仓库索引
├── SOURCES.tsv                 # 源仓库映射表（update-skills.sh 读取）
└── update-skills.sh            # 一键从上游同步/更新全部 skills
```

## 已安装的 Plugins

| Plugin | 用途 |
|--------|------|
| `code-review` | 代码审查 |
| `skill-creator` | 创建/管理 Skills |
| `github` | GitHub 集成 |
| `playwright` | 浏览器自动化 |
| `commit-commands` | Git commit 快捷命令 |
| `claude-code-setup` | Claude Code 自动化配置 |
| `clangd-lsp` | C/C++ LSP 支持 |

## Skill 分类

### R / Tidyverse / Bioconductor
`add-dials-parameter`, `add-parsnip-engine`, `add-parsnip-model`, `add-recipe-step`, `add-yardstick-metric`, `tidyverse-patterns`, `modern-r`, `r-style-guide`, `rlang-patterns`, `r-bayes`, `r-cli-app`, `r-oop`, `r-package-development`, `r-performance`, `testing-r-packages`, `r-skill-changelog-sync`, `shiny-bslib`, `shiny-bslib-theming`, `cran-extrachecks`, `lifecycle`, `mirai`, `cli`, `attach-db`, `brand-yml`

### Quarto / Publishing
`quarto-authoring`, `quarto-alt-text`, `alt-text`

### 数据科学 / 机器学习
`tabular-data-ml`, `single-cell-rna-qc`, `scvi-tools`, `duckdb-docs`, `ggsql`, `install-duckdb`

### 工作流 / DevOps
`nextflow-development`, `scientific-problem-selection`, `instrument-data-to-allotrope`

### 开发
`frontend-dev`, `fullstack-dev`, `cpp-pro`, `tdd-workflow`, `pr-create`, `pr-threads-address`, `pr-threads-resolve`, `create-release-checklist`, `critical-code-reviewer`, `describe-design`, `karpathy-guidelines`

### 图表 / 可视化
`fireworks-tech-graph`, `architecture-diagram-generator`, `excalidraw-diagram-generator`

### 文档 / 办公
`pptx-generator`, `minimax-docx`, `minimax-pdf`, `minimax-xlsx`

### 效率工具
`start`, `implement`, `working-on`, `release-post`, `query`, `read-file`, `read-memories`, `gif-sticker-maker`

## 多环境同步策略

1. **Skills**: 通过 Git 管理，`.cc-switch` 在新机器上做符号链接激活
2. **Plugins**: `setup.ps1`/`setup.sh` 自动安装
3. **Settings**: 使用 `settings.template.json` 作为模板，本地密钥保存在 `settings.local.json`（不提交）
4. **Hooks**: 通过 plugin 管理，配置文件备份在 `config/hooks/`

## Skill 来源与自动更新

每个 skill 都对应一个上游 GitHub 仓库（映射见 [SOURCES.md](./SOURCES.md) / [SOURCES.tsv](./SOURCES.tsv)）。上游发布新版本后，运行：

```bash
bash update-skills.sh            # 同步全部 skills/ 与 plugin-skills/
bash update-skills.sh taste-skill # 只同步某一个 skill
```

脚本会按 `SOURCES.tsv` 从各源仓库（posit-dev/skills、tidymodels/skills、google-deepmind/science-skills、anthropics/skills、duckdb/duckdb-skills、minimax-ai/skills、nexu-io/open-design 等）拉取最新内容并镜像到本仓库。

> 注意：`skills/modern-r` 与 `skills/r-skill-changelog-sync` 为自定义 skill，无公开源，不会参与自动更新。

## 更新流程

```bash
# 更新完 skill 后提交
bash update-skills.sh
git add skills/ plugin-skills/ SOURCES.md SOURCES.tsv update-skills.sh
git commit -m "Update skills from upstream sources"
git push

# 另一台机器拉取
git pull
ln -s ~/.cc-switch/skills/new-skill ~/.claude/skills/new-skill
```
