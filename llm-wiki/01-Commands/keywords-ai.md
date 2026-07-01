---
{
  "cmd_name": "keywords-ai",
  "cmd_category": "AI基础设施/AI网关",
  "cmd_dimension": "AI网关",
  "cmd_install": "pip install keywordsai",
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

# keywords-ai

> Keywords AI统一LLM API管理平台，支持多密钥管理、日志分析、用户追踪

## 安装

```bash
pip install keywordsai
```

## 用法

```
python app.py (使用keywordsai库)
```

## 参数

| Flag | Description |
|------|-------------|
| `KeywordsAIClient` | 客户端初始化 |
| `log_inference` | 记录推理调用 |

## 示例

### 示例 1: 初始化Keywords AI客户端

```bash
python -c "from keywordsai import KeywordsAIClient; c = KeywordsAIClient(api_key='kw-xxx')"
```

### 示例 2: 查看推理日志 API

```bash
python -c "from keywordsai import KeywordsAIClient; help(KeywordsAIClient.log_inference)"
```

## 关联命令

- [[helicone]]
- [[portkey]]

## 风险提示

> ⚠️ **LOW**: 注意API密钥安全

## 参考链接

- [https://www.keywordsai.co/](https://www.keywordsai.co/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
