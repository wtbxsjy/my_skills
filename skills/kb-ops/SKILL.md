---
name: kb-ops
description: 本地知识库运维。当用户要新建知识库、采集资料入库（论文/Zotero/网页/笔记/RSS）、把 raw 记录编译成 wiki 页、校验库契约、看库状态、或排查知识库脚本报错时，使用此 skill。涉及 kb-template 脚手架、raw→wiki 单向数据流、value_gate 价值闸门、frontmatter JSON Schema 契约、R 编排（ellmer 结构化输出）、Obsidian vault 兼容。
---

# kb-ops · 知识库运维

一套 R 脚手架，把散乱资料编译成 Obsidian 可读的知识库。**每个库是一个 git 仓库，
既是 Obsidian vault 也是 agent 工作目录。**

运维规则全部住在本 skill 里，各库只在自己的 `CLAUDE.md` 写 delta。
改规则改这里，所有库同时生效——不要把规则复制到各库。

## 0. 先确认依赖

任何脚本报 `缺少必需的 R 包` → 跑一次安装脚本，它会建好用户库目录并逐个装：

```bash
cd <kb-template 或任意库根> && Rscript R/kb_setup.R
```

必需 5 个：`yaml` `jsonlite` `frontmatter` `ellmer` `digest`。
必需包装不上通常是缺系统编译依赖（`libcurl4-openssl-dev` `libssl-dev` `libxml2-dev`）；
可选包（`ollamar`/`targets`/`mall`/`vitals`）装不上只警告，不影响主流程。

`digest` 是**必需**，不是可选。无它时 `kb_checksum` 有退化实现，但精度低于
`xxhash64`，只作最后防线。`kb_setup.R` 与 `kb_doctor.R` 的定性必须一致——
两处不一致过，用户按 doctor 以为可以不装。

**版本下限（实测，不必追新）**：`ellmer` 0.4.1 与 `frontmatter` 0.2.0 已验证
API 兼容——源码用到的 `chat_anthropic`/`chat_ollama`/`chat_openai`/
`chat_openai_compatible`/`token_usage`/`type_from_schema` 与
`read_front_matter`/`write_front_matter` 全部存在，且
`type_from_schema(text, path)` 形参一致。看到版本比开发环境旧时，
先查函数是否存在与形参是否一致，再决定要不要让用户升级。

在**全新系统**上，缺的往往不是 R 包而是系统开发头文件：`jsonlite`/`digest`
要编译 C，`ellmer` 的依赖 `curl`/`openssl` 要链接系统库。此时
`install.packages()` 报的是**编译错误**而非"包不存在"，容易误判成包本身有问题。

## 1. 定位库根

所有命令都在库根下跑（含 `kb.config.yaml` 的目录）。脚本自己会向上找库根，
也支持 `KB_HOME` 环境变量在任意目录运行：

```bash
cd <库根> && Rscript R/kb_status.R
# 或
KB_HOME=<库根> Rscript <库根>/R/kb_status.R
```

拿不准库在哪：`ls ~/Knowledgebase/*/kb.config.yaml`。

## 2. 核心模型（理解这个，其余都是细节）

```
外部源 --adapter--> raw/*.md --compile--> wiki/*.md --> Obsidian 阅读
                    (不可变)              (可重写)
```

**三条不可违反的铁律：**

1. **`raw/` 是事实层，只增不改。** adapter 只写 `raw/`；编译层只读 `raw/` 的
   `body`，只回填 `status`/`compiled_at`/`checksum`。手工改 `raw/` 的 `body`
   是允许的（修正解析错误），但 id 永不改动。
2. **`wiki/` 是产物层，可被覆盖。** 不要在 `wiki/` 手写内容，除非同时加
   `human_edited: true`（加了机器就永不覆盖它）。要改内容，改 `raw/` 的源或改提示词。
3. **`value_gate` 是唯一硬闸。** 只有 `value_gate: keep` 且
   `status ∈ {raw, stale}` 的记录会被编译。这是防止库劣化的全部机制——
   宁可库小而准，不可大而杂。

**为什么要有价值闸门**：采集是廉价的，编译是昂贵的（token）且会污染库
（低质页会被后续检索到，误导后续判断）。闸门把"我采了什么"与"我认可什么"分开。
`skip` 的记录**保留在库里不删**——删了下次会被重新采集。

## 3. 常用任务

### 新建一个库

```bash
Rscript <kb-template>/R/kb_init.R \
  --path ~/Knowledgebase/<库名> --name "<中文名>" --topic <slug> \
  --sources paper,zotero,manual --provider ollama --git
```

- `--topic <slug>`：库的主题前缀，会成为所有 id 的前缀（如 `cardio-xxx`）。选定后不要改。
- `--sources`：只列本库真会用的。未列的 adapter 不会被复制进库——避免菜单式困惑。
- `--provider`：`ollama` / `anthropic` / `openai` / `deepseek` /
  `openai_compatible` / `stub`（未知值会直接报错而不是静默回落）。没配好模型时
  先用 `stub`（见 §5）。缺省是 `ollama`——本地优先，避免配置写坏时意外产生云端
  API 费用。**接 DeepSeek 要写 `deepseek`**，见 §7 第一条。

建完立刻跑 `Rscript R/kb_doctor.R`，它做真实探测（端口、包、外部脚本路径、
云端 provider 的 API key），不假设任何服务在跑。

**然后先编一页，再编全部**：

