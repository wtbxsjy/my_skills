#!/usr/bin/env bash
# =============================================================================
# update-skills.sh — 从上游源仓库同步 skills/ 与 plugin-skills/ 的最新版本
#
# 用法:
#   bash update-skills.sh              # 同步全部 skill
#   bash update-skills.sh <skill-dir>  # 只同步指定 skill（如 skills/taste-skill）
#
# 依赖: git, cp（rsync 可选）
# 说明: 映射表见 SOURCES.tsv；目标目录与上游"镜像"同步（多余文件会被删除）。
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TSV="$ROOT/SOURCES.tsv"
CACHE_DIR="${MY_SKILLS_CACHE:-${XDG_CACHE_HOME:-$HOME/.cache}/my_skills-update}"
FILTER="${1:-}"

if [[ ! -f "$TSV" ]]; then
  echo "错误: 找不到 $TSV" >&2
  exit 1
fi

mkdir -p "$CACHE_DIR"

# 读取映射: 目标目录|仓库URL|分支|仓库内路径|备注
declare -a DEST=( ) REPO=( ) BRANCH=( ) SRCPATH=( )
while IFS='|' read -r dest repo branch srcpath note; do
  [[ -z "$dest" || "$dest" == \#* ]] && continue
  DEST+=("$dest"); REPO+=("$repo"); BRANCH+=("$branch"); SRCPATH+=("${srcpath:-.}")
done < "$TSV"

clone_or_update() {
  local repo="$1" branch="$2"
  local slug repo_dir
  slug="$(echo "$repo" | sed 's#https://github.com/##; s#\.git$##; s#/#__#g')"
  repo_dir="$CACHE_DIR/$slug"
  if [[ -d "$repo_dir/.git" ]]; then
    echo "  [缓存] $repo"
    git -C "$repo_dir" fetch --depth 1 origin "$branch" >/dev/null 2>&1 || true
  else
    echo "  [克隆] $repo @ $branch"
    git clone --depth 1 --filter=blob:none --sparse -b "$branch" "$repo" "$repo_dir" >/dev/null 2>&1
  fi
  echo "$repo_dir"
}

declare -A CLONED
count_total=0; count_updated=0

for i in "${!DEST[@]}"; do
  dest="${DEST[$i]}"; repo="${REPO[$i]}"; branch="${BRANCH[$i]}"; srcpath="${SRCPATH[$i]}"
  [[ -n "$FILTER" && "$dest" != *"$FILTER"* ]] && continue
  count_total=$((count_total + 1))

  abs_dest="$ROOT/$dest"
  if [[ "$dest" == "CUSTOM" || "$srcpath" == "CUSTOM" ]]; then
    echo "  [跳过] $dest (自定义 skill，无公开源)"
    continue
  fi

  repo_dir="${CLONED[$repo]:-}"
  if [[ -z "$repo_dir" ]]; then
    repo_dir="$(clone_or_update "$repo" "$branch")"
    CLONED["$repo"]="$repo_dir"
    # 稀疏检出本仓库需要的全部路径
    paths=()
    for j in "${!DEST[@]}"; do
      if [[ "${REPO[$j]}" == "$repo" ]]; then
        p="${SRCPATH[$j]}"
        [[ "$p" != "." ]] && paths+=("$p")
      fi
    done
    if [[ ${#paths[@]} -gt 0 ]]; then
      git -C "$repo_dir" sparse-checkout set "${paths[@]}" >/dev/null 2>&1 || true
    fi
  fi

  src="$repo_dir/$srcpath"
  if [[ ! -d "$src" ]]; then
    echo "  [警告] 源路径不存在: $repo/$srcpath"
    continue
  fi

  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$src/" "$abs_dest/"
  else
    rm -rf "$abs_dest"
    cp -a "$src" "$abs_dest"
  fi
  echo "  [更新] $dest <- $repo:$branch/$srcpath"
  count_updated=$((count_updated + 1))
done

echo
echo "完成: 共处理 $count_total 个目录，更新 $count_updated 个"
