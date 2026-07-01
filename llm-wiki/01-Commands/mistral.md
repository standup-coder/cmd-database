---
{
  "cmd_name": "mistral",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install mistralai 或参考官方",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openai",
    "cohere"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/more.yaml"
}
---

# mistral

> Mistral AI CLI

## 安装

```bash
pip install mistralai 或参考官方
```

## 用法

```
mistral [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `chat` |  |
| `list` | models |

## 示例

### 示例 1: 聊天

```bash
mistral chat --message 'Explain RAG'
```

### 示例 2: 列出模型

```bash
mistral list-models
```

## 关联命令

- [[openai]]
- [[cohere]]

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
