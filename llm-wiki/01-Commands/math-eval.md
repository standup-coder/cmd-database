---
{
  "cmd_name": "math-eval",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "pip install math-verify",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lm-eval",
    "inspect-ai"
  ],
  "cmd_tags": [
    "inference",
    "evaluation",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# math-eval

> 数学能力评测工具，支持GSM8K、MATH、SVAMP等数据集，验证模型推理和计算准确性

## 安装

```bash
pip install math-verify
```

## 用法

```
python eval.py (使用math_verify库)
```

## 参数

| Flag | Description |
|------|-------------|
| `--dataset` | 数据集 (gsm8k, math, svamp) |
| `--model` | 评测模型 |
| `--cot` | 链式思维提示 |

## 示例

### 示例 1: GSM8K链式思维评测

```bash
python eval_math.py --dataset gsm8k --model gpt-4 --cot --output results.json
```

### 示例 2: MATH数据集4-shot评测

```bash
python eval_math.py --dataset math --model llama-3-70b --n_shot 4
```

## 关联命令

- [[lm-eval]]
- [[inspect-ai]]

## 风险提示

> ⚠️ **LOW**: 评测操作安全

## 参考链接

- [https://github.com/huggingface/math-verify](https://github.com/huggingface/math-verify)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