```bash
Rscript R/kb_compile.R --limit 1
```

产出形态不对就去填 `CLAUDE.md` 的「页面口味」节（想要的分节结构、要不要保留
原始数字、术语中英文如何处理、多长算合适、哪些明确不要），再
`Rscript R/kb_recompile.R --all` 复位重编。**这是整个建库流程里唯一无法靠脚本
代劳的一步**——形态定下来之前批量编译只是把不合意的产物做得更多。

### 采集

```bash
Rscript R/kb_ingest.R --source <s> --input <路径或URL> \
  [--dry-run] [--keep] [--overwrite] [--limit N] [--skip-verify]
```

| source | input 是什么 |
|---|---|
| `manual` | markdown 文件或目录（你自己写的笔记） |
| `paper` | PDF 文件或目录。委托已跑通的 Python 双引擎解析（见 `paper2knowledge` skill） |
| `zotero` | Zotero 导出的 JSON manifest；含 `pdf_path` 时转交 paper adapter |
| `web` | URL，或每行一个 URL 的文本文件 |
| `mineru` | MinerU 已解析出的目录（每篇一个子目录，含 md + content_list json） |
| `feed` | RSS/FreshRSS。**默认不启用**，见 §7 坑 5 |

- 先 `--dry-run` 看会落什么，再真跑。
- `--keep` 直接标 `value_gate: keep`（只在你已确信该批资料都要留时用）。
- **重跑默认跳过已存在的 id**——这保护你手工标过的 `value_gate` 不被覆盖。
  确实要重抓用 `--overwrite`（会丢失该记录上的人工标注）。

**`mineru` 与 `paper` adapter 的分工**（选错会白等 GPU）：

| adapter | 吃什么 | 需要 |
|---|---|---|
| `paper` | PDF 原文 | MinerU 服务在跑（默认 30000 端口）+ GPU |
| `mineru` | MinerU **已解析出的目录** | 无外部依赖 |

已经有解析产物就用 `mineru`，不要走 `paper` 重跑一遍解析。
`mineru` adapter 的元数据优先级是实测定的：**md 的首个 `# ` 标题优先**
（9 篇里 7 篇准），v2 json 的 `title[0]` 作退路但**须排除刊名与章节名**
（`Cell Metabolism`、`REFERENCES AND NOTES` 这类），目录名（编码了
作者+年份+刊物+短标题）作最后退路兼 id 来源。两边都失效时标
`parse_quality: partial` 并把诊断写进 `error` —— 这类记录仍可编译，
但复核时要优先看。

### 判定价值（唯一需要人做判断的环节）

```bash
Rscript R/kb_status.R          # 看有多少条 undecided
```

然后逐条把 `raw/<source>/<id>.md` 的 `value_gate` 改成 `keep` 或 `skip`。

判定标准建议写进各库自己的 `CLAUDE.md`（不同库标准不同）。通用建议：
- 只是"看着相关"→ `skip`。真要留的是**你会回来查的东西**。
- `parse_quality: poor` 的先修解析再判定，不要让坏正文进编译。

### 编译

```bash
Rscript R/kb_compile.R --dry-run     # 先看计划与预算
Rscript R/kb_compile.R --limit 10
Rscript R/kb_index.R                 # 重建索引（确定性，不烧 token）
Rscript R/kb_lint.R                  # 校验产物
```

编译层的硬约束（已在脚本里实现，不要绕过）：
- 单次页数与 token 上限来自 `kb.config.yaml` 的 `compile` 段，超了停在断点并写 `log.md`。
- 产物必须过 `schema/wiki_page.schema.json`；不合就把该 raw 记录标 `failed` 并写
  `error` 字段——不静默放过。
- 失败的记录下次会重试；连续失败看 `error` 字段，通常是提示词或解析质量问题。

**换 provider / 改提示词后必须先复位**，否则一条都不会编译：

```bash
Rscript R/kb_recompile.R --all --dry-run   # 先看会退回哪些、删哪些页
Rscript R/kb_recompile.R --all             # compiled → raw，并删旧 wiki 页
Rscript R/kb_compile.R
```

`kb_recompile.R --stub-only` 只退回 stub 编译的页（`compiled_by: stub`），
适合"stub 走通管线后第一次接真模型"这个最常见场景。
标了 `human_edited: true` 的页永不被删。

`compile` 段的三个长输出参数，数值都是实测定的（9 篇 MinerU 全文论文）：

| 键 | 建议值 | 不给会怎样 |
|---|---|---|
| `max_output_tokens` | 24000（输出上限低的模型 16000） | `ellmer` 默认对"整篇论文→结构化页"不够：**4000 时 9/9 全截断，12000 时仍 3 条截断** |
| `max_body_chars` | 10000（本地小模型 3500） | 不写进提示词模型会撞输出上限；但**给太小是"wiki 太薄"的头号原因**——3500 只够 bullet 摘要，定量结果全被省掉 |
| `max_input_chars` | 90000（本地小模型 20000–30000） | MinerU 全文 32k–110k 字符，后半是参考文献。`kb_compile` 会优先在 `References` 处截断并剥离内联图片行，所以可以放宽 |

### RCS 预处理（`rcs` / `rcs_min_chars`）

借鉴 paper-qa 的 RCS（分块重排序 + 上下文摘要）。正文超 `rcs_min_chars`（默认
8000）且能按 `##` 切出 ≥5 块时，先用一次调用给每块打分 1–5 + 写 ≤200 字摘要，
只把 ≥2 分的块摘要送进页面编译器。

