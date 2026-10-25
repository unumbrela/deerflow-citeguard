# DeerFlow 二开项目规划

> 活文档:每完成一步就更新「进度」和「日志」,决策变化写进「决策记录」。
> 最后更新:2026-10-25

## 1. 目标

基于 [bytedance/deer-flow](https://github.com/bytedance/deer-flow)(MIT)做二次开发,产出一个可写进 Agent 实习简历的项目。

**简历目标句式(数字待实测填入):**
> 基于 DeerFlow 构建【垂直场景】skill,设计 N 条用例的自动评测,将任务成功率从 X% 提升到 Y%,单任务 token 成本降低 Z%。

**成功标准**
- [ ] 有可运行的 Demo 和清晰的 README
- [ ] 有评测集和"改进前 → 改进后"的量化对比
- [ ] 每项改动都能讲清"为什么、怎么验证"
- [ ] (加分)至少 1 个 PR 被上游合并

## 2. 方案

**主线:评测体系(A)+ 一个垂直场景 skill(B),视进度加入成本/稳定性优化(C)。**

| 方向 | 内容 | 状态 |
|---|---|---|
| A 评测 | 30~50 条任务,指标:完成率、引用准确率、耗时、token 成本 | 待定 |
| B 场景 | 一个自己会用的垂直场景(见待决事项) | 待定 |
| C 优化 | 上下文压缩、重试、输出校验、子任务用便宜模型 | 可选 |
| D 上游 PR | 从 bug / 文档 / 小功能开始 | 可选 |

## 3. 里程碑

| # | 里程碑 | 产出 | 预计 |
|---|---|---|---|
| M0 | 环境跑通 | 本地启动 DeerFlow,完成一次完整任务 | 第 1 周 |
| M1 | 读懂架构 | 模块图 + 一次任务的执行流程笔记 | 第 1~2 周 |
| M2 | 基线评测 | 评测集 v1 + 未改动版本的基线数据 | 第 3 周 |
| M3 | 场景 skill | 垂直场景功能可用 | 第 4~5 周 |
| M4 | 优化迭代 | 针对失败案例改进,对比数据 | 第 6~7 周 |
| M5 | 打磨交付 | README、架构图、Demo、简历描述 | 第 8 周 |
| M6 | 投递 | 简历定稿,开始投递并准备面试 | 第 9 周起 |

## 4. 进度

- [x] 选定项目:DeerFlow
- [x] 创建规划文档
- [x] M0 环境跑通:服务正常,完整任务 `runs/baseline-02` 成功交付报告
- [ ] M1 读懂架构:初版见 [ARCH_NOTES.md](ARCH_NOTES.md),待读清单未完成
- [x] M2 基线评测:30 主题评测集 + 引用核查脚本 + 正式基线 `suite-pre-02`(见 [BASELINE.md](BASELINE.md))。**局限:每主题只跑 1 次,尚无重复运行**
- [ ] M3 场景 skill:**进行中**。`skills/custom/systematic-literature-review/`(同名覆盖内置版)已写好并冒烟通过(2 主题 20/20 引用全部验证);全量对照 `suite-v2-01` 运行中
- [ ] M4 优化迭代
- [ ] M5 打磨交付
- [ ] M6 投递

## 5. 待决事项

- [x] 场景:论文调研(2026-10-24 确定)
- [x] 模型 API:阿里云百炼(DashScope),国内站;key 在 `deer-flow/.env`(已 gitignore)
- [x] 本机环境:Docker 29、Node 24、Python 3.12 齐全;走 Docker 路径,无需装 uv/pnpm/nginx
- [x] 核实仓库:MIT 许可,活跃(当天有提交),基线 commit `3fdd9bd`
- [ ] 基线任务跑通后,确认哪个 Qwen 模型效果与成本更合适
- [ ] 确定具体增量点(见 ARCH_NOTES.md 第 7 节)

## 6. 决策记录

| 日期 | 决策 | 原因 |
|---|---|---|
| 2026-10-24 | 选 DeerFlow 作为主项目 | MIT 许可、架构完整(子 Agent / memory / sandbox / skills / MCP)、国内资料多 |
| 2026-10-24 | 重点放评测与可靠性 | 做功能的人多,做评测的人少,且结果可量化 |
| 2026-10-24 | 场景定为论文调研 | 仓库已有 `systematic-literature-review` skill,可在其上做增量;其自带 eval 只检查流程,不衡量内容质量,存在空位 |
| 2026-10-24 | 走 Docker 路径 | 仓库推荐;本机已有 Docker,不需额外装工具 |
| 2026-10-24 | 模型:Qwen(百炼),主力 `qwen3.5-plus`,低成本 `qwen-flash` | `qwen3-max` 在该账号下不存在;三个模型已实测可用 |
| 2026-10-25 | 二开优先做 skill + 扩展,少改核心 | 仓库 AGENTS.md 要求 extension-first,也便于向上游提 PR |
| 2026-10-25 | 评测期间 `memory.enabled: false` | 长期记忆会跨运行注入,使运行不独立并扭曲行为(t02 被诱导反问用户)。日常使用时再打开 |
| 2026-10-25 | 主指标改为 `verified`(编号存在且标题匹配) | `resolved` 会被虚构编号蒙混过关(baseline-03 假通过 10/10,实为 1/10) |
| 2026-10-25 | 改进版 skill 放 `skills/custom/` 并与内置版**同名**覆盖 | 投影逻辑里 custom 按名字遮蔽 public;前后对比用完全相同的 prompt,变量只有 skill。该目录在上游被 gitignore,不影响上游 |
| 2026-10-25 | 修复点放在"让模型无法转述论文数据",不靠提示词叮嘱 | 全量追踪显示:检索输出被外置且未读回 → 4/4 编造;读回 → 0/18(p=0.00014)。所以检索结果由脚本落盘分批,子 Agent 直接读文件;报告写完由脚本核对每个 arXiv 编号 |
| 2026-10-25 | **选 B:`allow_host_bash: true`**(用户决定) | 最快让 skill 按设计使用 arXiv 脚本。**已知代价**:模型可在网关容器内执行任意 shell,容器环境变量含百炼 key,存在提示注入外泄风险。缓解:仅限本机单用户使用,项目结束后轮换 key 并把该项改回 `false`。`baseline-02` 保留为"默认配置"基线,`baseline-03-bash` 为"放开 bash"基线 |

## 7. 风险

- 只换模型或改界面 → 面试被追问会露馅。每项改动必须有验证数据。
- 与已有二开(trace 面板、Copilot 适配)重复 → 动手前先查现有 fork,避开同方向。
- 上游 2.0 变动大 → 以当前仓库代码为准,固定一个 commit 作为基线。
- 范围膨胀 → 严格按里程碑推进,C / D 是可选项。

## 8. 日志

- 2026-10-24:完成调研与选型,创建本文档。
- 2026-10-24:clone 仓库,生成 `config.yaml` / `.env`,配置三个 Qwen 模型(已测通),`make docker-init` 完成。写出 ARCH_NOTES.md 初版。
- 2026-10-24:首次 `docker-start` 失败:Colima 缺 buildx,Dockerfile 的 `--mount` 需要 BuildKit。已 `brew install docker-buildx`,并在 `~/.docker/config.json` 加 `cliPluginsExtraDirs`(备份:`config.json.bak-deerflow`)。
- 2026-10-25:第二次失败:Colima 虚拟机磁盘 20GiB 用了 97%(`no space left on device`)。经用户同意扩容到 50GiB(`colima stop && colima start --disk 50`),未删除任何数据;其他 9 个容器中断约 1 分钟,2 个 blog 容器因重启策略为 `no` 需手动启动,已恢复。
- 2026-10-25:`make docker-start` 成功,四个容器运行(nginx / frontend / gateway / redis)。管理员账号已由用户自行创建;我另注册了一个评测专用的普通用户供脚本使用(凭据与 cookie 在 `.local/`,权限 600)。
- 2026-10-25:写 `eval/run_task.py`(创建线程 → 流式运行 → 记录耗时/事件/token)。冒烟测试(qwen-flash,问 1+1)2.1 秒通过。**观察:一句话任务也消耗约 1.4 万输入 token,是系统提示词 + 全部 skill 描述的固定开销,可作为成本优化的候选点。**
- 2026-10-25:启动基线 `runs/baseline-01`(qwen3.5-plus,文献综述:LLM agent evaluation benchmarks,10 篇,cs.CL,APA)。结果:撞上我设的 200 步上限,无交付报告,但暴露出 bash 被禁用、`web_fetch` 401、`web_search` 不稳定、时间窗口违规等问题,详见 [BASELINE.md](BASELINE.md)。修正脚本(上限改 1000、token 字段改名),重跑 `runs/baseline-02`。
- 2026-10-25:`baseline-02` 成功(601 秒,约 50 万 token,交付报告)。用 arXiv 官方 API 核查:10/10 论文真实存在;但第一作者 6/10 正确、满足近两年 5/10、满足 cs.CL 2/10。写出 `eval/check_citations.py`。详见 BASELINE.md。**下一步**:扩成评测集并做重复运行,同时决定检索方案。
- 2026-10-25:用户选择方案 B。`config.yaml` 设 `allow_host_bash: true`,重启网关;冒烟测试确认 Agent 能经 `bash` 跑通 `arxiv_search.py` 并拿到权威元数据。启动 `runs/baseline-03-bash`(同任务同模型)。
- 2026-10-25:写评测框架 `eval/{topics.json,run_suite.py,aggregate.py}`(30 个主题,覆盖 8 个 arXiv 类别,可断点续跑)。冒烟(2 主题)20/20 引用全部验证通过,**未重现 baseline-03 的编造 → 编造是随机的**,需要全量数据估计发生率。启动全量 `runs/suite-pre-01`(30 个主题 × 1 次,并发 3,预计 1 小时以上)。
- 2026-10-25:`suite-pre-01` 跑完但**作废**:(1)记忆串扰,t02 被"你之前做过"诱导成反问用户,输入消息随运行增长;(2)核查脚本被 arXiv 429 限流,11 份没核查成;(3)核查脚本只认 `## References`,t14 被解析成 0 条。已关闭 `memory.enabled`、给核查加退避重试、兼容 `Sources` 标题。详见 BASELINE.md。
- 2026-10-25:**arXiv 对本机 IP 限流**(429/503),核查脚本重试后仍失败。改进:`check_citations.py` 改用 https、带 User-Agent、读 `Retry-After`、429/5xx/超时都退避重试、每个 arXiv 编号本地缓存(`eval/.arxiv_cache.json`)。限流未解除前**暂停启动 `suite-pre-02`**:Agent 的 `arxiv_search.py` 与核查共用出口 IP,在限流期间跑会把"检索失败"混进结果。后台轮询中,恢复后再继续。
- 2026-10-25(新会话):arXiv 限流已自行解除(几小时后探测 200)。重写 `check_citations.py` 的解析:按"报告里出现的每个 arXiv 编号"在全文找 APA 行,不再依赖 `## References` 章节;去掉标题/章节号/`**Citation**:` 前缀;以**最后一处** APA 行(文末参考文献)为准;新增 `consistent` 指标(同一论文多处引用是否互相矛盾)。用已知答案回归:baseline-02 verified 8/10、first_author 6/10(WebArena 自相矛盾被标出);baseline-03 verified 1/10;t14 由 0 条变为 10 条。`run_suite.py` 并发降到 2 并加启动前 arXiv 探测;`aggregate.py` 新增 `search_429` 统计。后台串行执行:重核 pre-01 → 记忆关闭的 `suite-pre-02` → 汇总,日志 `runs/chain-pre02.log`。
- 2026-10-25:`suite-pre-02` 完成,成为正式基线:交付 29/30;引用已验证 86.9%;一半以上编造的运行 4/29(14%,CI 5–31%);时间窗口 70%、类别 70%;平均 341 秒 / 226,567 token。关记忆对编造率无可检出影响(p=0.50)。**更正**:"输出外置导致编造"不能作通用解释(58 个运行 57 个都外置)。详见 BASELINE.md。
- 2026-10-25:`baseline-03-bash` 更快更省(303 秒 / 23.7 万 token),但**引用已验证仅 1/10:Agent 编造了 9 篇论文**。根因:检索输出 19,617 字符超过 `externalize_min_chars: 12000`,被换成摘要,Agent 没读原文件就编造。同时发现并修复了核查脚本缺陷(`resolved` 只查编号存在,会被虚构编号蒙混过关;改用 `verified` = 编号存在且标题匹配)。详见 BASELINE.md。
- 2026-10-25(新会话):读 skill 与 arxiv_search.py,**全量追踪 suite-pre-02 的调用链**,得出编造的真正分界线是"外置后是否读回原文"(BASELINE.md 新增一节,并修订了此前的更正)。实现 `skills/custom/systematic-literature-review/`:`slr_tools.py search`(按 `--years` 由代码算日期、只留主类别匹配、结果落盘并分批、只打印紧凑索引)与 `verify`(报告里每个 arXiv 编号必须出自检索结果);15 个离线单元测试。
- 2026-10-25:**联调发现三个环境事实**:(1) 网关按配置缓存技能列表,新增 skill 后要 `docker restart deer-flow-gateway` 才生效;(2) custom 目录下的 skill 在沙箱里的路径是 `/mnt/skills/legacy/<name>/`,不是 `custom`,SKILL.md 不能写死路径;(3) **LocalSandbox 只翻译命令行里出现的 `/mnt/user-data/...`**,脚本内部默认的路径会落到容器字面路径,文件工具和子 Agent 都看不到——所以 `--out-dir`/`--papers` 必须必填。第一次联调因此退化成 3 篇论文。修复后冒烟 t01、t02 各 10/10。
- 2026-10-25:观察到 t01 没有按 SKILL.md 运行 `verify`(自己写了临时检查),说明核查关卡靠模型自觉不可靠。已启动全量 `suite-v2-01`(30 主题 × 1 次,配置与 pre-02 完全一致),待结果再决定是否把核查改成中间件强制。
