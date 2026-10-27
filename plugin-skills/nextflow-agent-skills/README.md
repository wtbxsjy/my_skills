# nextflow-agent-skills

来自 [nextflow-io/agent-skills](https://github.com/nextflow-io/agent-skills)（Nextflow 官方，Apache-2.0，基线提交 `5ed41d0`）。

5 个 skill，围绕 Nextflow Registry 的模块：`install-nextflow`、`create-workflow`、`run-module`、
`launch-workflow`、`migrate-nextflow-code`。需要 Nextflow 26.04+（工作流模块需要 26.10+）。
`launch-workflow` 依赖 Seqera MCP（`https://mcp.seqera.io/mcp`，上游的 `.mcp.json` 未导入，需要自行配置）。

与 `../seqera-nextflow-plugin/` 有 4 个同名 skill（`install-nextflow`、`launch-workflow`、
`migrate-nextflow-code`、`run-module`），内容不同（Seqera 版是增强改编版）。两套同时启用会重名，
选用方法见 `skills/nextflow-skills-guide`。

同步：`bash update-skills.sh plugin-skills/nextflow-agent-skills`
