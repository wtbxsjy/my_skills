# seqera-nextflow-plugin

来自 [seqeralabs/nextflow-plugin](https://github.com/seqeralabs/nextflow-plugin)（Seqera，Apache-2.0，基线提交 `fad06b4`）。

28 个 skill：构建流水线、转换为 Nextflow（含 Snakemake/Python/R）、迁移与现代化、测试与调试、
Nextflow Platform（Seqera）操作。`LICENSE`、`NOTICE`、`licenses/` 为上游的许可与第三方声明；
`scripts/` 是 `migrate-nextflow-code` 引用的静态类型检查辅助脚本（可选）。

使用注意：
- 这些 skill 之间有相对路径引用（例如到 `launch-workflow/references/seqera-mcp/`），请整体保留本目录结构。
- 涉及 Seqera Platform 的 skill 需要 Seqera MCP（`https://mcp.seqera.io/mcp`，OAuth 登录）；上游的 `.mcp.json` 未导入。
- 与 `../nextflow-agent-skills/` 有 4 个同名 skill，另有 `nextflow-development`（改编自本仓库 `skills/nextflow-development`），
  同时启用会重名，选用方法见 `skills/nextflow-skills-guide`。

同步：`bash update-skills.sh plugin-skills/seqera-nextflow-plugin`
