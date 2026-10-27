# deerflow-extension-scholar

DeerFlow 插件，给 `systematic-literature-review` skill 提供检索、筛选工具和引用核查关卡。只依赖公开的 `deerflow-extension-api`，不改 DeerFlow 核心。

| 贡献 | 作用 |
|---|---|
| `search` 工具 | 在 Gateway 进程内查 arXiv，取约 50 篇候选；再查这些候选的参考文献(Semantic Scholar)，把窗口内、同类别的论文补进来；按「被多少篇候选引用」排序，取前 3N 篇(最多 100 篇)入围。日期窗口、主类别由代码过滤，结果按线程保存，只返回计数。**不需要 `allow_host_bash`** |
| `screen` 工具 | 模型按标题和摘要给入围论文打 0~3 分(与主题的相关程度)，**由代码选出** N 篇：2~3 分的优先，其次 1 分，0 分不选，同档内按被引用次数排序。返回入选论文的紧凑索引、批次号和 PRISMA 式计数；完整筛选表(分数、理由、来源)存进 `search.json` |
| `get_batch` 工具 | 子 Agent 按批次号直接取入选论文的数据，模型不再转述。筛选之前拒绝取数。每批不超过 9,000 字符，不会触发宿主的输出外置(12,000) |
| `CitationGateMiddleware` | `present_files` 交付 `.md` 报告后，在模型看到结果前用代码核对：报告里每个 arXiv 编号都必须出自本线程的检索。不通过就把交付结果改写成"被拒绝 + 原因"，最多拒绝 `max_blocks` 次，之后要求模型向用户明确说明 |
| 类别检查(同一中间件) | 用户写了类别(如 `cs.CL`)而检索没用它，就把检索结果换成报错，并作废这次检索：`get_batch` 拒绝取数，基于它写的报告也通不过关卡 |
| 代为交付(同一中间件，`after_model`) | 模型保存了带 arXiv 编号的报告、却不调 `present_files` 就要结束时，由关卡代为调用，报告照样要经过核查。每次检索最多代交一次 |

## 检索为什么这样设计(P2)

v3.1 只做一次 arXiv 相关度检索，取回几篇就引几篇，覆盖率开发集上同一主题两次的命中数完全相同。离线摸底(开发集 8 题，每题选 10 篇，脚本在 `eval/*_probe.py`)：

| 选法 | 命中综述参考文献 |
|---|---|
| arXiv 相关度前 10(v3.1) | 10 |
| 前 50 篇由模型打分后取前 10 | 11 |
| 按被引数排序(OpenAlex) | 7~9，且带后见之明，不用 |
| 候选池 + 参考文献，按共同引用次数排序 | 19 |
| **上一行 + 模型去掉跑题论文(现在的做法)** | **21** |
| 4 个查询(模型拆分)+ 共同引用 + 筛选 | 20(没有提升，不做多查询) |

只看引用不看主题，会选进大家都引的通用论文(基础模型技术报告、RL 算法)，模型筛选就是去掉这些。

**不泄漏的约束**:只用候选的**参考文献**(向后)，不用「被引」(向前)：向前会查到窗口之后的论文，包括综述本身。补进来的论文必须在窗口内、类别相符，元数据仍然来自 arXiv。

**失败降级**:Semantic Scholar 不带 key 时常被限流，在时间预算内重试，失败就不扩展，检索照常返回(`citation_expansion.status` 说明原因)。没有模型授权或打分调用失败时，按共同引用次数选，`screen` 的结果会要求模型在方法部分写明。

## 为什么关卡放在 `before_model`

扩展的 `wrap_tool_call` 只能观察：宿主总是返回下游结果，插件没法否决 `present_files`。但 `present_files` 之后模型一定会再被调用一次，`before_model` 可以按消息 ID 替换那条工具结果。所以模型看到的是"交付被拒"，不是"交付成功"。

扩展的钩子不能 `jump_to`(宿主的包装层不带这个声明)。代为交付靠的是：Agent 循环看最后一条 AI 消息有没有工具调用来决定下一步，所以关卡给它补上一个 `present_files` 调用就够了。

决定记录在 `<storage_path>/threads/<thread_id>/gate.jsonl`，评测脚本会收集它。

全文模式下，错配或伪造的证据标记会被拒收，检查器保留原文并要求修订，不会通过删除标记隐藏问题。零证据、引用论文缺少证据标记也不能通过。检查结果使用统一的 `EvidenceCheck` 契约，日志记录 `evidence_schema_version`；通过只代表引语出处和引用关联已检查，不代表每条论断的语义已验证。预算耗尽后的不完整报告仍需明确告知用户未通过核查。

## 安装（本机 Docker 开发环境）

```bash
docker cp extensions/scholar deer-flow-gateway:/tmp/scholar-src
docker exec -w /app/backend deer-flow-gateway uv run --no-sync deerflow extensions install /tmp/scholar-src --yes
```

然后在 `config.yaml` 的 `plugins:` 条目里补上配置，并重启网关：

```yaml
  config:
    enabled: true
    storage_path: /app/backend/.deer-flow/scholar
    max_blocks: 3
    citation_expansion: true        # false = 只用 arXiv 检索结果(消融用)
    # s2_api_key: ...               # 可选，Semantic Scholar key，限流更宽
  host_access:                      # 筛选用的模型由运维授权，插件不持有凭据
    model_invocation:
      roles:
        default: qwen3.5-plus-screen
      max_concurrency: 6
      timeout_seconds: 25
```

`qwen3.5-plus-screen` 是 `models:` 里单独加的一条：同一个 `qwen3.5-plus`,但 `extra_body: {enable_thinking: false}`、`temperature: 0`。开着思考时，一次 10 篇的打分调用要约 100 秒，超过插件工具 30 秒的上限。不配 `host_access` 也能运行，只是不做模型筛选。

本地源码以快照方式安装，改代码后要用 `deerflow extensions upgrade` 重新安装。

## 测试

```bash
pip install -e <deer-flow>/backend/packages/extension-api
pip install -e ".[dev]"
pytest -q && ruff check . && ruff format --check .
```

全部离线运行:arXiv 和 Semantic Scholar 用 `httpx.MockTransport` 模拟，模型用假的 invoker。
