---
{
  "cmd_name": "safety-eval",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "pip install ml-safety",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "red-teaming",
    "big-bench"
  ],
  "cmd_tags": [
    "evaluation",
    "safety",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# safety-eval

> MLSafety模型安全评测套件，覆盖毒性、偏见、隐私泄露、越狱抗性

## 安装

```bash
pip install ml-safety
```

## 用法

```
python evaluate.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--test_suite` | 测试套件 (toxicity, bias, privacy, jailbreak) |
| `--model` | 待评测模型 |

## 示例

### 示例 1: 毒性和越狱抗性评测

```bash
python evaluate.py --test_suite toxicity,jailbreak --model gpt-4
```

### 示例 2: 全面安全评测

```bash
python evaluate.py --test_suite all --model llama-3-70b --output safety_report.json
```

## 关联命令

- [[red-teaming]]
- [[big-bench]]

## 风险提示

> ⚠️ **LOW**: 评测操作安全

## 参考链接

- [https://github.com/mlcommons/ailuminate](https://github.com/mlcommons/ailuminate)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
