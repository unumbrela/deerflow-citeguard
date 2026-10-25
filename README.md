# deerflow-citeguard

给 [DeerFlow](https://github.com/bytedance/deer-flow)(字节开源的多 Agent 框架)的**文献综述 Agent** 做可靠性评测与修复:量化它会不会"编造论文",查清原因,并用确定性的代码把这一类错误挡在报告之外。

> 状态:基线、机制分析、两轮改进(v2.0 → v2.1)与对照评测已完成。**在我调参所用的同一批 30 个主题上**,引用已验证率 86.9% → 100%,时间窗口 / 类别满足率约 70% → 100%,每份报告 10 篇;但这是**样本内**结果,编造次数的下降不显著(p = 0.052),token 成本反而 +7.6%。下一步是留出主题集与重复运行,详见 [BASELINE.md](BASELINE.md)。
> 活文档:[PLAN.md](PLAN.md)(进度、决策、日志)· [BASELINE.md](BASELINE.md)(每次实验的原始记录与局限)· [ARCH_NOTES.md](ARCH_NOTES.md)(DeerFlow 架构笔记)

## 问题

让 Agent 做"近两年、cs.CL 类别、10 篇、APA 格式"的文献综述,报告读起来都很像样。但逐条拿 arXiv 官方 API 核对引用:

**30 个主题 × 1 次(`qwen3.5-plus`,记忆关闭,基线 `suite-pre-02`)**

| 指标 | 值 |
|---|---|
| 交付报告 | 29 / 30 |
| 引用已验证率(arXiv 编号存在且标题匹配) | 86.9%(291 条) |
| 一半以上引用是编造的运行 | **4 / 29(14%,95% CI 5%–31%)** |
| 满足"近两年" / 满足指定类别 | 69.8% / 70.4% |
| 平均耗时 / token | 341 秒 / 226,567 |

一个运行里编造的不是"某条引用写错了",而是整篇论文——编号、标题、作者(有的写成 "Various authors")、摘要、结论全部虚构,并被写进综合分析里。

## 原因(逐个追踪调用链得出)

DeerFlow 会把过长的工具输出(默认 > 12,000 字符)存成文件,只给模型一份**结构摘要**。检索脚本返回 10 篇论文约 19,600 字符,被换成摘要后只露出第 1 篇。Agent 如果**把原文件读回来**就没事;如果直接把"10 篇论文"派给子 Agent,其余 9 篇就是模型凭空补的。

| 分组(基线 29 个运行) | 运行数 | 编造严重(已验证 < 50%) |
|---|---|---|
| 输出被外置,Agent 读回了原文 | 18 | **0** |
| 输出被外置,Agent 没读回 | 4 | **4** |
| 无法判断(早期消息被摘要压缩) | 7 | 0 |

Fisher 精确检验 p = 0.00014。这是观察性分组而非对照实验,样本小;完整推理与局限见 [BASELINE.md](BASELINE.md)。
过程中也走过弯路(早期把"外置"本身当成原因,后经全量核对修正;评测指标 `resolved` 会被虚构编号蒙混过关,改为 `verified`),都如实记录在文档里。

## 做法

不靠提示词叮嘱模型"记得读文件",而是**让模型没有机会转述论文数据**。改进版 skill 与内置版同名,以 custom skill 的方式覆盖它,不改 DeerFlow 核心:

- `slr_tools.py search`:检索、"近 N 年"由代码按今天算、类别按**主类别**过滤、结果落盘并分批,只向模型打印一份紧凑索引(远小于外置阈值)。
- 子 Agent 直接读取批次文件,主 Agent 不再把论文文本抄进 prompt。
- `slr_tools.py verify`:报告写完后,核对其中每个 arXiv 编号是否出自检索结果,并警告标题 / 第一作者对不上的条目。
- 结果不足时由代码把精确短语放宽为"所有词都出现"(类别与时间窗口不动),避免模型自己放宽用户约束(v2.1)。
- 19 个离线单元测试(arXiv 全部 mock):`python3 -m unittest discover -s skills/systematic-literature-review/tests`

联调中发现的三个环境事实(都已写进 [PLAN.md](PLAN.md) 日志):网关缓存技能列表需重启;custom skill 在沙箱里的路径是 `/mnt/skills/legacy/...`;LocalSandbox 只翻译**命令行里出现的** `/mnt/user-data/...`,脚本内部默认的路径对文件工具和子 Agent 不可见——所以 `--out-dir` 必须由调用方显式传入。

## 结果(同一批 30 个主题,每个 1 次;样本内)

| | 基线 | v2.0 | v2.1 |
|---|---|---|---|
| 引用已验证率 | 86.9% | 100% | 100% |
| 一半以上编造的运行 | 4 / 29 | 0 / 30 | 0 / 30 |
| 满足"近两年" / 指定类别 | 69.8% / 70.4% | 100% / 97.4% | 100% / 100% |
| 平均每份引用数(要求 10) | 10.03 | **8.87** | 10.00 |
| 平均耗时 / token | 341 秒 / 226,567 | 188 秒 / 234,964 | 182 秒 / 243,695 |

v2.0 去掉了编造和约束违反,却让 7 个运行凑不够 10 篇;原因是精确短语过窄,且 Agent 凑不够时自己去掉了类别过滤。v2.1 由代码放宽查询(类别和时间窗口不动)。**v2.1 是看过 v2.0 的失败之后写的,所以上表最后一列是样本内成绩。**

## 仓库结构

```
eval/            评测框架:30 个主题(topics.json)、运行器、arXiv 引用核查、汇总
skills/          改进版 systematic-literature-review(源码)
scripts/         install_skill.sh:把 skills/ 部署为 DeerFlow 的 custom skill
runs/            各次实验的报告、引用核查结果与元数据(原始 trace 因体积未入库)
BASELINE.md  PLAN.md  ARCH_NOTES.md
```

`deer-flow/`(上游代码)不在本仓库内。基线固定在上游 commit `3fdd9bd`。

## 复现

前置:本机 Docker 起好 DeerFlow(`make docker-start`),`config.yaml` 配好模型;评测使用的设置是 `qwen3.5-plus`(阿里云百炼)、`memory.enabled: false`、`allow_host_bash: true`、递归上限 1000。

```bash
git clone https://github.com/bytedance/deer-flow deer-flow && git -C deer-flow checkout 3fdd9bd
scripts/install_skill.sh && docker restart deer-flow-gateway     # 部署改进版 skill

cd eval
python3 -I run_suite.py --name my-run --reps 1 --workers 2        # 跑 30 个主题
python3 -I aggregate.py --name my-run                             # 逐条核对 arXiv 并汇总
```

`run_task.py` 需要一个本地 DeerFlow 账号的 cookie(放在被忽略的 `.local/`,见脚本顶部说明)。

## 安全提示

评测期间为了让 skill 的脚本能跑,打开了 `allow_host_bash: true`:模型可以在网关容器内执行任意 shell,而容器环境变量里有模型 API key,存在提示注入外泄的风险。只应在本机单用户场景使用;不要在多用户或暴露公网的部署里开启。

## 局限

- 每个主题只跑 1 次;编造是运行内的随机事件,基线的置信区间很宽。对比"改进前后"需要重复运行。
- 评测只衡量引用能否对上 arXiv,**不评价综述内容本身的质量**。
- 单一模型、单一 prompt 模板;机制分析中有 7 个运行无法判断。

## 致谢与许可

基于字节跳动开源的 [DeerFlow](https://github.com/bytedance/deer-flow)(MIT)。`arxiv_search.py` 与引用模板来自上游 skill,本仓库在其基础上修改;许可证见 [LICENSE](LICENSE)(MIT,保留上游版权声明)。
