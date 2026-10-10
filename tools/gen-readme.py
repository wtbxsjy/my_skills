import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

src_map = {}
with open(os.path.join(ROOT, 'SOURCES.tsv'), encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        p = line.split('|')
        if len(p) < 4:
            continue
        dest, repo, branch, srcpath = p[0], p[1], p[2], p[3] or '.'
        src_map[dest] = (repo, branch, srcpath)

def repo_html(repo_url):
    return repo_url.replace('.git', '')

def skill_link(dest):
    if dest in src_map:
        repo, branch, srcpath = src_map[dest]
        if repo == 'CUSTOM' or srcpath == 'CUSTOM':
            return './' + dest
        base = repo_html(repo)
        if srcpath == '.':
            return base
        return base + '/tree/' + branch + '/' + srcpath
    return './' + dest

def source_name(dest):
    if dest in src_map:
        repo = src_map[dest][0]
        if repo == 'CUSTOM':
            return '自定义'
        return repo_html(repo).replace('https://github.com/', '')
    return '自定义'

def get_description(skill_dir):
    sp = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.isfile(sp):
        return ''
    txt = open(sp, encoding='utf-8', errors='ignore').read()
    m = re.search(r'^description:\s*(.+)$', txt, re.M)
    if not m:
        return ''
    first = m.group(1).strip()
    if first in ('>', '|', '>-', '>+'):
        lines = []
        start = txt[:m.end()].count(chr(10)) + 1
        for line in txt.splitlines()[start:]:
            if line.startswith('  ') or line.startswith(chr(9)):
                lines.append(line.strip())
            else:
                break
        desc = ' '.join(lines).strip()
    else:
        desc = first.strip().strip('"').strip(chr(39))
    desc = re.sub(r'\s+', ' ', desc).strip()
    if len(desc) > 150:
        cut = desc[:147]
        last = max(cut.rfind('. '), cut.rfind('。'), cut.rfind(','))
        if last > 60:
            cut = cut[:last + 1]
        desc = cut.rstrip() + '...'
    return desc

def collect_skills(base, prefix):
    out = {}
    for name in sorted(os.listdir(base)):
        d = os.path.join(base, name)
        if not os.path.isdir(d):
            continue
        out[prefix + '/' + name] = get_description(d)
    return out

skills = collect_skills(os.path.join(ROOT, 'skills'), 'skills')
plugins = {}
for p1 in sorted(os.listdir(os.path.join(ROOT, 'plugin-skills'))):
    d1 = os.path.join(ROOT, 'plugin-skills', p1)
    if not os.path.isdir(d1):
        continue
    for p2 in sorted(os.listdir(d1)):
        d2 = os.path.join(d1, p2)
        if os.path.isdir(d2) and os.path.isfile(os.path.join(d2, 'SKILL.md')):
            plugins['plugin-skills/' + p1 + '/' + p2] = get_description(d2)

all_skills = dict(skills)
all_skills.update(plugins)

def anchor(t):
    t = t.lower()
    t = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', t, flags=re.UNICODE)
    t = re.sub(r'\s+', '-', t)
    return t

R = ['cli','cran-extrachecks','lifecycle','mirai','r-cli-app','r-package-development','testing-r-packages',
     'r-bayes','r-oop','r-performance','r-style-guide','rlang-patterns','tdd-workflow','tidyverse-patterns',
     'add-dials-parameter','add-parsnip-engine','add-parsnip-model','add-recipe-step','add-yardstick-metric',
     'shiny-bslib','shiny-bslib-theming','create-release-checklist','release-post','gt-xlsx-roundtrip']
QUARTO = ['quarto-authoring','quarto-alt-text','quarto-talks','alt-text','brand-yml']
DATA = ['tabular-data-ml','single-cell-rna-qc','scvi-tools','ggsql','attach-db','duckdb-docs','install-duckdb','query','read-file','read-memories']
BIO = ['alphafold-database-fetch-and-analyze','alphagenome-single-variant-analysis','chembl-database','clinical-trials-database','clinvar-database','credentials','dbsnp-database','embl-ebi-ols','encode-ccres-database','ensembl-database','foldseek-structural-search','gnomad-database','gtex-database','human-protein-atlas-database','interpro-database','jaspar-database','literature-search-arxiv','literature-search-biorxiv','literature-search-europepmc','literature-search-openalex','ncbi-sequence-fetch','openfda-database','opentargets-database','pdb-database','predictingthepast','protein-sequence-msa','protein-sequence-similarity-search','pubchem-database','pubmed-database','pymol','quickgo-database','reactome-database','string-database','ucsc-conservation-and-tfbs','unibind-database','uniprot-database','uv','workflow-skill-creator']
DEV = ['cpp-pro','rust-skills','karpathy-guidelines','playwright-cli','critical-code-reviewer','describe-design','implement','working-on','pr-create','pr-threads-address','pr-threads-resolve','session-report','claude-automation-recommender','claude-md-improver','scientific-problem-selection','start','nextflow-development','instrument-data-to-allotrope']
FRONTEND = ['frontend-design','frontend-dev','fullstack-dev','taste-skill','taste-skill-v1','gpt-tasteskill','brandkit','brutalist-skill','minimalist-skill','output-skill','soft-skill','redesign-skill','stitch-skill','imagegen-frontend-mobile','imagegen-frontend-web','image-to-code-skill','frontend-slides','guizang-ppt-skill']
CHART = ['ggplot2-pub','diagram-design','fireworks-tech-graph','architecture-diagram-generator','excalidraw-diagram-generator','lieflat-charts']
OFFICE = ['pptx-generator','ppt-master','minimax-docx','minimax-pdf','minimax-xlsx','gif-sticker-maker']
KNOWLEDGE = ['defuddle','json-canvas','obsidian-bases','obsidian-cli','obsidian-markdown','ima-skill','kb-ops']
META = ['skill-creator','writing-rules','credentials','uv','find-skills','score','travel-planner']
LJG = ['ljg-blind','ljg-book','ljg-card','ljg-classic','ljg-constraint','ljg-invest','ljg-is','ljg-learn','ljg-paper','ljg-explain','ljg-present','ljg-push','ljg-qa','ljg-rank','ljg-read','ljg-relationship','ljg-roundtable','ljg-structure','ljg-think','ljg-word','ljg-writes']

CATS = [
    ('R / Tidyverse / Bioconductor', R),
    ('Quarto / 发布与写作', QUARTO),
    ('数据科学 / 机器学习 / 数据查询', DATA),
    ('生物医药 / 文献数据库', BIO),
    ('开发 / 工程 / 工作流', DEV),
    ('前端 / 设计', FRONTEND),
    ('图表 / 可视化', CHART),
    ('文档 / 办公', OFFICE),
    ('知识管理 / Obsidian', KNOWLEDGE),
    ('个人技能集（ljg-*）', LJG),
    ('Meta / 效率工具', META),
]
CUSTOM_NAMES = ['modern-r', 'r-skill-changelog-sync']
PLUGIN_TITLE = '插件附带 Skills'
CUSTOM_TITLE = '自定义 Skills（无公开源）'

def cat_of(dest):
    if dest.startswith('plugin-skills/'):
        return PLUGIN_TITLE
    name = dest.split('/')[-1]
    for title, names in CATS:
        if name in names:
            return title
    if name in CUSTOM_NAMES:
        return CUSTOM_TITLE
    return PLUGIN_TITLE

groups = {}
for dest in all_skills:
    t = cat_of(dest)
    groups.setdefault(t, []).append(dest)
for t in groups:
    groups[t].sort()

ordered = [t for t, _ in CATS]
if PLUGIN_TITLE in groups:
    ordered.append(PLUGIN_TITLE)
if CUSTOM_TITLE in groups:
    ordered.append(CUSTOM_TITLE)

L = []
L.append('<h1 align="center">My Claude Code Skills</h1>')
L.append('')
L.append('<p align="center">')
L.append('  Claude Code 环境 Skills / Plugins / Settings / Hooks 统一管理仓库 · 全部 skill 可一键从上游同步更新')
L.append('</p>')
L.append('')
L.append('<p align="center">')
L.append('  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>')
L.append('  <a href="https://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>')
L.append('  <img src="https://img.shields.io/github/stars/wtbxsjy/my_skills?style=flat-square&label=Stars" alt="Stars">')
L.append('  <img src="https://img.shields.io/github/license/wtbxsjy/my_skills?style=flat-square" alt="License">')
L.append('</p>')
L.append('')
L.append('---')
L.append('')
L.append('## Contents')
L.append('')
L.append('- [快速开始](#快速开始)')
L.append('- [Skill Library](#skill-library)')
for t in ordered:
    if t in groups:
        L.append('  - [' + t + '](#' + anchor(t) + ')')
L.append('- [Skill 来源与更新](#skill-来源与更新)')
L.append('- [多环境同步策略](#多环境同步策略)')
L.append('- [Contributing](#contributing)')
L.append('')
L.append('---')
L.append('')
L.append('## 快速开始')
L.append('')
L.append('在新机器上同步环境：')
L.append('')
L.append('```bash')
L.append('git clone https://github.com/wtbxsjy/my_skills.git')
L.append('cd my_skills')
L.append('bash setup.sh        # Linux / macOS（Windows 用 setup.ps1）')
L.append('```')
L.append('')
L.append('## Skill Library')
L.append('')
for t in ordered:
    if t not in groups:
        continue
    L.append('### ' + t)
    L.append('')
    L.append('| Skill | 描述 | 来源 |')
    L.append('|---|---|---|')
    for dest in groups[t]:
        name = dest.split('/')[-1]
        desc = all_skills.get(dest, '')
        link = skill_link(dest)
        src = source_name(dest)
        L.append('| [**' + name + '**](' + link + ') | ' + desc + ' | ' + src + ' |')
    L.append('')
L.append('## Skill 来源与更新')
L.append('')
L.append('每个 skill 都对应一个上游 GitHub 仓库（完整映射见 [SOURCES.md](./SOURCES.md) / [SOURCES.tsv](./SOURCES.tsv)）。上游发布新版本后：')
L.append('')
L.append('```bash')
L.append('bash update-skills.sh              # 同步全部 skills/ 与 plugin-skills/')
L.append('bash update-skills.sh taste-skill  # 只同步某一个 skill')
L.append('git add -A && git commit -m "Update skills" && git push')
L.append('```')
L.append('')
L.append('## 多环境同步策略')
L.append('')
L.append('1. **Skills**：通过 Git 管理，`.cc-switch` 在新机器上做符号链接激活')
L.append('2. **Plugins**：`setup.ps1` / `setup.sh` 自动安装')
L.append('3. **Settings**：`settings.template.json` 作为模板，本地密钥保存在 `settings.local.json`（不提交）')
L.append('4. **Hooks**：通过 plugin 管理，配置文件备份在 `config/hooks/`')
L.append('')
L.append('## Contributing')
L.append('')
L.append('- 添加新 skill：放入 `skills/<name>/`，并在 `SOURCES.tsv` 中登记上游仓库后提交')
L.append('- 同步上游更新：运行 `bash update-skills.sh` 后提交')
L.append('- 自定义 skill（无公开源）：保留在仓库中，并在 `SOURCES.tsv` 中标注 `CUSTOM`')
L.append('')

with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(L))
print('README.md written,', len(all_skills), 'skills,', len(groups), 'categories')