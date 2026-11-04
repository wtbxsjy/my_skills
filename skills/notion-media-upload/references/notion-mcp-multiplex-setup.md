# Notion MCP 多工作空间接入与 DSH 配置

本环境里 Notion MCP 不是"每个工作空间一个 server"，而是 **1 个多路复用 server + 5 个工具**，
统一接入 4 个工作空间（cuhk / hotmail / bgi / polyu）。本文记录这套东西的结构、配置与重建步骤，
也是 `notion_upload.py` 能用 `--workspace <label>` 切换空间的原因——两者读同一个 token 文件。

## 1. 为什么不是 4 个官方 server

官方 `@notionhq/notion-mcp-server` 每个工作空间暴露 **24 个工具**；4 个空间 = **96 个工具**，
JSON schema 约 **300 KB**，每次会话/请求都要带。实测这会明显拖慢并占用上下文。

多路复用方案：自研一个 stdio server，暴露 5 个精炼工具，每个工具带 `workspace` 参数，
内部用对应 token 打同一套官方 REST API。schema 小一个数量级，工具名固定为
`mcp__notion__search` / `mcp__notion__read_page` / `mcp__notion__create_page` /
`mcp__notion__update_page_markdown` / `mcp__notion__api`。

## 2. 文件位置

```
~/.dsh/notion.tokens                         # 每行 "<label> <token>"，权限 600；绝不提交/打印
~/.dsh/notion-multiplex/
  ├── run.sh                                 # 启动器：node server.mjs
  ├── server.mjs                             # 自研 MCP server（stdio JSON-RPC，零依赖）
  ├── probe.mjs                              # 端到端探针：握手/schema/读路径/写校验
  └── node_modules/                          # 仅 probe 需要的 @modelcontextprotocol/client
~/.dsh/notion-mcp/
  ├── run-notion-mcp.sh <label>              # 官方 server 包装（每空间一个，默认 disabled，供回滚）
  ├── node_modules/@notionhq/notion-mcp-server   # v2.6.1
  └── package.json
~/.dsh/profiles/web/cordis.patch.yml         # DSH 的 MCP 配置（insert 块）
```

回滚备份：`~/.dsh/profiles/web/cordis.patch.yml.bak-notion-mux-20261104-113105`
（多路复用上线前的原始配置，含 4 个独立 server）。

## 3. server.mjs 设计要点

- **协议**：MCP over stdio，换行分隔 JSON-RPC 2.0；单文件、零运行时依赖。
- **token**：启动时读一次 `~/.dsh/notion.tokens` → `Map<label, token>`；`label` 就是各工具的
  `workspace` 参数。token 不出现在输出、错误或日志里。
- **API**：`https://api.notion.com`，`Notion-Version: 2025-09-03`；
  `read_page` 的 markdown 走 `GET /v1/pages/{id}/markdown`（`Notion-Version: 2026-03-11`，
  Notion 的 markdown 接口），默认截断 60k 字符；`format=blocks` 回退块树；
  `update_page_markdown` 走 `PATCH /v1/pages/{id}/markdown`。
- **容错**：429 自动重试一次（Retry-After ≤ 10 s）；单请求 45 s 超时；错误统一转成
  `UserError` 文本（例如 `unknown workspace "xxx"; available: cuhk, hotmail, bgi, polyu`）。
- **工具**：`search`（可跨 workspace 一次查全部）、`read_page`、`create_page`、
  `update_page_markdown`、`api`（REST 逃生舱，path 必须 `/v1/` 开头）。

## 4. DSH 配置

在 **当前 profile** 的 `cordis.patch.yml`（本机为 `~/.dsh/profiles/web/cordis.patch.yml`）
里加一个 `insert` 块：

```yaml
# ── Notion MCP（多路复用）：1 个 server + 5 个工具，服务全部工作空间 ──
- insert:
    - id: mcp-notion
      name: "@deepseek-ai/dsh-mcp-client"
      config:
        serverName: notion
        transport: stdio
        command: /bin/bash
        args:
          - /home/renzhe/.dsh/notion-multiplex/run.sh
        cwd: /home/renzhe/.dsh/notion-multiplex
        toolCallTimeoutMs: 120000
```