**它解决的是 `max_input_chars` 解决不了的问题**：那个参数再大也是盲截断，切掉
的后半部分往往正是讨论与结论。RCS 按信息密度取舍——引言/致谢压缩、结果/讨论
保留，模型看到的从几万字符原文变成几千字符精炼摘要。代价是每条材料多一次调用。

- 材料普遍较短的库（会议记录、代码笔记）设 `rcs: no`：没有可压缩的冗余，
  白花一次调用。
- **所有失败路径都降级为原文**——连不上、评分失败、分块 <5、全被判 1 分。
  RCS 是优化不是硬依赖，评分挂了不该让整轮编译失败。
- `provider: stub` 下完全不触发。这条要盯：提示词在 stub 分支下**照样构建**，
  所以任何写在提示词构建路径上的 LLM 调用都会在占位符模式下偷发真实请求，
  必须自己加 `identical(provider, "stub")` 早退。同步这个功能时就踩了一次。
- 开了 RCS 之后，系统提示第 9 条「每小节末尾标注来源章节」从"锦上添花"变成
  必需——送进模型的是章节摘要，没有标注就无从判断结论出自原文哪一段。

**三个值要同比缩放，不要单调一个。** 短材料的库（会议记录、代码笔记、实验日志）
应整体下调，否则模型为凑长度而稀释内容。提示词里的 body 下限是从
`max_body_chars` 按 0.4 倍派生的，改目标值即可，不必动代码。

放宽 `max_body_chars` 后还要盯一次：实测长上下文模型在目标 10000 时只写
1700–3200 字符就收尾、省掉定量结果，所以提示词里额外加了"定量数据必须保留 +
长度下限"的要求。**换模型后重看一页**，形态不对就回去调提示词而不是调参数。

### 第二遍综合（`kb_link.R`）

`kb_compile` 逐条编译，每条 prompt 只见自己的源材料——所以产物 `links` 恒空，
跨源页无从产生，wiki 只是平铺目录。`kb_link.R` 补这一层：

```bash
Rscript R/kb_link.R                  # 四类跨源页 + 批量链接补全（全跑）
Rscript R/kb_link.R --entities-only  # pass B 实体页（跨 ≥2 页的具名对象）
Rscript R/kb_link.R --methods-only   # pass C 方法页（可复用技术，索引级概览）
Rscript R/kb_link.R --queries-only   # pass D 问题页（跨源问题的当前最佳答案）
Rscript R/kb_link.R --concepts-only  # pass E 概念页（跨 ≥3 页的抽象概念）
Rscript R/kb_link.R --links-only     # pass A 批量补 links/open_questions
Rscript R/kb_index.R                 # 必跑：新页不进 index 就是孤儿页
```

四类跨源页共用一套骨架（提案一次调用 → 逐条建页），id 带
`entity-`/`method-`/`query-`/`concept-` 前缀，`sources` 取所用页的 raw 来源
并集，`links` 确定性回填。提案按白名单过滤：`page_ids` 不在已编译页清单里的
一律丢弃，防悬挂链接。加第五类只需在注册表加一项，不必动主干。

**实体页 vs 概念页的分界**：实体页是"某个具名对象"，概念页是"多页共享的背景
框架"。后者综合价值更高但更容易与实体页重叠，所以门槛设成 ≥3 页（实体页 ≥2）。

**pass A 是批处理**：一批 ≤10 页一次调用，不是每页一次——API 调用量差一个
量级。`LINK_BATCH_MAX` 在 `R/kb_link.R` 顶部。**这个值反直觉地小，别按上下文
容量去估**：瓶颈是输出生成速度而不是输入长度。按上下文估会得出 150 页（1M
上下文只用 1/4），但实测 46 页一批直接超时（486 秒）；10 页/批稳定在 30–60 秒。
换更快的模型可以上调，**按超时实测调**。
**分批时每批共享完整全库清单、只输出本批页的 links**；若只喂本批页，模型看
不到全局，跨批链接会塌掉。每页只喂正文前 1000 字符——判断该不该链接靠主题
与对象，不靠细节，喂多了只是让批处理更容易超时。

`provider: stub` 时 `kb_link` **明确拒绝并以 0 退出**——跨源综合的本质是让模型
看多页材料后提出新页，占位符模拟不了这个判断，产出的会是无意义空壳页。

### 提交前

```bash
Rscript R/kb_lint.R && git add -A && git commit -m "..."
```

`kb_lint.R` 非零退出就不要提交。

## 4. lint 报错怎么修

