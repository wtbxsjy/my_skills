---
name: nextflow-agents
description: >
  Write, run and debug Nextflow `agent` blocks: the process-like primitive (Nextflow 26.10+, preview)
  that runs an LLM-driven step inside a pipeline with typed inputs/outputs, a rendered prompt,
  tools (`nf:module_run`, `fs:*`, `shell:bash`), skills, caching, retries and lineage. Use when the user
  mentions Nextflow agents, `agent {` blocks, `agent.runner`, the `nf-agent` / `nf-agent-pi` plugins,
  "LLM step in a Nextflow pipeline", agentic map-reduce, or docs.seqera.io/nextflow/agent. Not for
  coding agents that help write Nextflow (see the nextflow-skills-guide skill) and not for ordinary processes.
argument-hint: <what the agent should do | error message>
allowed-tools: Bash, Read, Write, Edit
---

You are helping with **Nextflow agents** — an LLM-driven pipeline step, not a coding assistant.
Request: `$@`

Everything here comes from the official docs page (`references/agent-docs.md`, source
https://docs.seqera.io/nextflow/agent) and the official examples (`references/examples/`). It describes a
**preview** feature of **Nextflow 26.10**: syntax and behavior may change. It was not executed when this
skill was written (Nextflow 26.10 and an LLM key were not available), so when something fails, trust the
installed version's behavior over this text and re-read the docs page.

## Step 1 — Check the environment

```bash
nextflow -version          # needs 26.10 or later (calendar versioning: 26.10 > 26.04 > 25.10)
```

- Older Nextflow → agents are not available; use the `install-nextflow` skill (in
  `plugin-skills/nextflow-agent-skills` or `plugin-skills/seqera-nextflow-plugin`) to upgrade.
- A model credential must be available to the *driver*: `agent.apiKey`, `NXF_AGENT_API_KEY`, or the
  provider variable (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `MISTRAL_API_KEY`,
  `OPENROUTER_API_KEY`, `AZURE_OPENAI_API_KEY`). Never put keys into the script, the process
  environment or a committed config; use `secrets.NAME` in config.
- Pick a **runner** (config `agent.runner`):
  - `langchain4j` (default): runs in the driver JVM, no container. No `shell:bash`.
  - `pi`: runs every agent in a **container** (needs a container engine, plugin `nf-agent-pi`, and the runner
    image published with the Nextflow release; override with `agent.container`). Required for `shell:bash`.

## Step 2 — Write the agent

Minimal skeleton (typed DSL, structured output):

```nextflow
nextflow.enable.types = true

record Analysis {
    summary: String
    confidence: Float
}

agent analyst {
    model 'openai/gpt-5-mini'                       // <provider>/<model>
    instruction 'You are a precise scientific analyst. Be concise and honest about uncertainty.'

    input:
    question: String

    output:
    result: Analysis                                // typed output => JSON-schema-validated answer

    prompt:
    """
    Analyze the following question: ${question}
    """
}

workflow {
    analyst(channel.of('Is FASTQ a binary or a text format?')).view()
}
```

```groovy
// nextflow.config
agent.runner = 'pi'            // or 'langchain4j'
docker.enabled = true          // pi runner needs a container engine
```

Rules to apply while writing:

- An agent has **exactly one output**: a typed value (record/`Boolean`/`Float`/`Integer`/`List`/`Path`/`String`),
  or an output expression built from `stdout()`, `file()`, `files()`. Use a **record** for several values.
- Each input is serialized as JSON and appended to the model message even if the prompt does not mention it.
- File outputs only exist if the prompt **tells the agent to write that file**; otherwise a missing-output error is raised.
- Directives: `model`, `instruction` (system prompt), `goal` (objective for multi-turn work), `maxIterations`
  (default 20), `tools`, `skills`, `label`; task directives (`cpus`, `memory`, `container`, `executor`, ...) go in
  the `agent {}` config scope. Agents **do not inherit** the `process` scope.
- **Tools** are namespaced refs `<family>[:<group>]:<name>`; an agent only gets what it declares:
  - `nf:module_run` (all processes in scope, or `nf:module_run:SAMTOOLS_*`, wildcard only in the name segment);
    a process must be typed or have a module spec to be callable. A failing tool task fails the agent run.
  - `fs:*` (`read`, `write`, `edit`, `ls`, `grep`, `find`), sandboxed to the agent's work directory.
  - `shell:bash` (pi runner only).
- **Skills** are `SKILL.md` folders the model loads on demand: local (`skills 'name'` → `skills/name/` beside the
  script) or remote (`github.com/<org>/<repo>@<rev>`). They are instructions only, no code runs. A remote
  skill becomes model instructions: treat it as untrusted and **pin a commit SHA**.
- Agents can be packaged as modules (`include { reporter } from './agents/reporter'`) that carry their own
  `skills/` and `tools/`; run one with `nextflow module run ./agents/reporter --request '...'`.

## Step 3 — Run and inspect

```bash
nextflow run main.nf -with-agent-trace      # readable trace of each agent run (agent.trace)
nextflow run main.nf -resume                # replays a stored agent run when the hash is unchanged
nextflow lineage find type=AgentRun         # agent runs are AgentRun lineage records, not TaskRun
```

- **Caching is replay, not determinism.** The task hash covers runner, model, endpoint, instruction, goal,
  max iterations, prompt, inputs, output schema, skills (capped at 64 files / 256 KB) and tools. Use `cache false`
  to opt out.
- Provider resolution order: `agent.apiProvider` → host of `agent.baseUrl` → `model` prefix. Credentials:
  config → `NXF_AGENT_API_KEY`/`NXF_AGENT_BASE_URL` → `<PROVIDER>_API_KEY`/`_BASE_URL`. Containerized agents get
  credentials over RPC (TLS on by default); `agent.rpc.remoteHost` is the knob when the driver host cannot be inferred.
- Within one agent, tool calls are sequential; different agent tasks run in parallel (one task per channel item).
- Bound cost and runtime: `maxIterations`, `requestTimeout` (default 120 sec), a clear `goal`, and narrow `tools`.

## Step 4 — Pick an example to start from

The folder `references/examples/` has 18 official examples, simple → complex (see its `README.md`):
`01_structured-output`, `02_two-agents`, `03_skills`, `04_tool`, `05_tool-parallel`, `06_tool-structured`,
`07_module-as-tool`, `08_filesystem`, `09_goal-directed`, `10_convergence-loop`, `11_contig-filter`,
`12_isolate-triage`, `13_samplesheet-builder`, `14_data-labelling`, `15_map-reduce`, `16_fan-in-parity`,
`17_agent-module`, `19_shell-tools`. Examples 07, 09, 11 and 12 expect an input FASTQ in `data/`
(the upstream symlink to `examples/data` was not copied; download the test FASTQ as described in the examples
README) and need Wave for the nf-core module images.

## Common problems

| Symptom | Likely cause / fix |
|---|---|
| Agents not recognized / syntax error on `agent` | Nextflow < 26.10, or the runner plugin is not loadable; set `agent.runner` (loads `nf-agent` / `nf-agent-pi`) |
| `Unsupported protocol version` | `agent.container` pinned to an older `nf-agent-pi` image (< 0.4.1); remove the pin |
| `shell:bash` rejected before the run | only the `pi` runner supports it |
| Missing-output error | the prompt did not instruct the agent to write the declared `file(...)` |
| Tool not found / ref selects nothing | the process is not in scope (`include` it) or the ref pattern is wrong; a ref selecting nothing is an error |
| Credentials not found | set `agent.apiKey` or the provider variable on the machine running the **driver** |
| Result changes between runs | models are non-deterministic; `-resume` only replays a stored run |

## License note

`references/agent-docs.md` is the Nextflow documentation (CC BY-SA 4.0, © Seqera); `references/examples/` are the
official examples from the Nextflow repository (Apache-2.0). Attribution is kept in those files.
