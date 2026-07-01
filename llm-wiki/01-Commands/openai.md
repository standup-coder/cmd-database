---
{
  "cmd_name": "openai",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install openai",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "groq",
    "anthropic"
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

# openai

> OpenAI 官方 CLI

## 安装

```bash
pip install openai
```

## 用法

```
openai [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `api` | 调用 API |
| `chat.completions.create` |  |
| `models` | list |

## 示例

### 示例 1: 调用 ChatGPT

```bash
openai api chat.completions.create -m gpt-4 -g user 'Hello'
```

### 示例 2: 列出模型

```bash
openai api models.list
```

## 关联命令

- [[groq]]
- [[anthropic]]

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
