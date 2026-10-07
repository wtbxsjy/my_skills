import os
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tsv_path = os.path.join(ROOT, 'SOURCES.tsv')

rows = []
with open(tsv_path, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        p = line.split('|')
        if len(p) < 4:
            continue
        dest, repo, branch, srcpath = p[0], p[1], p[2], p[3] or '.'
        note = p[4] if len(p) > 4 else ''
        rows.append((dest, repo, branch, srcpath, note))

groups = OrderedDict()
for r in rows:
    groups.setdefault(r[1], []).append(r)

def repo_link(url):
    return url.replace('.git', '')

lines = []
lines.append('# Skill 来源与更新')
lines.append('')
lines.append('本仓库中的每个 skill 都对应一个上游 GitHub 仓库。升级上游后，运行 `bash update-skills.sh` 即可把所有 skill 同步到最新版本。')
lines.append('')
lines.append('- 映射数据文件：[SOURCES.tsv](./SOURCES.tsv)（供 `update-skills.sh` 读取）')
lines.append('- 一键更新脚本：[update-skills.sh](./update-skills.sh)')
lines.append('- 用法：`bash update-skills.sh` 全量同步；`bash update-skills.sh <skill名>` 只同步某个 skill')
lines.append('')
lines.append('## 源仓库汇总')
lines.append('')
for repo, items in groups.items():
    lines.append('### ' + repo_link(repo))
    lines.append('')
    lines.append('| 本仓库目录 | 上游分支 | 上游路径 | 备注 |')
    lines.append('|---|---|---|---|')
    for dest, _r, branch, srcpath, note in items:
        note = note or ''
        lines.append('| `' + dest + '` | `' + branch + '` | `' + srcpath + '` | ' + note + ' |')
    lines.append('')

lines.append('## 自定义 Skill（无公开源，不参与自动更新）')
lines.append('')
lines.append('| Skill | 说明 |')
lines.append('|---|---|')
lines.append('| `skills/modern-r` | 自定义：R 代码现代化改造指南 |')
lines.append('| `skills/r-skill-changelog-sync` | 自定义：R 包 changelog 同步检查 |')
lines.append('| `skills/kb-ops` | 自定义：本地知识库运维（kb-template 脚手架） |')
lines.append('| `skills/gt-xlsx-roundtrip` | 自定义：forgts + gtxlsx 在 Excel 与 gt 表格间往返转换 |')
lines.append('')

with open(os.path.join(ROOT, 'SOURCES.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('SOURCES.md generated,', len(rows), 'entries')