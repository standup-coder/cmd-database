---
{
  "cmd_name": "litellm",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install 'litellm[proxy]'",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openai",
    "groq"
  ],
  "cmd_tags": [
    "gateway",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/more.yaml"
}
---

# litellm

> 统一多 LLM API 的网关/代理

## 安装

```bash
pip install 'litellm[proxy]'
```

## 用法

```
litellm [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` |  |
| `--temperature` |  |
| `--proxy` | 启动代理 |

## 示例

### 示例 1: CLI 调用

```bash
litellm --model gpt-4 --temperature 0.2
```

### 示例 2: 启动代理

```bash
litellm --proxy --model gpt-4
```

## 关联命令

- [[openai]]
- [[groq]]

## 风险提示

> ⚠️ **MEDIUM**: 代理会转发 API key，请配置访问控制和日志脱敏

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
