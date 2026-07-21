---
{
  "cmd_name": "perplexity",
  "cmd_category": "AI基础设施/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "pip install perplexity-python 或参考官方 SDK",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "groq",
    "openai-function-calling"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-extra.yaml"
}
---

# perplexity

> Perplexity API CLI

## 安装

```bash
pip install perplexity-python 或参考官方 SDK
```

## 用法

```
perplexity [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` |  |
| `--messages` |  |
| `--stream` |  |

## 示例

### 示例 1: 通过 CLI 提问

```bash
perplexity ask 'What is RAG?'
```

### 示例 2: 流式输出回答

```bash
perplexity --model sonar-pro --stream 'Explain Kubernetes'
```

## 关联命令

- [[groq]]
- [[openai-function-calling]]

## 所属维度

[[扩展工具-MOC|AI基础设施/扩展工具]]
