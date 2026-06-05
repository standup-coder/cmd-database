---
cmd_name: humaneval
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: git clone https://github.com/openai/human-eval.git && pip install -e
  .
cmd_platforms:
- linux
- darwin
- windows
summary: "HumanEval代码生成评测基准，164个Python编程问题，测试函数级代码生成能力"
cmd_level: advanced
cmd_related:
- mbpp
- swe-bench
cmd_tags:
- evaluation
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# humaneval

> HumanEval代码生成评测基准，164个Python编程问题，测试函数级代码生成能力

## 安装

```bash
git clone https://github.com/openai/human-eval.git && pip install -e .
```

## 用法

```
evaluate_functional_correctness [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--sample_file` | 模型生成样本文件 |
| `--problem_file` | 问题定义文件 |
| `--k` | pass@k中的k值 |

## 示例

### 示例 1: 评测代码生成样本

```bash
evaluate_functional_correctness samples.jsonl --problem_file=data/HumanEval.jsonl.gz
```

### 示例 2: 生成并评测代码

```bash
python generate.py --model gpt-4 --output samples.jsonl && evaluate_functional_correctness samples.jsonl
```

## 关联命令

- [[mbpp]]
- [[swe-bench]]

## 风险提示

> ⚠️ **HIGH**: 执行模型生成的代码有风险，需在沙箱运行

## 参考链接

- [https://github.com/openai/human-eval](https://github.com/openai/human-eval)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
