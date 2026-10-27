# scientific-agent-skills

来自 [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
（现已更名为 Scientific Agent Skills / `K-Dense-AI/scientific-agent-skills`，MIT，基线提交 `5f2bc03`，版本 2.72.0）。

177 个科研类 skill：生物信息、化学信息、蛋白质、临床、神经科学、显微/影像、地球科学、物理、工程、
数据分析与可视化、科学写作、实验室自动化、监管与标准等，另含 `nextflow` skill。只导入 `skills/` 目录
（上游的 255MB `docs/`、测试与脚本未导入）。各 skill 的 frontmatter 里保留了各自的许可证声明（MIT / Apache-2.0 / BSD-3-Clause 等）。

与本仓库 `skills/` 下有 2 个同名项：`literature-review`、`scvi-tools`（内容各自独立，放在本目录下互不冲突）。
`paperclip`、`pi-agent` 两个 skill 的文档里包含 `curl ... | bash` 形式的第三方安装命令，使用前请自行审阅。

同步：`bash update-skills.sh plugin-skills/scientific-agent-skills`（会同步全部 177 个）
