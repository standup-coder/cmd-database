---
{
  "cmd_name": "judge-eval",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "pip install judge-eval",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "prometheus-eval",
    "mt-bench"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# judge-eval

> LLM-as-Judge评估框架，系统化评估裁判模型质量，减少位置偏见和长度偏见

## 安装

```bash
pip install judge-eval
```

## 用法

```
python evaluate_judge.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--judge_model` | 待评测的裁判模型 |
| `--reference_judge` | 参考裁判(默认GPT-4) |
| `--bias_type` | 偏见类型 (position, length, verbosity) |

## 示例

### 示例 1: 评估Prometheus作为裁判的质量

```bash
python evaluate_judge.py --judge_model prometheus-7b --reference_judge gpt-4
```

### 示例 2: 评测多个模型的位置偏见和长度偏见

```bash
python evaluate_judge.py --judge_model all --bias_type position,length
```

## 关联命令

- [[prometheus-eval]]
- [[mt-bench]]

## 风险提示

> ⚠️ **LOW**: 评测框架操作安全

## 参考链接

- [https://github.com/hemingkx/LLM-as-Judge](https://github.com/hemingkx/LLM-as-Judge)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
