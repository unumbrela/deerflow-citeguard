# deerflow-extension-scholar

DeerFlow 插件，给 `systematic-literature-review` skill 提供检索工具和引用核查关卡。只依赖公开的 `deerflow-extension-api`，不改 DeerFlow 核心。

| 贡献 | 作用 |
|---|---|
| `search` 工具 | 在 Gateway 进程内查 arXiv；日期窗口、主类别由代码过滤；结果按线程保存；只返回紧凑索引。**不需要 `allow_host_bash`** |
| `get_batch` 工具 | 子 Agent 按批次号直接取论文数据，模型不再转述。每批不超过 9,000 字符，不会触发宿主的输出外置(12,000) |
| `CitationGateMiddleware` | `present_files` 交付 `.md` 报告后，在模型看到结果前用代码核对：报告里每个 arXiv 编号都必须出自本线程的检索。不通过就把交付结果改写成"被拒绝 + 原因"，最多拒绝 `max_blocks` 次，之后要求模型向用户明确说明 |
| 类别检查(同一中间件) | 用户写了类别(如 `cs.CL`)而检索没用它，就把检索结果换成报错，并作废这次检索：`get_batch` 拒绝取数，基于它写的报告也通不过关卡 |
| 代为交付(同一中间件，`after_model`) | 模型保存了带 arXiv 编号的报告、却不调 `present_files` 就要结束时，由关卡代为调用，报告照样要经过核查。每次检索最多代交一次 |

## 为什么关卡放在 `before_model`

扩展的 `wrap_tool_call` 只能观察：宿主总是返回下游结果，插件没法否决 `present_files`。但 `present_files` 之后模型一定会再被调用一次，`before_model` 可以按消息 ID 替换那条工具结果。所以模型看到的是"交付被拒"，不是"交付成功"。

扩展的钩子不能 `jump_to`(宿主的包装层不带这个声明)。代为交付靠的是：Agent 循环看最后一条 AI 消息有没有工具调用来决定下一步，所以关卡给它补上一个 `present_files` 调用就够了。

决定记录在 `<storage_path>/threads/<thread_id>/gate.jsonl`，评测脚本会收集它。

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
```

本地源码以快照方式安装，改代码后要用 `deerflow extensions upgrade` 重新安装。

## 测试

```bash
pip install -e <deer-flow>/backend/packages/extension-api
pip install -e ".[dev]"
pytest -q && ruff check . && ruff format --check .
```

全部离线运行：arXiv 用 `httpx.MockTransport` 模拟。
