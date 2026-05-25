# Claude Code Environment Setup Script (Windows PowerShell)
# Run this script to sync your Claude Code environment on a new machine

param(
    [switch]$SkipPlugins,
    [switch]$SkipSkills,
    [switch]$SkipConfig
)

$ErrorActionPreference = "Stop"
$CLAUDE_DIR = "$env:USERPROFILE\.claude"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Claude Code Environment Setup"
Write-Host "========================================" -ForegroundColor Cyan

# --- Step 1: Install Plugins ---
if (-not $SkipPlugins) {
    Write-Host "`n[1/4] Installing plugins..." -ForegroundColor Yellow

    $plugins = @(
        "code-review@claude-plugins-official",
        "skill-creator@claude-plugins-official",
        "github@claude-plugins-official",
        "playwright@claude-plugins-official",
        "commit-commands@claude-plugins-official",
        "claude-code-setup@claude-plugins-official",
        "clangd-lsp@claude-plugins-official"
    )

    foreach ($plugin in $plugins) {
        Write-Host "  Installing $plugin..."
        claude plugins install $plugin
    }
    Write-Host "  Plugins installed." -ForegroundColor Green
}

# --- Step 2: Configure Skills ---
if (-not $SkipSkills) {
    Write-Host "`n[2/4] Setting up skills..." -ForegroundColor Yellow

    if (-not (Test-Path "$env:USERPROFILE\.cc-switch")) {
        Write-Host "  .cc-switch not found. Clone it first:"
        Write-Host "    git clone <your-cc-switch-repo> $env:USERPROFILE\.cc-switch"
    }

    if (-not (Test-Path "$CLAUDE_DIR\skills")) {
        New-Item -ItemType Directory -Path "$CLAUDE_DIR\skills" -Force | Out-Null
    }

    # Symlink skills from .cc-switch to .claude/skills
    # Adjust the list below based on which skills you want active
    $activeSkills = @(
        "start", "read-file", "read-memories", "query",
        "alt-text", "ggsql", "implement", "working-on"
    )

    foreach ($skill in $activeSkills) {
        $src = "$env:USERPROFILE\.cc-switch\skills\$skill"
        $dst = "$CLAUDE_DIR\skills\$skill"
        if ((Test-Path $src) -and -not (Test-Path $dst)) {
            Write-Host "  Linking skill: $skill"
            New-Item -ItemType SymbolicLink -Path $dst -Target $src -Force | Out-Null
        }
    }
    Write-Host "  Skills configured." -ForegroundColor Green
}

# --- Step 3: Apply Settings ---
if (-not $SkipConfig) {
    Write-Host "`n[3/4] Applying settings..." -ForegroundColor Yellow

    $repoConfig = "$PSScriptRoot\config\settings.template.json"
    $targetConfig = "$CLAUDE_DIR\settings.json"

    if (Test-Path $repoConfig) {
        if (-not (Test-Path $targetConfig)) {
            Write-Host "  Installing settings template..."
            Copy-Item $repoConfig $targetConfig
            Write-Host "  IMPORTANT: Edit $targetConfig to set your API keys!" -ForegroundColor Red
        } else {
            Write-Host "  settings.json already exists. Compare with template:"
            Write-Host "    diff $targetConfig $repoConfig"
        }
    } else {
        Write-Host "  No settings template found in repo." -ForegroundColor Yellow
    }

    # Create settings.local.json if not exists
    $localConfig = "$CLAUDE_DIR\settings.local.json"
    if (-not (Test-Path $localConfig)) {
        @{
            "permissions" = @{
                "allow" = @()
            }
        } | ConvertTo-Json -Depth 3 | Set-Content $localConfig
        Write-Host "  Created settings.local.json for machine-specific overrides."
    }

    Write-Host "  Settings applied." -ForegroundColor Green
}

# --- Step 4: Verify ---
Write-Host "`n[4/4] Verifying setup..." -ForegroundColor Yellow

Write-Host "  Claude Code version:"
claude --version 2>$null

Write-Host "  Skills directory contents:"
Get-ChildItem "$CLAUDE_DIR\skills" -Directory | ForEach-Object { Write-Host "    - $($_.Name)" }

Write-Host "  Installed plugins:"
claude plugins list 2>$null

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " Setup complete!"
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Edit $CLAUDE_DIR\settings.json to set your API keys"
Write-Host "  2. Customize which skills are activated via symlinks"
Write-Host "  3. Set GITHUB_TOKEN environment variable for GitHub MCP"
