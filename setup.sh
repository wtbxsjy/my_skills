#!/bin/bash
# Claude Code Environment Setup Script (Linux/macOS / Git Bash)
# Run: bash setup.sh

set -e

SKIP_PLUGINS=false
SKIP_SKILLS=false
SKIP_CONFIG=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --skip-plugins) SKIP_PLUGINS=true; shift ;;
        --skip-skills)  SKIP_SKILLS=true; shift ;;
        --skip-config)  SKIP_CONFIG=true; shift ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

CLAUDE_DIR="$HOME/.claude"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "========================================"
echo " Claude Code Environment Setup"
echo "========================================"

# --- Step 1: Install Plugins ---
if [ "$SKIP_PLUGINS" = false ]; then
    echo ""
    echo "[1/4] Installing plugins..."

    plugins=(
        "code-review@claude-plugins-official"
        "skill-creator@claude-plugins-official"
        "github@claude-plugins-official"
        "playwright@claude-plugins-official"
        "commit-commands@claude-plugins-official"
        "claude-code-setup@claude-plugins-official"
        "clangd-lsp@claude-plugins-official"
    )

    for plugin in "${plugins[@]}"; do
        echo "  Installing $plugin..."
        claude plugins install "$plugin" || echo "  Warning: failed to install $plugin"
    done
    echo "  Plugins installed."
fi

# --- Step 2: Configure Skills ---
if [ "$SKIP_SKILLS" = false ]; then
    echo ""
    echo "[2/4] Setting up skills..."

    if [ ! -d "$HOME/.cc-switch" ]; then
        echo "  .cc-switch not found. Clone it first:"
        echo "    git clone <your-cc-switch-repo> $HOME/.cc-switch"
    fi

    mkdir -p "$CLAUDE_DIR/skills"

    # Symlink skills from .cc-switch to .claude/skills
    # Adjust the list below based on which skills you want active
    active_skills=(
        "start" "read-file" "read-memories" "query"
        "alt-text" "ggsql" "implement" "working-on"
    )

    for skill in "${active_skills[@]}"; do
        src="$HOME/.cc-switch/skills/$skill"
        dst="$CLAUDE_DIR/skills/$skill"
        if [ -d "$src" ] && [ ! -e "$dst" ]; then
            echo "  Linking skill: $skill"
            ln -s "$src" "$dst"
        fi
    done
    echo "  Skills configured."
fi

# --- Step 3: Apply Settings ---
if [ "$SKIP_CONFIG" = false ]; then
    echo ""
    echo "[3/4] Applying settings..."

    repo_config="$SCRIPT_DIR/config/settings.template.json"
    target_config="$CLAUDE_DIR/settings.json"

    if [ -f "$repo_config" ]; then
        if [ ! -f "$target_config" ]; then
            echo "  Installing settings template..."
            cp "$repo_config" "$target_config"
            echo "  IMPORTANT: Edit $target_config to set your API keys!"
        else
            echo "  settings.json already exists. Compare with template:"
            echo "    diff $target_config $repo_config"
        fi
    else
        echo "  No settings template found in repo."
    fi

    # Create settings.local.json if not exists
    local_config="$CLAUDE_DIR/settings.local.json"
    if [ ! -f "$local_config" ]; then
        echo '{"permissions":{"allow":[]}}' > "$local_config"
        echo "  Created settings.local.json for machine-specific overrides."
    fi

    echo "  Settings applied."
fi

# --- Step 4: Verify ---
echo ""
echo "[4/4] Verifying setup..."

echo "  Claude Code version:"
claude --version 2>/dev/null || echo "  (claude CLI not found in PATH)"

echo "  Skills directory contents:"
ls -1 "$CLAUDE_DIR/skills" 2>/dev/null | sed 's/^/    - /'

echo "  Installed plugins:"
claude plugins list 2>/dev/null || echo "  (run 'claude plugins list' to check)"

echo ""
echo "========================================"
echo " Setup complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "  1. Edit $CLAUDE_DIR/settings.json to set your API keys"
echo "  2. Customize which skills are activated via symlinks"
echo "  3. Set GITHUB_TOKEN environment variable for GitHub MCP"
