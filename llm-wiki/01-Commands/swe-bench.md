---
{
  "cmd_name": "swe-bench",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "git clone https://github.com/princeton-nlp/SWE-bench.git && pip install -e .",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "humaneval",
    "agent-bench"
  ],
  "cmd_tags": [
    "evaluation",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# swe-bench

> SWE-bench软件工程评测基准，测试LLM解决真实GitHub Issue的能力

## 安装

```bash
git clone https://github.com/princeton-nlp/SWE-bench.git && pip install -e .
```

## 用法

```
python -m swebench.harness.run_evaluation [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--predictions_path` | 模型预测文件路径 |
| `--swe_bench_tasks` | 评测任务集 |
| `--log_dir` | 日志目录 |

## 示例

### 示例 1: 评测Lite数据集

```bash
python -m swebench.harness.run_evaluation --predictions_path preds.json --swe_bench_tasks princeton-nlp/SWE-bench_Lite --log_dir logs
```

### 示例 2: 评测Verified数据集

```bash
python -m swebench.harness.run_evaluation --predictions_path preds.json --swe_bench_tasks princeton-nlp/SWE-bench_Verified
```

## 关联命令

- [[humaneval]]
- [[agent-bench]]

## 风险提示

> ⚠️ **MEDIUM**: 运行真实代码修改，需在隔离环境执行

## 参考链接

- [https://www.swebench.com/](https://www.swebench.com/)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