工具名前缀由 `serverName` 决定（`notion` → `mcp__notion__*`）。

**回滚用**（保留在同一个 insert 块里，默认禁用）：

```yaml
    - id: mcp-notion-hotmail
      name: "@deepseek-ai/dsh-mcp-client"
      disabled: true
      config:
        serverName: notion-hotmail
        transport: stdio
        command: /bin/bash
        args: [/home/renzhe/.dsh/notion-mcp/run-notion-mcp.sh, hotmail]
        cwd: /home/renzhe/.dsh/notion-mcp
        toolCallTimeoutMs: 60000
```

cuhk / bgi / polyu 三项同构，只换 `id`、`serverName`、参数标签。把 `disabled` 去掉即可回到
"每空间一个官方 server"（工具数 96、schema ≈300 KB）。

**生效方式**：改完 YAML 需要重启 DSH 客户端/新开会话，MCP 连接在会话建立时创建。

## 5. 从零重建

1. 写 token 文件：每行 `label token`，`chmod 600 ~/.dsh/notion.tokens`；不要放进 git。
2. `mkdir -p ~/.dsh/notion-multiplex`，放入 `server.mjs`、`run.sh`、`probe.mjs`。
3. 在 profile 的 `cordis.patch.yml` 加第 4 节的 insert 块（回滚项可选）。
4. 重启 DSH；验证：
   - `node ~/.dsh/notion-multiplex/probe.mjs`（握手 + schema + 搜索/读页/写校验）
   - 或 `python3 scripts/check_workspaces.py`（逐 label 调 `/v1/users/me`，见下）
5. 新增工作空间：token 文件加一行 → 重启（server 启动时读取）→ 直接可用 `workspace` 参数。

## 6. 验证与排错

`scripts/check_workspaces.py` 会对 token 文件里每个 label 调一次 `/v1/users/me`，打印
`label → workspace_name / bot / upload_limit`，并检查 token 文件权限：

```bash
python3 ~/my_skills/skills/notion-media-upload/scripts/check_workspaces.py
# cuhk     workspace=Zhe Ren' Plus workspace  bot=dsh  upload_limit=5368709120
# hotmail  workspace=wtbxsjy_self              bot=dsh  upload_limit=5242880
# bgi      workspace=BGI-Shenzhen              bot=dsh  upload_limit=5242880
# polyu    workspace=Zhe Ren的 Notion           bot=dsh  upload_limit=5242880
```

注意 **上传上限按工作空间不同**：cuhk 是 5 GiB，其余 5 MiB。上传前用
`notion_upload.py limits --workspace <label>` 查，不要写死。

常见错误：

| 现象 | 原因 |
|---|---|
| `unknown workspace "xxx"` | label 拼错，或 token 文件里没有该行 |
| `HTTP 401` | token 失效/被重置 |
| `404 object_not_found` | 页面没有分享给该集成（页面 `⋯` → `Connections`） |
| `400 validation_error ... workspace-level ...` | 内部集成**不能**创建工作区顶层私有页；顶层页需人工创建，或改用带 `insert_content` 的 public integration |
| 上传本地文件失败 | MCP 只发 JSON，multipart 走 `scripts/notion_upload.py`（见主 SKILL.md） |

## 7. 两条通道的分工

| 需求 | 通道 |
|---|---|
| 搜索、读页面 markdown/块、建页、改正文、任意 JSON REST | MCP（`mcp__notion__*`，带 `workspace`） |
| 插入本地图片/PDF（multipart 上传） | `scripts/notion_upload.py`（同一 token 文件、同一 label 语义） |

两个通道共用 `~/.dsh/notion.tokens`，所以 `--workspace` 与 MCP 的 `workspace` 参数取值完全一致。
