---
{
  "cmd_name": "long-context-eval",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "pip install ruler-benchmark",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lm-eval",
    "inspect-ai"
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

# long-context-eval

> 长上下文评测工具，Needle-in-Haystack、RULER等，测试模型在超长文本中的信息检索能力

## 安装

```bash
pip install ruler-benchmark
```

## 用法

```
python eval.py (使用needle_in_haystack库)
```

## 参数

| Flag | Description |
|------|-------------|
| `--context_length` | 上下文长度 (4k, 8k, 32k, 128k, 1M) |
| `--depth_percent` |  needle 插入深度百分比 |
| `--model` | 评测模型 |

## 示例

### 示例 1: 128K上下文针海捞针

```bash
python needle_eval.py --model llama-3.1-8b --context_length 128000 --depth_percent 50
```

### 示例 2: RULER多任务长上下文评测

```bash
python ruler_eval.py --model claude-3-opus --tasks retrieval,association --max_length 200000
```

## 关联命令

- [[lm-eval]]
- [[inspect-ai]]

## 风险提示

> ⚠️ **LOW**: 长文本评测消耗大量token

## 参考链接

- [https://github.com/gkamradt/LLMTest_NeedleInAHaystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