| 报错 | 含义与修法 |
|---|---|
| `不在允许集合` | frontmatter 枚举值写错。照 `schema/*.json` 改 |
| `sources 指向不存在的 raw 记录` | wiki 页引用了已删除的源。删该 wiki 页或恢复源记录 |
| `links 指向不存在的 wiki 页` | 双链悬挂（warn）。补页或删链接 |
| `status=compiled 但没有任何 wiki 页引用它` | 状态在说谎。改回 `raw` 让它重编 |
| `value_gate=skip 但已被 wiki 页引用` | 闸门被绕过。删该 wiki 页，或把记录改回 `keep` |
| `正文已变更但 status 仍为 compiled` | 源改了。`kb_lint.R --fix` 自动标 `stale` |
| `id 重复` | 两条记录抢同一个 id。改一个（但 id 是引用锚点，改前先 grep 引用） |
| `文件名与 id 不一致` | 改文件名等于 id。Obsidian 双链靠文件名 |
| `含 CRLF 行尾` | Windows 侧编辑器写的。`kb_lint.R --fix` 或让 Obsidian 用 LF |
| `文件名仅大小写不同` | Windows 文件系统不区分大小写会互相覆盖。立刻改名 |
| `溯源引用指向不存在的证据页` | 正文「（来源：[[evidence-…]]）」目标不是已生成的证据页（臆造 id 会落到这里）。删该引注或重编该页 |
| `溯源引用指向不存在的 wiki 页` | 正文「（来源：[[页id]]）」目标不是已知 wiki 页。删该引注或重编该页 |
| `溯源引用缺少段落号` | 只有 evidence- 目标的引用才必须带 ¶N；引用 wiki 页整体时去掉 evidence- 前缀即可（免 ¶N 的合法形态）。旧形态页重编 |
| `溯源段号超出证据页锚点范围` | 模型臆造段号——链接可点但落到错误段落，比缺失溯源更糟。重编该页 |

## 5. 没配好 LLM 时先验证管线

设 `kb.config.yaml` 里 `compile.provider: stub`，然后正常跑 `kb_compile.R`。
它机械生成占位页，不调 LLM、不烧 token、不依赖服务，用来验证
闸门→schema→落盘→状态回写→lint→index 整条线是通的。
占位页 `confidence: low` 且正文带显式警告，不会被误当成真内容；
配好模型后重跑会覆盖它们。

## 6. 改 schema 要知道的事

`schema/raw_source.schema.json` 与 `schema/wiki_page.schema.json` **一份契约两处用**：
`kb_lint.R` 拿它校验，编译层拿它经 `ellmer::type_from_schema()` 约束 LLM 输出。
所以改 schema 会同时改变校验与生成两处行为——改完必跑：

```bash
Rscript tests/test_schema.R      # 校验器单元测试（50 项）
KB_TEMPLATE=<kb-template> bash tests/test_e2e.sh   # 端到端（122 项）
```

校验器是自己实现的 draft-07 子集（不依赖 V8/jsonvalidate，它们在受限环境装不上）。
**不支持 `$ref`/`oneOf`/`anyOf`/`allOf`——遇到会显式报错而不是静默通过。**
需要这些关键字就得先扩校验器。

## 7. 已知的坑（都踩过，别再踩）

- **推理型模型在 `json_object` 模式下仍会先输出 chain-of-thought 再写 JSON。**
  直接 `fromJSON(raw)` 必然失败，而报错信息（"unexpected character"）与真实
  原因毫无关系，很容易误判成提示词或 schema 的问题。`kb_llm_structured` 现在
  先 `sub("^[^{[]*", "", raw)` 从第一个 `{` 或 `[` 处截断再解析，截断后仍失败
  才走重试；对干净响应是空操作，顺带也解决 ```` ```json ```` 围栏包裹。
  **这是推理型模型的通用行为，不是某一家专有**——换模型别以为不用管。
  另注：DeepSeek 的 `response_format` 不支持 `json_schema`，只能用
  `json_object` + 客户端校验，所以这个剥离是必需的而非可选优化。

- **provider 的 API key 环境变量名各不相同，猜错的代价很高。**
  DeepSeek 只认 `DEEPSEEK_API_KEY`；若在 config 里写 `provider: openai_compatible`
  想接 DeepSeek，`ellmer` 会去读 `OPENAI_API_KEY` 拿到空值，报错与真实原因毫无
  关系。`kb_doctor.R` 现在按 config 的 provider 查对应变量、缺失时报 **fail**
  （不是 warn——缺 key 会让整轮编译白跑）。名字表是逐个扫 `asNamespace("ellmer")`
  的 `*_key()` 函数核实的，不是照文档抄；换 provider 时改那张表即可。
  接 DeepSeek 要写 `provider: deepseek` 而不是 `openai_compatible`。

- **模板里的提示词不能带任何具体领域的例子。**
  `kb_link.R` 的四类提案提示词原带具名领域例子（某个基因、某项技术、"同属本
  领域"这类判断语），用在别的学科会把模型往那个方向带偏——实测过。现在领域
  描述从 `kb.config.yaml` 的 `name` 注入（`kb_domain`），"候选类型"清单只描述
  形状，JSON 示例是纯占位符。改提示词时守住：**具体内容来自配置，代码里只留
  结构。**

- **`setNames(list(...), <length-1 名字>)` 会把名字向量循环补齐。**
  写成 `setNames(list(type="array", items=...), "entities")`，R 把名字补成
  `c("entities", NA)`，于是 `properties[[1]]` 变成裸字符串 `"array"`。必须写
  `setNames(list(list(type="array", ...)), "entities")`——用 `list(list(...))`
  把整个子 schema 包成单元素。
  **更隐蔽的一面**：无名项在 `properties` 层时，`intersect(names(...), ...)`
  会静默丢弃它，那个字段**永不被校验**——比崩溃更糟，schema 看着在用实则形同
  虚设。校验器现在两层都查，并指出会被跳过的项号。

- **测试里 `env -u VAR R ...` 会绕过 shell 函数。**
  `test_e2e.sh` 把 `R()` 定义为 shell 函数，`env` 只查可执行文件，于是找到系统
  的 `R` 并进交互模式、报 `--save` 缺失。清环境变量要用子 shell：
  `( unset VAR; R script.R )`。

- **扫「代码里有没有 X」时记得剔除注释行。**
  检查提示词是否残留领域词时，`grep` 命中了解释改动历史的 `##` 注释，误报一次。
  注释里出现领域词是正常的——它不进提示词。断言要先 `grep -vE "^\s*##"`。

