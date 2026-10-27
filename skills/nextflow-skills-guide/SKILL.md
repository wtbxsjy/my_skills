---
name: nextflow-skills-guide
description: >
  Map of every Nextflow / nf-core related skill in this repository and which one to use for a task:
  building, converting (Snakemake, scripts, notebooks), migrating, testing, debugging and running Nextflow
  pipelines; nf-core pipelines and lint; Seqera Platform and the Seqera MCP; Nextflow Registry modules;
  Nextflow `agent` blocks. Also explains the duplicated skill names (install-nextflow, run-module,
  launch-workflow, migrate-nextflow-code, nextflow-development) and how to enable one copy. Use when the
  user asks "which Nextflow skill", mentions Nextflow/nf-core/Seqera and it is unclear which skill fits,
  or wants to set up Nextflow skills for an agent.
argument-hint: <task description>
allowed-tools: Read, Bash
---

Task: `$@`

The Nextflow skills in this repository come from six sources. They are stored **by source** so that
same-named skills do not collide. Pick the row for the task, then read that skill's `SKILL.md`.

| Source (path in this repo) | What it is |
|---|---|
| `plugin-skills/seqera-nextflow-plugin/` | 28 skills from `seqeralabs/nextflow-plugin` (Apache-2.0): the broadest set |
| `plugin-skills/nextflow-agent-skills/` | 5 skills from `nextflow-io/agent-skills` (Apache-2.0), Nextflow Registry focused |
| `plugin-skills/nf-core-skills/` | `nf-core-pipeline`, `nf-core-lint` from `edmundmiller/nf-core-skills` (MIT) |
| `skills/nf-core-agents-md/` | nf-core's official `AGENTS.md` rules (from `nf-core/agents`, MIT) |
| `skills/nextflow-agents/` | the Nextflow `agent` block (docs.seqera.io/nextflow/agent, Nextflow 26.10 preview) |
| `plugin-skills/scientific-agent-skills/nextflow` | one general Nextflow skill inside the K-Dense science collection |
| `skills/nextflow-development` | older Anthropic skill that runs nf-core pipelines (rnaseq, sarek, atacseq) on FASTQ data |

## Task → skill

| I want to... | Use |
|---|---|
| Install or upgrade Nextflow / Java | `install-nextflow` (see "Duplicated names") |
| Plan and scaffold a new pipeline from scripts, notebooks, papers, or instructions | `seqera-nextflow-plugin/build-nextflow-pipeline` |
| Compose a pipeline from Nextflow Registry modules | `nextflow-agent-skills/create-workflow` (+ `run-module`) |
| Find an existing module for a tool (nf-core first), or alternative tools for a step | `seqera-nextflow-plugin/search-existing-modules`, `find-alternative-tools` |
| Build and verify a container for a tool | `seqera-nextflow-plugin/create-container` |
| Convert a Snakemake workflow, or judge whether source material is convertible | `seqera-nextflow-plugin/migrate-from-snakemake`, `audit-conversion-readiness` |
| Design pipeline structure (subworkflows, channels, output patterns) | `seqera-nextflow-plugin/nf-pipeline-design`, `nextflow-output-patterns`, `nf-docker-scripts` |
| Write or explain `nextflow.config`; create `nextflow_schema.json` | `seqera-nextflow-plugin/nextflow-config`, `nextflow-schema` |
| Upgrade code for new Nextflow versions, strict syntax, static typing | `seqera-nextflow-plugin/migrate-nextflow-code` |
| Write tests / fix failing tests | `seqera-nextflow-plugin/nf-test` |
| Debug a failed local run | `seqera-nextflow-plugin/debug-local-run`, `repair-workflow`, `nextflow-history`, `nf-data-lineage` |
| Run one Registry module quickly | `run-module` |
| Run a standard nf-core pipeline (rnaseq, sarek, atacseq) on FASTQs | `seqera-nextflow-plugin/nextflow-development` (adapted) or `skills/nextflow-development` (original) |
| Create or modify an nf-core pipeline, run `nf-core pipelines lint` | `nf-core-skills/nf-core-pipeline`, `nf-core-lint`, **and** `skills/nf-core-agents-md` rules |
| Maintain an nf-core pipeline (template sync, module updates) | `seqera-nextflow-plugin/maintain-nf-core-pipeline` |
| Develop or migrate a Nextflow plugin | `seqera-nextflow-plugin/nf-plugin-development`, `nf-plugin-legacy-migration` |
| Launch on cloud/HPC with Seqera Platform; set up compute environments, credentials, data links, seqerakit | `launch-workflow`, `ce-credentials-setup`, `seqera-data-links`, `seqerakit`, `debug-seqera-failed-run` |
| Put an LLM step **inside** a pipeline (`agent` blocks) | `skills/nextflow-agents` |
| General Nextflow help with HPC/SLURM, samplesheets, channels | `scientific-agent-skills/nextflow` |

## Duplicated names and which copy to enable

Agents load skills by `name:`, so enable **one** copy of each:

| Name | Copies | Suggested copy |
|---|---|---|
| `install-nextflow` | seqera-nextflow-plugin, nextflow-agent-skills | either (near identical); seqera version |
| `run-module` | both | `nextflow-agent-skills`: larger, covers process **and** workflow modules |
| `launch-workflow` | both | `seqera-nextflow-plugin`: bundles the Seqera MCP connection reference |
| `migrate-nextflow-code` | both | `seqera-nextflow-plugin`: far larger (version, strict-syntax, typing references) |
| `nextflow-development` | seqera-nextflow-plugin (adapted for the plugin), `skills/nextflow-development` (original) | `seqera-nextflow-plugin` if you use the Seqera MCP, else the original |

These suggestions come from comparing the copies' size and descriptions; they are not upstream guidance.
`create-workflow` exists only in `nextflow-agent-skills`; most other skills exist only in `seqera-nextflow-plugin`.

To enable a skill for an agent, link or copy **that skill's directory** into the agent's skills folder
(for example `~/.claude/skills/<name>`). Keep each plugin's skills together when they cross-reference each
other: almost every Seqera skill links to `launch-workflow/references/seqera-mcp/README.md` with a relative
path, so if you enable any of the Seqera skills, enable `launch-workflow` from `seqera-nextflow-plugin` as well
(and keep the sibling layout, i.e. link the directories into the same parent folder).

## Prerequisites that recur

- **Nextflow**: calendar versioning (`YY.MM.PATCH`; 26.04.0 is newer than 25.10.1). Registry modules need 26.04+,
  workflow modules 26.10+, `agent` blocks 26.10+ (preview). Needs Java 17+.
- **Seqera MCP** for Seqera Platform skills: `https://mcp.seqera.io/mcp` (OAuth sign-in on first use). The upstream
  `.mcp.json` files were not imported; add the server to your agent configuration yourself.
- **nf-core tools** (`nf-core`), **nf-test**, and **prek** for nf-core pipeline work.
- Never write a throwaway wrapper workflow just to test a single module; use `nextflow module run`.

## Official documentation

- Nextflow docs: https://docs.seqera.io/nextflow (agents page: https://docs.seqera.io/nextflow/agent)
- Nextflow Registry: https://registry.nextflow.io; nf-core: https://nf-co.re; nf-test: https://www.nf-test.com
- Sources: https://github.com/seqeralabs/nextflow-plugin, https://github.com/nextflow-io/agent-skills,
  https://github.com/edmundmiller/nf-core-skills, https://github.com/nf-core/agents,
  https://github.com/K-Dense-AI/claude-scientific-skills
