---
{
  "cmd_name": "openrouter",
  "cmd_category": "AI基础设施/AI网关",
  "cmd_dimension": "AI网关",
  "cmd_install": "pip install openrouter",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "helicone",
    "portkey"
  ],
  "cmd_tags": [
    "gateway",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-gateway.yaml"
}
---

# openrouter

> OpenRouter统一访问100+开源和商用模型API，标准化接口、自动竞价

## 安装

```bash
pip install openrouter
```

## 用法

```
python app.py (使用openrouter库)
```

```
curl https://openrouter.ai/api/v1/chat/completions
```

## 参数

| Flag | Description |
|------|-------------|
| `HTTP-Referer` | 应用来源标识 |
| `X-Title` | 应用名称 |

## 示例

### 示例 1: 通过OpenRouter调用Claude

```bash
python -c "import openai; client = openai.OpenAI(base_url='https://openrouter.ai/api/v1', api_key='sk-or-xxx'); r = client.chat.completions.create(model='anthropic/claude-3.5-sonnet', messages=[{'role':'user','content':'Hello'}])"
```

### 示例 2: 列出所有可用模型

```bash
curl https://openrouter.ai/api/v1/models | jq '.data[].id'
```

## 关联命令

- [[helicone]]
- [[portkey]]

## 风险提示

> ⚠️ **LOW**: 第三方API聚合，注意数据安全

## 参考链接

- [https://openrouter.ai/](https://openrouter.ai/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