- **`kb_compile.R` 编完会把记录标 `compiled`，而队列只收 `raw|stale`。**
  换 provider 或改提示词后直接重跑 → 队列为空、一条不编、退出码 0，
  看起来成功实则什么都没做。用 `kb_recompile.R` 复位。这是整套流程里
  最容易误判成"跑通了"的一处。
- **结构化输出撞 token 上限时，拿到的是截断 JSON，整条编译失败。**
  症状是 `chat_structured` 报解析错而不是"输出太长"，容易误查提示词。
  `ellmer` 的输出上限走 `ellmer::params(max_tokens=)` 传给 `chat_*(params=)`，
  不是 `chat_structured()` 的参数。
- **`Rscript -e '...' --args x` 里 `--args` 本身会进 `commandArgs(TRUE)`。**
  于是 `commandArgs(TRUE)[1]` 拿到的是字符串 `"--args"` 而不是 `x`。
  这与「`Rscript script.R --args x`」的行为不同。`-e` 形式直接写
  `Rscript -e '...' x`，不要加 `--args`。
- **help 文本里写了的 flag，代码必须真的检查。** `kb_recompile.R` 最初
  `--all` 只存在于 help 里，代码从不读它 —— 拼错成 `--al` 时静默处理 0 条
  并正常退出，你以为复位过了，接着 `kb_compile.R` 报"队列为空"，
  两次误导叠加极难定位。**任何入口脚本都要有未知参数 → 报错退出的校验。**
- **checksum 必须对字节哈希。** `digest::digest(<character>)` 走 `serialize()`，
  结果含 encoding 标记；同一份 UTF-8 内容，新建字符串标记是 `unknown`、
  从文件读回是 `UTF-8`，哈希不等 → 中文库里每条记录开箱即报漂移。
  实现已是 `charToRaw(enc2utf8(normalize(body)))` + `serialize = FALSE`，不要退回去。
- **退化 checksum 必须对位置敏感。** 无 `digest` 时的兜底实现曾用「长度+字节和」，
  它对任意字符换序都碰撞：`钾通道` 与 `通钾道` 同哈希。而**换序正是中文正文
  最常见的真实修改**，等于漂移检测在最需要它时静默失效。现已改为双参数多项式
  滚动哈希（模数 < 2^31、乘子小，`h*M < 2^36` 在 double 内精确无误差）。
  这个缺陷能活到交付，是因为原有 checksum 测试全部走 `digest` 在场的路径。
- **判断"是否 kb-template 模板目录"只能用 `templates/*.tpl`。** 别用
  `R/kb_init.R`——它会被复制进每个生成的库，用它当判据会让**真库里缺
  `kb.config.yaml` 的真故障被误判成"这是模板目录"而放过**。
  模板目录里跑 `kb_doctor.R` 查依赖是正常用法，此时无配置应为 warn 而非 fail。
- **`set -u` 下引用 `R_LIBS` 必须给默认值。** 测试脚本开了 `set -u`，而用户
  默认环境通常不设 `R_LIBS` → 未绑定变量直接中止。回退链：
  `R_LIBS` → `R_LIBS_USER` → `.libPaths()[1]`（永远存在）。
  这类 bug 专门在「用户什么都没配」的最常见场景触发，沙箱里设了变量反而测不出。
- **单元素向量会被 YAML 写成标量。** `tags: demo` 而非 `tags:\n  - demo`，
  Obsidian tag 面板与按行 grep 都会静默失效。`kb_write_fm` 已强制
  `KB_ARRAY_FIELDS` 成 list。新增数组字段要加进那个常量。
- **id 允许中文。** schema 的 id 模式含 CJK 范围——中文标题是常态，音译或哈希
  会让 id 失去可读性。但不允许空格与全角标点。
- **R 拒绝从可写目录加载编译过的包。** 报 `Refusing to dyn.load` 时
  `chmod -R a-w <libdir>`。`kb_doctor.R` 会检查这一项并打印命令。
- **RSS 排在最后，默认不启用。** feed 只给摘要不给全文，`parse_quality` 恒为
  `partial`；更重要的是它是无限流，会让库以你判定不过来的速度膨胀，
  把价值闸门变成摆设。先把手工/论文源跑顺，确认判定节奏跟得上再考虑开。
- **不要双向同步 markdown。** LLM 高频改写 + 同步工具 = 冲突地狱。
  单向：采集端产出 → 库（git）→ Obsidian 只读渲染。

### 并行编译与「同一份逻辑的多份副本」

- **段落编号判据必须两端共用一份。** wiki 的 `¶N` 与证据页的 `^pN` 靠位置对应，
  两端各写一份判据时必然漂移——实测过一次：证据页那份多了「表格分隔行不编号」，
  于是含 markdown 表格的材料从第一个表格起全部锚点错开一位并逐表累积。
  **失效方式是最坏的一种**：链接照样可点、lint 照样通过、不报任何错，读者点过去
  看到的是邻近但错误的段落——比没有溯源更糟，因为读者会相信这个出处。
  现由 `lib/compile_core.R` 的 `kb_para_citable` + `kb_number_paragraphs` 两端共用，
  标记方式用 `mark_fun` 参数化（编译端前缀 `[¶N]`，证据页后缀 `^pN`——Obsidian
  的块锚点只在段末生效）。**新增任何消费段号的脚本，一律调这两个函数。**

