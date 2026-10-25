# DeerFlow 架构笔记

> 基线 commit:`3fdd9bd`(2026-10-24)。代码约 18.8 万行 Python,不必通读,按需深入。
> 路径均相对 `deer-flow/backend/packages/harness/deerflow/`(简称 `harness/`)。

## 1. 服务拓扑

```
浏览器 → Nginx :2026 ─┬─ /api/*  → Gateway :8001 (FastAPI + 内嵌 LangGraph 运行时)
                      └─ 其余    → Frontend :3000 (Next.js)
```

- 代理 `/api/langgraph/*` 会被改写为 Gateway 的原生路由,所以没有独立的 LangGraph Server。
- 浏览器入口是 `http://localhost:2026`。

## 2. 代码分层

| 层 | 路径 | 说明 |
|---|---|---|
| **harness** | `backend/packages/harness/deerflow/` | 可发布的 Agent 框架,import 前缀 `deerflow.*` |
| **app** | `backend/app/` | Gateway 与 IM 渠道(飞书/Slack 等),import 前缀 `app.*` |
| **extension-api** | `backend/packages/extension-api/` | 扩展的公开契约 |
| **skills** | `skills/public/` | 以 `SKILL.md` 为单位的工作流说明,23 个 |
| **examples** | `examples/` | 扩展示例 |

**硬规则**:app 可以 import harness,反过来不行(`tests/test_harness_boundary.py` 在 CI 里强制检查)。

## 3. harness 关键模块

| 模块 | 内容 |
|---|---|
| `agents/lead_agent/agent.py` | 主 Agent 组装,`build_middlewares()` 决定中间件链 |
| `agents/lead_agent/prompt.py` | 系统提示词(1285 行) |
| `agents/middlewares/` | 约 50 个中间件,是可靠性逻辑的集中地 |
| `subagents/` | 子 Agent:`executor.py`(执行)、`registry.py`(注册)、`builtins/` |
| `tools/builtins/task_tool.py` | 主 Agent 派发子任务的入口 |
| `skills/` | skill 的加载与激活 |
| `community/` | 搜索 / 抓取 / 沙箱的各家适配(tavily、firecrawl、e2b 等) |
| `mcp/` | MCP 集成,含持久化任务运行时 |

## 4. 中间件链(决定 Agent 行为的核心)

按注册顺序(详见 `build_middlewares()`):

1. **上下文注入**:日期、记忆注入首条 HumanMessage,保持系统提示词静态以复用前缀缓存
2. **Skill 激活**:用户以 `/skill-name` 开头时,确定性加载整个 SKILL.md
3. **durable context**:在摘要压缩之前,先捕获已完成的委派和已加载的 skill
4. **Summarization**:接近 token 上限时自动摘要
5. **Todo**:plan mode 下提供 `write_todos`
6. **Token 用量 / Title / Memory / ViewImage**
7. **Deferred tool filter**:MCP 工具 schema 在 `tool_search` 提升前不暴露给模型
8. **SubagentLimit**:截断超出并发上限的并行 `task` 调用
9. **LoopDetection**:检测并打断重复的工具调用循环
10. **TokenBudget**:每次运行的 token 上限
11. **ModelContentCompatibility / TerminalResponse / ModelLengthFinishReason**:兜底与兼容

可靠性相关的现成组件:`loop_detection`、`token_budget`、`tool_error_handling`、`llm_error_handling`、`tool_result_sanitization`、`receipt_verification`。**做优化前先看这些,避免重复造轮子。**

## 5. 子 Agent

- 内置两种:`general-purpose`、`bash`(`subagents/builtins/`)。
- 并发上限 `MAX_CONCURRENT_SUBAGENTS = 3`(`systematic-literature-review/SKILL.md` 里写明超出会被静默丢弃)。
- 子 Agent 不能再派发子 Agent(提示词中明确禁用 `task`)。
- 结果以字符串返回,带 `Task Succeeded. Result:` 之类的前缀,调用方要自己剥前缀再解析。

## 6. 与「论文调研」场景直接相关的现有 skill

| skill | 能力 | 局限(可能的增量点) |
|---|---|---|
| `systematic-literature-review` | arXiv 检索 → 子 Agent 并行抽取元数据 → 综合 → APA/IEEE/BibTeX 报告 | 只用 arXiv;只基于摘要抽取,没读全文;无引用核查;检索只跑一次不重试 |
| `academic-paper-review` | 单篇论文深度评审 | 未细读 |
| `deep-research` | 通用深度研究 | 未细读 |

这个 skill 自带 `evals/evals.json`(5 条)和 `trigger_eval_set.json`(20 条)。
它是**规则式 checklist**(检查有没有调用某个工具、报告里有没有某个章节),不衡量**内容质量**(引用是否真实、综合是否准确)。**这正是评测方向 A 的空位。**

## 7. 增量点候选(待验证)

1. **引用核查**:对报告中每条论文引用,用 arXiv API 核实标题、作者、日期是否真实存在,计算引用准确率。可量化,且小白可做。
2. **全文抽取**:现在只读摘要;可对高相关论文抓取 PDF 做更深抽取,对比质量差异。
3. **多源检索**:接入 Semantic Scholar 等(SKILL.md 说明这应做成 MCP server,刚好练 MCP)。
4. **内容质量评测**:LLM-as-judge + 引用核查,建立 30~50 条调研任务的基准。
5. **成本优化**:子 Agent 改用 `qwen-flash`,对比质量与 token 成本。

## 8. 扩展机制

仓库的 AGENTS.md 要求「先评估能否做成扩展,再考虑改核心代码」:
- 扩展通过 `config.yaml -> plugins:` 加载,可贡献中间件、路由、生命周期钩子。
- 示例:`examples/deerflow-extension-{example,bookmarks,agent-teams}`。
- **含义**:我们的二开应优先做成 skill + 扩展,少动核心。这样更干净,也更容易向上游提 PR。

## 9. 待读清单

- [ ] `agents/lead_agent/prompt.py`:主 Agent 如何被引导
- [ ] `subagents/executor.py` 与 `task_tool.py`:一次委派的完整生命周期
- [ ] `skills/public/deep-research/SKILL.md`、`academic-paper-review/SKILL.md`
- [ ] `docs/summarization.md`、`backend/docs/ARCHITECTURE.md`
- [ ] 一次真实运行的 trace(跑通后用文献综述任务观察)

## 10. 工具输出外置机制(影响可靠性,务必了解)

- `config.yaml -> tool_output`:单个工具输出超过 `externalize_min_chars`(默认 12000)时,完整内容存到 `/mnt/user-data/outputs/.tool-results/*.log`,模型只收到**结构摘要 + 首尾片段**。`read_file` 豁免,模型可以主动读回原文。
- 风险:模型若不去读原文,会基于摘要里没有的内容继续推进,并可能**编造**。baseline-03 中 10 篇论文只露出 1 篇,其余 9 篇被编造(见 BASELINE.md)。
- 相关代码:`agents/middlewares/tool_output_budget_middleware.py`、`tool_output_synopsis.py`、`TOOL_OUTPUT_PERSISTENCE.md`。
