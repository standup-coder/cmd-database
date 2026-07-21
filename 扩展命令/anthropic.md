---
{
  "cmd_name": "anthropic",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "npm install -g @anthropic-ai/claude-cli 或参考官方",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openai",
    "claude"
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

# anthropic

> Anthropic Claude CLI

## 安装

```bash
npm install -g @anthropic-ai/claude-cli 或参考官方
```

## 用法

```
anthropic [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` |  |
| `--max-tokens` |  |
| `--temperature` |  |

## 示例

### 示例 1: 向 Claude 提问

```bash
anthropic 'Explain transformers'
```

### 示例 2: 指定模型

```bash
anthropic --model claude-3-opus --max-tokens 2048
```

## 关联命令

- [[openai]]

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