- **预处理链的嵌套顺序不能错：`rcs_summarize(annotate(clip(body)))`。**
  先按长度截断，再打段号，最后分块摘要。若先打段号后截断，被截掉的段落也占了
  段号，与证据页对不上；而 RCS 摘要要求保留段号，所以它必须在最外层。
  证据页刻意**不做长度截断**（与编译端唯一的有意分歧）：截断会让后半部分的
  溯源引用失去落点。

- **并行 worker 与串行路径必须调同一个函数。** 手工把编译逻辑复制进 `mirai` 块
  是最自然的写法，也是提示词漂移的直接来源。实测遇到过三份副本共存：串行版、
  worker 版、mirai 内联版，措辞各不相同，其中内联那份丢了 body 字数下限。
  **它只在 `concurrency > 1` 时生效**——为提速调高并发就会悄悄编出更短的页，
  而你会以为是模型或材料的问题。且三份里有一份是**死代码**（零调用点），
  死代码的真正危害是掩盖真相：你改的那份不生效，生效的在别处。
  正确做法：逻辑抽进 `lib/compile_core.R`，两条路径都 source 它。

- **`mirai` daemon 是独立进程，`source` 本脚本有两个必修的坑。**
  1. **`quit()` 会杀掉 daemon 进程本身**，不是「返回」。而脚本顶部通常有
     「队列为空 → `quit(0)`」——worker 里队列**必然**为空（父进程已把该批标成
     `compiled`），于是并行任务无声失败。用 `KB_WORKER` 环境变量把整个队列段
     包进 `if (!KB_WORKER_MODE) { ... }`，不要用 `quit()` 跳过。
     顺带也别让 worker 重跑队列扫描与「编译计划」打印——N 份日志交错没法读。
  2. **daemon 里 `commandArgs()` 没有 `--file=`**，靠它自定位的脚本会把
     `KB_R` 解析到错误目录，`source(lib/*)` 全数失败、报「无法打开链结」。
     父进程用 `KB_WORKER_ROOT` 显式传库根，自定位失败时退回它。
     worker 也不该解析父进程的命令行参数：`args <- if (KB_WORKER_MODE)
     character(0) else commandArgs(TRUE)`。
  3. 守卫要留出 worker 也需要的变量。`provider` 既被 worker 用、也被守卫内的
     「编译计划」打印用，放错一侧会让 stub 编译整块失败——移动它时两处都要跑。

- **`concurrency` 默认留 1。** 先串行跑通一篇、确认页面质量，再并行。并行下多条
  同时失败、日志交错，排查成本高得多。另外 `max_tokens_per_run` 的中途停止在
  并行路径上没有意义（任务已全部派发），要限量得用 `--limit`。

- **并行路径的验证状态：只做过组件级验证，没有端到端跑通过。** 诚实记录，
  以免下次误以为它已经过实战检验：
  - **已验证**：`KB_WORKER=1` + `KB_WORKER_ROOT` 模拟 daemon 环境下，脚本能被
    `source` 且不自杀、`compile_core.R` 的函数全部就位；调度分支能正确进入
    「并行编译 N 条（M workers）」。
  - **未验证**：真正多进程跑完一轮。`mirai` 在受限沙箱里起不了 daemon
    （默认 IPC socket 报 `Permission denied`，改 `tcp://127.0.0.1:0` 则父子
    连不上、`call_mirai` 无限挂起）。**首次在真机上开并行，先用 2 条材料试。**
  - 顺带一个会浪费时间的坑：`provider: stub` 被代码强制 `nc <- 1L`（stub 不发
    请求，多开进程无意义）。**用 stub 测不到并行路径**——我用它「测」过一次
    并行，4 条全绿，其实走的是串行，什么都没验证到。要测并行得用真 provider，
    或起一个本地 OpenAI 兼容的假服务顶上。

- **并行不该是单点故障：daemon 起不来必须退回串行。** 原代码 `mirai::daemons()`
  裸调，起不来就 `停止执行`,整批一条都编不出来。容器、受限 IPC、端口占用都会
  触发。两种失败模式要分开防：
  - **启动失败**——`try()` 捕获后退回串行。隔离了 IPC 命名空间的容器里,mirai
    默认的进程间 socket 会被拒（实测报 `Permission denied`）。
  - **起得来但连不通**——发一个探针任务限时等待（`daemon_probe_s`,默认 30s）。
    **这种比崩溃更糟**:没有探针时 `call_mirai()` 无限挂起,连个可归因的错误
    都没有,只能看着它卡住。想用 `tcp://127.0.0.1:0` 绕开 IPC 限制时正会撞上。

- **脚手架的默认值要按「什么都不配的人」来定,不是按你自己的用法。**
  库里 `concurrency` 默认曾是 4 —— 意味着任何人拿到库、什么都不配就直接吃
  并行路径,而那条路径当时还没端到端跑通过。默认值改 1,要提速的人自己去配。
  同类默认值：RSS 默认不启用、`rcs` 只在超长材料上触发。

- **断言写行为，不要绑实现。** 「空队列不杀 daemon」这条最初写成
  `grep 'nrow(queue) && !KB_WORKER_MODE'`，后来实现改成「整段包在守卫块里」
  （更彻底），断言就误报了。改成用 `awk` 追踪守卫块深度、检查 `quit` 是否落在
  块内——同一个行为，不同实现都能过。

