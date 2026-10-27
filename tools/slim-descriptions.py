#!/usr/bin/env python3
"""slim-descriptions.py - keep trimmed SKILL.md descriptions across upstream syncs.

Why: a skill's `description` is injected into every session's skill catalog, so this repository
shortens long upstream descriptions by hand. `update-skills.sh` mirrors the upstream files and
therefore brings the long descriptions back. This tool remembers the trimmed text and puts it back
after a sync. Standard library only.

Registry: descriptions.slim.json (next to SOURCES.tsv)
    {"version": 1, "skills": {"skills/<name>": {"slim": "<trimmed text>", "orig": "<sha of upstream text>"}}}
`orig` is a fingerprint of the *upstream* description at the time of trimming. If upstream rewrites
its description later, `apply` still writes the trimmed text but warns that it may be stale.

Commands
    capture [dest ...]   record descriptions that differ from upstream (compares the working tree
                         with the upstream cache used by update-skills.sh; fetches it if missing)
    apply   [dest ...]   write the registered trimmed descriptions into SKILL.md (all entries when
                         no dest is given); update-skills.sh calls this after every sync
    status               list registry entries that are out of sync and long, unregistered descriptions
    selftest             run the built-in tests

A `dest` is a directory such as skills/idea-evaluator; a substring also works (like update-skills.sh).
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, 'descriptions.slim.json')
SOURCES = os.path.join(ROOT, 'SOURCES.tsv')
CACHE_DIR = os.environ.get('MY_SKILLS_CACHE') or os.path.join(
    os.environ.get('XDG_CACHE_HOME') or os.path.join(os.path.expanduser('~'), '.cache'), 'my_skills-update')
# Trimmed descriptions in this repository are 75-271 characters; the catalog renders at most 500.
SLIM_LIMIT = 271
LONG_LIMIT = 300
# capture only records a real trim: the local text must be much shorter than upstream's. Anything else
# (local text stale after an upstream rewrite, a small wording edit) must not be frozen, or the next
# sync would silently undo upstream's change. Real trims in this repository shrink to 35-60% of the
# original; the cases to exclude were 85-104%.
TRIM_MIN_UPSTREAM = 150
TRIM_MAX_RATIO = 0.75

FM_RE = re.compile(r'\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)', re.S)
KEY_RE = re.compile(r'^[A-Za-z_][\w-]*:(?:[ \t]|$)')


# --------------------------------------------------------------------------- frontmatter handling
def norm(text):
    return re.sub(r'\s+', ' ', text).strip()


def sha(text):
    return hashlib.sha256(norm(text).encode('utf-8')).hexdigest()[:16]


def find_description(fm):
    """Return (start, end, first_line_value, continuation_lines) of the top-level description field."""
    lines = fm.splitlines(keepends=True)
    pos = 0
    start = None
    for i, line in enumerate(lines):
        if start is None:
            if re.match(r'^description:(?:[ \t]|$)', line):
                start = (i, pos)
        pos += len(line)
    if start is None:
        return None
    i0, p0 = start
    j = i0 + 1
    while j < len(lines):
        l = lines[j]
        if l.strip() and not l[0].isspace():  # a non-blank line at column 0 starts the next key
            break
        j += 1
    # drop trailing blank lines from the field so they survive replacement
    k = j
    while k > i0 + 1 and not lines[k - 1].strip():
        k -= 1
    first = re.sub(r'^description:[ \t]*', '', lines[i0]).rstrip('\r\n')
    cont = [l.rstrip('\r\n') for l in lines[i0 + 1:k]]
    end = p0 + sum(len(l) for l in lines[i0:k])
    return p0, end, first, cont


def decode_value(first, cont):
    first = first.strip()
    if re.match(r'^[>|][-+0-9]*\s*(#.*)?$', first):  # block scalar
        return norm(' '.join(l.strip() for l in cont))
    if first.startswith('"'):
        raw = norm(' '.join([first] + [l.strip() for l in cont]))
        end = None
        i = 1
        while i < len(raw):
            if raw[i] == '\\':
                i += 2
                continue
            if raw[i] == '"':
                end = i
                break
            i += 1
        body = raw[:end + 1] if end is not None else raw
        try:
            return norm(json.loads(body))
        except ValueError:
            return norm(body.strip('"'))
    if first.startswith("'"):
        raw = norm(' '.join([first] + [l.strip() for l in cont]))
        m = re.match(r"^'((?:[^']|'')*)'", raw)
        return norm((m.group(1) if m else raw.strip("'")).replace("''", "'"))
    return norm(' '.join([first] + [l.strip() for l in cont]))


def read_description(path):
    """Return the normalized description of a SKILL.md, or None."""
    try:
        text = open(path, encoding='utf-8').read()
    except OSError:
        return None
    m = FM_RE.match(text)
    if not m:
        return None
    f = find_description(m.group(1))
    if not f:
        return None
    return decode_value(f[2], f[3])


def quote(text):
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'


def write_description(path, slim):
    text = open(path, encoding='utf-8', newline='').read()  # newline='' keeps CRLF files intact
    m = FM_RE.match(text)
    f = find_description(m.group(1))
    p0, end, _, _ = f
    fm = m.group(1)
    nl = '\r\n' if '\r\n' in fm else '\n'
    tail_nl = nl if fm[p0:end].endswith(('\n', '\r')) else ''
    new_fm = fm[:p0] + 'description: ' + quote(slim) + tail_nl + fm[end:]
    new_text = text[:m.start(1)] + new_fm + text[m.end(1):]
    open(path, 'w', encoding='utf-8', newline='').write(new_text)


# --------------------------------------------------------------------------- registry and sources
def load_registry():
    if not os.path.isfile(REGISTRY):
        return {'version': 1, 'skills': {}}
    with open(REGISTRY, encoding='utf-8') as f:
        return json.load(f)


def save_registry(reg):
    with open(REGISTRY, 'w', encoding='utf-8') as f:
        json.dump(reg, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')


def load_sources():
    rows = []
    if not os.path.isfile(SOURCES):
        return rows
    for line in open(SOURCES, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        p = line.split('|')
        if len(p) < 4:
            continue
        dest, repo, branch, srcpath = p[0], p[1], p[2], p[3] or '.'
        rows.append((dest, repo, branch, srcpath))
    return rows


def select(names, universe, exact=False):
    if not names:
        return list(universe)
    out = []
    for n in names:
        n = n.rstrip('/')
        hit = [u for u in universe if u == n] or ([] if exact else [u for u in universe if n in u])
        for h in hit:
            if h not in out:
                out.append(h)
    return out


def ensure_cache(repo, branch, rows):
    """Same cache layout as update-skills.sh; never touches the working tree of this repository."""
    slug = re.sub(r'\.git$', '', repo.replace('https://github.com/', '')).replace('/', '__')
    d = os.path.join(CACHE_DIR, slug)
    os.makedirs(CACHE_DIR, exist_ok=True)

    def git(*a):
        return subprocess.run(['git', '-C', d] + list(a), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if os.path.isdir(os.path.join(d, '.git')):
        if git('fetch', '--depth', '1', 'origin', branch).returncode == 0:
            git('checkout', '-q', '-f', 'FETCH_HEAD')
    else:
        r = subprocess.run(['git', 'clone', '--depth', '1', '--filter=blob:none', '--sparse', '-b', branch, repo, d],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if r.returncode != 0:
            return None
    paths = [r[3] for r in rows]
    if '.' in paths:
        git('sparse-checkout', 'disable')
    else:
        git('sparse-checkout', 'set', *sorted(set(paths)))
    return d


# --------------------------------------------------------------------------- commands
def cmd_capture(args):
    rows = [r for r in load_sources() if r[1] != 'CUSTOM' and r[3] != 'CUSTOM']
    wanted = set(select(args.dest, [r[0] for r in rows]))
    rows = [r for r in rows if r[0] in wanted]
    reg = load_registry()
    groups = {}
    for r in rows:
        groups.setdefault((r[1], r[2]), []).append(r)
    recorded = unchanged = skipped = removed = 0
    for (repo, branch), grp in groups.items():
        cache = None
        if args.no_fetch:
            slug = re.sub(r'\.git$', '', repo.replace('https://github.com/', '')).replace('/', '__')
            cache = os.path.join(CACHE_DIR, slug)
            if not os.path.isdir(cache):
                cache = None
        else:
            cache = ensure_cache(repo, branch, grp)
        for dest, _, _, srcpath in grp:
            wt = read_description(os.path.join(ROOT, dest, 'SKILL.md'))
            up = read_description(os.path.join(cache, srcpath, 'SKILL.md')) if cache else None
            if wt is None or up is None:
                skipped += 1
                print('  [skip]    %s (%s)' % (dest, 'no local SKILL.md' if wt is None else 'upstream not available'))
                continue
            if wt == up:
                if dest in reg['skills']:
                    del reg['skills'][dest]
                    removed += 1
                    print('  [removed] %s (now identical to upstream)' % dest)
                else:
                    unchanged += 1
                continue
            if len(up) < TRIM_MIN_UPSTREAM or len(wt) > TRIM_MAX_RATIO * len(up):
                # not a trim: the local text is stale (upstream rewrote it) or was edited for another reason
                if dest in reg['skills']:
                    del reg['skills'][dest]
                    removed += 1
                skipped += 1
                print('  [skip]    %s (differs from upstream but is not a trim: %d vs %d chars; '
                      'edit by hand or fix the cause)' % (dest, len(wt), len(up)))
                continue
            old = reg['skills'].get(dest)
            if old and old['slim'] == wt and old['orig'] == sha(up):
                unchanged += 1
                continue
            reg['skills'][dest] = {'slim': wt, 'orig': sha(up)}
            recorded += 1
            print('  [record]  %s (%d -> %d chars)' % (dest, len(up), len(wt)))
    if not args.dry_run:
        save_registry(reg)
    print('capture: %d recorded, %d unchanged, %d removed, %d skipped%s' %
          (recorded, unchanged, removed, skipped, ' (dry run, registry not written)' if args.dry_run else ''))
    return 0


def cmd_apply(args):
    reg = load_registry()
    entries = reg['skills']
    explicit = bool(args.dest)
    targets = select(args.dest, list(entries), exact=args.exact) if explicit else list(entries)
    done = ok = warned = 0
    for dest in sorted(targets):
        path = os.path.join(ROOT, dest, 'SKILL.md')
        cur = read_description(path)
        if cur is None:
            if not args.quiet:
                print('  [skip]    %s (no SKILL.md or description)' % dest)
            continue
        e = entries[dest]
        if cur == e['slim']:
            ok += 1
            continue
        if sha(cur) != e['orig']:
            if len(cur) <= SLIM_LIMIT:
                print('  [skip]    %s: description differs from the registry but is already short; '
                      'if you edited it on purpose run: slim-descriptions.py capture %s' % (dest, dest))
                warned += 1
                continue
            if args.strict:
                print('  [skip]    %s: upstream description changed since it was trimmed (--strict)' % dest)
                warned += 1
                continue
            print('  [WARN]    %s: upstream description changed since it was trimmed; '
                  'applied the old trimmed text, please review (new upstream: %d chars)' % (dest, len(cur)))
            warned += 1
        write_description(path, e['slim'])
        done += 1
        if not args.quiet:
            print('  [slim]    %s (%d -> %d chars)' % (dest, len(cur), len(e['slim'])))
    # hint about synced skills that are long but have no trimmed version registered
    hinted = 0
    for dest in (args.dest if explicit else []):
        d = dest.rstrip('/')
        if d in entries:
            continue
        cur = read_description(os.path.join(ROOT, d, 'SKILL.md'))
        if cur and len(cur) > LONG_LIMIT:
            hinted += 1
            if hinted <= 10:
                print('  [hint]    %s has a long description (%d chars) and no trimmed version registered' % (d, len(cur)))
    if hinted > 10:
        print('  [hint]    ... and %d more long, untrimmed descriptions (see: slim-descriptions.py status --all)' % (hinted - 10))
    print('slim: %d rewritten, %d already trimmed, %d need attention' % (done, ok, warned))
    return 0


def iter_skills(include_plugins):
    bases = ['skills'] + (['plugin-skills'] if include_plugins else [])
    for b in bases:
        base = os.path.join(ROOT, b)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            d = os.path.join(base, name)
            if b == 'skills':
                if os.path.isfile(os.path.join(d, 'SKILL.md')):
                    yield '%s/%s' % (b, name)
            elif os.path.isdir(d):
                for sub in sorted(os.listdir(d)):
                    if os.path.isfile(os.path.join(d, sub, 'SKILL.md')):
                        yield '%s/%s/%s' % (b, name, sub)


def cmd_status(args):
    reg = load_registry()
    entries = reg['skills']
    bad = 0
    print('registry: %d trimmed descriptions' % len(entries))
    for dest in sorted(entries):
        cur = read_description(os.path.join(ROOT, dest, 'SKILL.md'))
        if cur is None:
            print('  [missing]     %s' % dest)
            bad += 1
        elif cur != entries[dest]['slim']:
            kind = 'upstream text is back' if sha(cur) == entries[dest]['orig'] else 'differs'
            print('  [out of sync] %s (%s, %d chars): run apply' % (dest, kind, len(cur)))
            bad += 1
    custom = {r[0] for r in load_sources() if r[1] == 'CUSTOM'}
    longs = []
    for dest in iter_skills(args.all):
        if dest in entries:
            continue
        cur = read_description(os.path.join(ROOT, dest, 'SKILL.md'))
        if cur and len(cur) > args.limit:
            longs.append((len(cur), dest, dest in custom))
    longs.sort(reverse=True)
    print('long descriptions (> %d chars) without a trimmed version: %d%s' %
          (args.limit, len(longs), '' if args.all else '  (skills/ only; use --all for plugin-skills/)'))
    for n, dest, is_custom in longs[:args.top]:
        print('  %4d  %s%s' % (n, dest, '  (CUSTOM: edit SKILL.md directly)' if is_custom else ''))
    if len(longs) > args.top:
        print('  ... %d more (--top N)' % (len(longs) - args.top))
    print('after trimming one by hand run: slim-descriptions.py capture <dest>')
    return 1 if bad else 0


# --------------------------------------------------------------------------- self test
def cmd_selftest(_):
    samples = {
        'folded': '---\nname: a\ndescription: >\n  Long folded text that\n  spans lines. Use when X.\nlicense: MIT\n---\n# Body\n',
        'dquote': '---\nname: a\ndescription: "A \\"quoted\\" word, colon: ok"\nlicense: MIT\n---\nBody\n',
        'squote': "---\nname: a\ndescription: 'It''s single quoted'\nmetadata:\n  version: 1\n---\nBody\n",
        'plain': '---\nname: a\ndescription: plain text that continues\n  on the next line\nlicense: MIT\n---\nBody\n',
        'literal': '---\nname: a\ndescription: |\n  Line one\n\n  Line two\nversion: "1"\n---\nBody\n',
        'crlf': '---\r\nname: a\r\ndescription: >\r\n  Windows line\r\n  endings\r\nlicense: MIT\r\n---\r\nBody\r\n',
        'last': '---\nname: a\nlicense: MIT\ndescription: last key in the block\n---\nBody\n',
        'chinese': '---\nname: a\ndescription: 中文描述，包含: 冒号 和 "引号"\n---\nBody\n',
    }
    expect = {
        'folded': 'Long folded text that spans lines. Use when X.',
        'dquote': 'A "quoted" word, colon: ok',
        'squote': "It's single quoted",
        'plain': 'plain text that continues on the next line',
        'literal': 'Line one Line two',
        'crlf': 'Windows line endings',
        'last': 'last key in the block',
        'chinese': '中文描述，包含: 冒号 和 "引号"',
    }
    fails = 0
    with tempfile.TemporaryDirectory() as td:
        for k, text in samples.items():
            p = os.path.join(td, k + '.md')
            open(p, 'w', encoding='utf-8', newline='').write(text)
            got = read_description(p)
            if got != expect[k]:
                print('FAIL read %s: %r != %r' % (k, got, expect[k]))
                fails += 1
                continue
            slim = 'Short "text": with \\ backslash and 中文.'
            write_description(p, slim)
            after = open(p, encoding='utf-8', newline='').read()
            if read_description(p) != slim:
                print('FAIL roundtrip %s: %r' % (k, read_description(p)))
                fails += 1
            body = text.split('---')[-1] if '\r\n' not in text else text.split('---')[-1]
            if not after.endswith(body):
                print('FAIL body changed %s' % k)
                fails += 1
            keep = [l for l in text.splitlines() if re.match(r'^(name|license|version|metadata):|^  version', l)]
            for l in keep:
                if l not in after.splitlines():
                    print('FAIL other key lost %s: %r' % (k, l))
                    fails += 1
            if ('\r\n' in text) != ('\r\n' in after):
                print('FAIL newline style changed %s' % k)
                fails += 1
            before = after
            write_description(p, slim)
            if open(p, encoding='utf-8', newline='').read() != before:
                print('FAIL not idempotent %s' % k)
                fails += 1
    print('selftest: %s (%d cases)' % ('OK' if not fails else '%d FAILURES' % fails, len(samples)))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('capture', help='record descriptions that differ from upstream')
    c.add_argument('dest', nargs='*')
    c.add_argument('--no-fetch', action='store_true', help='use the existing upstream cache as is')
    c.add_argument('--dry-run', action='store_true')
    c.set_defaults(fn=cmd_capture)
    a = sub.add_parser('apply', help='write registered trimmed descriptions into SKILL.md')
    a.add_argument('dest', nargs='*')
    a.add_argument('--strict', action='store_true', help='skip entries whose upstream text changed')
    a.add_argument('--quiet', action='store_true')
    a.add_argument('--exact', action='store_true', help='dest arguments are exact directories (no substring match)')
    a.set_defaults(fn=cmd_apply)
    s = sub.add_parser('status', help='show out-of-sync entries and long untrimmed descriptions')
    s.add_argument('--all', action='store_true', help='include plugin-skills/')
    s.add_argument('--limit', type=int, default=LONG_LIMIT)
    s.add_argument('--top', type=int, default=25)
    s.set_defaults(fn=cmd_status)
    t = sub.add_parser('selftest')
    t.set_defaults(fn=cmd_selftest)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == '__main__':
    main()
