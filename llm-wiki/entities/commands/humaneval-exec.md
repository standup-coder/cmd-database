---
cmd_name: humaneval-exec
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: git clone https://github.com/openai/human-eval
cmd_platforms:
- linux
- darwin
summary: "HumanEval代码评测执行器，运行模型生成的代码并通过单元测试，计算pass@k指标"
cmd_level: advanced
cmd_related:
- humaneval
- mbpp
cmd_tags:
- evaluation
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# humaneval-exec

> HumanEval代码评测执行器，运行模型生成的代码并通过单元测试，计算pass@k指标

## 安装

```bash
git clone https://github.com/openai/human-eval
```

## 用法

```
evaluate_functional_correctness [OPTIONS] SAMPLES_FILE
```

## 参数

| Flag | Description |
|------|-------------|
| `--problem_file` | 题目定义文件 |
| `--k` | pass@k的k值 |
| `--n_workers` | 并行工作进程 |

## 示例

### 示例 1: 计算pass@1/10/100

```bash
evaluate_functional_correctness samples.jsonl --problem_file=HumanEval.jsonl.gz --k=1,10,100
```

### 示例 2: 4进程并行评测

```bash
python -m human_eval.evaluate --samples samples.jsonl --n_workers 4
```

## 关联命令

- [[humaneval]]
- [[mbpp]]

## 风险提示

> ⚠️ **HIGH**: 执行生成的代码存在安全风险，需在隔离沙箱中运行

## 参考链接

- [https://github.com/openai/human-eval](https://github.com/openai/human-eval)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
