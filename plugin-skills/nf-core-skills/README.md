# nf-core-skills

来自 [edmundmiller/nf-core-skills](https://github.com/edmundmiller/nf-core-skills)（MIT，基线提交 `a31e15c`；
上游说明它将来会迁移到 `nf-core/skills`）。

导入 2 个 skill：`nf-core-pipeline`（创建/修改 nf-core 流水线）、`nf-core-lint`（运行并解读 `nf-core pipelines lint`）。

未导入：上游的 `plugins/nf-core-tools` skill（只是在其仓库内运行 `prek` 钩子的开发工具）以及 `.claude/hooks`、
`scripts/prek-hooks` 下的钩子脚本——它们是该仓库自己的 CI/开发约束，不属于 skill。

同步：`bash update-skills.sh plugin-skills/nf-core-skills`