## 8. 改动脚手架后的验收清单

每次改 `kb-template` 的脚本或 schema，按这个顺序过一遍。顺序是有讲究的：
前两步在开发环境跑，第 3 步必须在**用户真机**跑——沙箱与真机的 R 版本、
包版本、环境变量都不同，而差异恰好落在最容易出 bug 的地方。

1. **两套测试全绿**（开发环境）
   ```bash
   cd <kb-template>
   Rscript tests/test_schema.R                 # 契约与 checksum 单元测试
   KB_TEMPLATE=$PWD bash tests/test_e2e.sh     # 建库→采集→编译→lint 全链
   ```
2. **降级分支必须单独测。** 这是最容易漏的一条。凡是写了
   `if (requireNamespace(...)) 用好的 else 退化` 的地方，测试若只在包在场时跑，
   退化分支等于从未被测——退化 checksum 的换序碰撞就是这么活到交付的。
   为每个退化实现写独立用例，不要依赖"包缺失"这个偶然条件去触发它。
3. **在用户真机跑一遍 `kb_doctor.R` + 两套测试。** 真机会暴露开发环境掩盖的问题：
   - 未设置的环境变量（`set -u` 下直接中止）
   - 比开发环境旧的包版本（查函数是否存在、形参是否一致，再决定要不要升级）
   - 尚不存在的用户库目录、缺失的系统开发头文件
4. **审契约一致性。** 同一件事在多处声明时，逐项对照是否一致：
   - `kb_setup.R` 的 `REQUIRED`/`OPTIONAL` vs `kb_doctor.R` 的包清单定性
   - `schema/*.json` vs `kb_lint.R` 的校验分支 vs `kb_compile.R` 传给
     `type_from_schema()` 的路径（同一份 schema 三处用，不能各说各话）
   - 文档里的包清单 vs 源码里**实际** `library()/requireNamespace()/::` 的引用。
     别凭记忆列——曾据此发现文档列的 6 个包源码根本没用到。用**单引号**包裹
     这条（双引号会让 shell 吃掉转义，把包名截断成 `requireNamespace(p`）：
     ```bash
     grep -rhoE '(library|requireNamespace)\("?[A-Za-z0-9.]+|[A-Za-z0-9.]+::' R/ \
       | sed -E 's/.*\("?//; s/::$//' | sort -u
     ```
     结果应只剩必需 5 个 + base（`graphics` `grDevices` `tools` `utils`）+
     形参名 `p`（来自 `requireNamespace(p, ...)`，不是包名）。
5. **每修一个 bug，补一条回归测试。** 修完重跑第 1 步确认没有连带破坏。

## 9. 与 `paper2knowledge` skill 的分工

`paper2knowledge` 负责**单篇 PDF → 结构化提取**（MinerU / OCR 双引擎、元数据校验、
补充材料分离、IMA 上传）。kb-ops 站在它上层：管多库、多源、编译成 wiki、契约校验。

paper adapter 直接委托它的 `process_paper.py`，**不在 R 里重写 PDF 解析**——
那套双引擎已经跑通且校验过，重写只会失去它的解析质量。
`kb.config.yaml` 的 `paper_pipeline.script` 指向该脚本，`kb_doctor.R` 会检查路径是否真实存在。

## 10. 脚本清单

| 脚本 | 作用 | 调 LLM |
|---|---|---|
| `kb_setup.R` | 装 R 依赖（新机器第一条命令） | 否 |
| `kb_init.R` | 建新库 | 否 |
| `kb_ingest.R` | 采集 → `raw/` | 否 |
| `kb_compile.R` | `raw/` → `wiki/`（第一遍，逐条） | **是** |
| `kb_link.R` | 四类跨源页 + 批量 `links` 补全（第二遍） | **是** |
| `kb_recompile.R` | `compiled` → `raw` 复位，删旧页 | 否 |
| `kb_index.R` | 重建 `wiki/index.md` | 否 |
| `kb_lint.R` | 契约校验（7 类检查） | 否 |
| `kb_status.R` | 状态看板 | 否 |
| `kb_doctor.R` | 依赖、外部服务、**云端 provider 的 API key** 健康检查 | 否 |

分工原则：**能用规则判定的一律脚本判定，LLM 只做语义综合。**
index、校验、状态、id 生成全是确定性的——交给 LLM 只会引入漂移并烧钱。

## 接新语料时必查：同篇重复

真实语料里同一篇论文常被解析两次（规范命名 + 出版商文件名）。实测
Immunopeptide 42 条解析目录实为 21 篇（完整双份），AMP 54 条实为 27 篇。

**上游三道检查全部拦不住**，所以采集后必须自己查：

- checksum 去重失效——两次解析批次不同，正文有细微差异，md5 不等
- id 去重失效——命名不同，id 自然不撞
- 落盘的重复检查只看 id，同样放行

