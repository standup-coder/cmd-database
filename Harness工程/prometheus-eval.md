---
{
  "cmd_name": "prometheus-eval",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "pip install prometheus-eval",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mt-bench",
    "alpaca-eval"
  ],
  "cmd_tags": [
    "evaluation",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# prometheus-eval

> Prometheus开源LLM评估模型，无需GPT-4即可进行高质量指令评测

## 安装

```bash
pip install prometheus-eval
```

## 用法

```
python evaluate.py (使用prometheus-eval库)
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | Prometheus模型路径 |
| `--data` | 评测数据 |

## 示例

### 示例 1: 使用开源模型评估

```bash
python evaluate.py --model prometheus-eval/prometheus-7b-v2.0 --data eval_set.json
```

### 示例 2: 生成评估反馈

```bash
python evaluate.py --model prometheus-eval/prometheus-7b-v2.0 --data eval_set.json --feedback
```

## 关联命令

- [[mt-bench]]
- [[alpaca-eval]]

## 风险提示

> ⚠️ **LOW**: 本地评估，无需API

## 参考链接

- [https://github.com/prometheus-eval/prometheus-eval](https://github.com/prometheus-eval/prometheus-eval)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
