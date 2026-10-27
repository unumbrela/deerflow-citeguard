# 验证与源码快照

## 离线检查

在仓库根目录运行；Python 3.12+，依赖安装见 [插件说明](../extensions/scholar/README.md)。

```bash
.venv/bin/python -m pytest -q extensions/scholar/tests
.venv/bin/python -I -m unittest discover -s eval/tests -q
.venv/bin/ruff check extensions/scholar
.venv/bin/ruff format --check extensions/scholar
```

`test_evidence_pipeline.py` 串联真实插件工具、存储和关卡，模拟外部 HTTP 与筛选模型，检查检索、阅读、证据登记、拒收、修订和重复交付。它不证明真实模型会遵守流程，也不替代在线效果评测。

## 固定一份源码

```bash
.venv/bin/python scripts/capture_snapshot.py create --out .local/releases/my-snapshot
.venv/bin/python scripts/capture_snapshot.py verify .local/releases/my-snapshot
```

- 输出 `source/` 与 `manifest.json`；已有目录不会覆盖。
- 包含插件、测试、Skill、专用子 Agent 定义和脚本。清单记录 Git 提交、dirty 状态、插件版本及逐文件 SHA-256。
- 同时记录执行快照命令的 Python 与依赖版本，明确区别于部署环境。
- 创建期间源码发生变化会中止；验证会发现新增、删除或修改的源码文件。
- 使用固定文件范围，不收集 `.env`、运行配置、cookie、缓存或实验原始 trace。不要向源码文件写入凭据。

这是**源码快照**，不是完整环境镜像。运行配置、模型参数、依赖锁定和在线部署核对仍需补齐；不能据此声称重现了历史实验。校验用于检测文件变化，不提供发布者身份认证。

## 本轮验证记录

2026-10-27，基于提交 `b06e653` 加当前修复，插件版本号仍为 `0.3.5`：

- 插件：本地 127 项、Docker 隔离环境 127 项通过。
- 评测及快照工具：37 项通过；lint、格式检查通过。
- 容器只加载临时源码并运行测试，没有替换运行中的插件或重启网关。
- 源码快照：`.local/releases/u0-evidence-contract-20261027/`，仅保存在本机。
- 可追溯记录：[validation.json](../runs/u0-validation-20261027/validation.json)，含源码哈希、容器依赖和测试结果。

下一步先锁定部署配置与依赖，再使用同一快照做真实模型冒烟；通过后再登记可发布版本。