查法：按归一化标题统计重复组，别信 checksum。

    for f in raw/mineru/*.md; do grep -m1 '^title:' $f; done | sort | uniq -d | wc -l

去重的保留优先级必须是**全序**（元数据完整 > 正文长 > 目录名字典序）。
少了末位那个纯确定性键，同一语料重采会选到不同份，库不可复现。

## 归一化标题的三个坑（实测踩到，非推演）

- `[^a-z0-9 ]` 会把西里尔/中文标题整体抹成空串 → 重复漏检，且 id 退化成
  只剩 topic 前缀。用 `[[:punct:]]` 只归一化标点。
- MinerU 会把 β 解析成 U+0001（控制字符），另一份解析里 β 直接丢失 →
  两键不等。`[[:punct:]]` 不匹配控制字符，必须单独剥 `[[:cntrl:]]`。
- OCR 会把作者名/刊头黏在标题尾部 → 需要前缀合并。只认**前缀**不认子串
  （子串会把 "AMP review" 并进 "AMP review of methods"），且被包含的键
  要求 >= 30 字符。

## 元数据：宁可留空，不要猜

目录名不是 `<Author><Year>_` 形态时，**绝不能**把首段当作者——会产出
`authors: ["mmc7"]`、`authors: ["41467"]`，进 frontmatter 与 wiki 溯源后
页面上会写"据 mmc7 等"，是会静默产出错误引用的一类缺陷。

三类命名惯例要分开判定，否则会丢掉本可靠的信息：

- `<Author><Year>_<Journal>_<Title>` → 作者+年份都可靠
- `<YYYY|YYYYMM>_<Journal>_<Title>` → **年份可靠**、无作者（AMP 语料 18 篇属此类，
  合并判定会把这些年份一起扔掉）
- 出版商文件名 → 两者都不可靠，留空 + 写 error 说明

从正文抽作者/年份不可行（实测 7 篇里仅 2 篇有 Authors 段；年份混着参考文献
年份，有一篇前 6k 出现 2004–2016 六个年份）。DOI 路子也不行（抽到的含被引
文献 DOI 与截断值，覆盖率仅 24/42、36/54）。

## kb_make_id 改字符集要先跑既有 id 回归

它是全库共用函数。改动前先断言既有 id 逐字不变——`tests/test_mineru_adapter.R`
里有现成的。两个已知约束：

- 拉丁变音符必须**折成 ASCII**而非保留：既有库的 id 就是折过的
  （`amp-kosciuczuk-...`），保留会改变既有 id；且 id 会进文件名，变音符
  文件名在 Windows/WSL + git 上易出问题。
- 不能全局跑 `iconv("ASCII//TRANSLIT")` 来折——它会把西里尔与中文一并删空
  （实测），id 又退化成纯 topic。要按码点范围定向 `chartr`。

## value_gate 是会被跳过的那一步

新采的记录一律 `undecided`，而编译队列只收 `keep`——所以采集后
`kb_compile.R` 报「队列为空并正常退出」是**设计使然，不是故障**。
第一次遇到会以为编译坏了。

判定本身是领域判断，不能代劳；但摩擦要降到人做得动，否则会被整体跳过，
无关论文就进了库。用 `R/kb_gate.R`：

    Rscript R/kb_gate.R --list                 # 当前状态
    Rscript R/kb_gate.R --all keep             # 全收
    Rscript R/kb_gate.R --grep <正则> skip     # 按标题/id 批量排除
    Rscript R/kb_gate.R --from-csv sel.csv     # 从 csv 写回（列：id, value_gate）

csv 入口配合导出清单最好用：清单里带 title / year / 正文长度 / 摘要片段，
在表格里过一遍填 value_gate 列再写回。

改 value_gate 时**同值不要重写**：写盘会动 mtime，增量编译按 mtime 判 stale，
无谓改动会触发整库重编译（真金白银的 API 调用）。`kb_gate.R` 已经处理了。

## 写测试时的三个环境陷阱（都实测踩过）

- **临时夹具别放 `/tmp`**：某些沙箱会在命令之间清空它。后果很隐蔽——
  「误用防线全部通过」其实是「找不到 csv」的误报，五条防线里三条根本没跑到。
  夹具放仓库内的临时目录（记得加进 .gitignore 或用完即删）。
- **`quit()` 不触发 `on.exit`**：R 里用 `quit(status=)` 结束的测试，沙箱目录
  会残留在仓库里。要在 `quit()` 前显式清理，且清理语句必须在成功/失败两条
  路径共用的位置。另外 cwd 还在沙箱里时 `unlink` 删不掉它，先 `setwd` 回去。
- **子进程不继承 `.libPaths()`**：`system2("Rscript", ...)` 要显式传
  `env = paste0("R_LIBS=", paste(.libPaths(), collapse=":"))`，否则子进程
  报「缺少必需的 R 包」，看着像环境没装好。

还有一条与 R 语法有关：脚本里顶层的裸表达式会被自动 print，所以
`run(...)`、`file.copy(...)` 这类调用要包 `invisible()`，否则测试输出里
混满子进程回显，真正的 ok/FAIL 被淹没。

## 挂新测试进 e2e 后要做反向验证

`>/dev/null 2>&1` + `check 0 $?` 的写法，在脚本路径写错或文件不存在时
同样会「通过」。挂上之后故意让新测试失败一次，确认 e2e 真的报 FAIL。
（顺带：做这种破坏性验证前先备份，且核实备份真的写成了——用 `cp a /tmp_x ||
cp a ../x` 这种写法，前一条意外成功后备份就落在了预期外的位置。）

## kb_init 记得带 --git

`.gitattributes` 里 `*.md text eol=lf` 是 WSL + Windows Obsidian 混写库的关键，
缺了它一旦在 Windows 侧编辑 md，CRLF 就进提交历史。模板已改为无条件写这两个
文件，但用旧版模板建的库要手工补。
