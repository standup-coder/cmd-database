---
cmd_name: helicone
cmd_category: AI基础设施/AI网关
cmd_dimension: AI网关
cmd_install: pip install helicone
cmd_platforms:
- linux
- darwin
- windows
summary: "Helicone LLM可观测性网关，一行代码接入，支持缓存、重试、成本追踪、A/B测试"
cmd_level: intermediate
cmd_related:
- portkey
- openrouter
cmd_tags:
- gateway
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ai-gateway.yaml
---


# helicone

> Helicone LLM可观测性网关，一行代码接入，支持缓存、重试、成本追踪、A/B测试

## 安装

```bash
pip install helicone
```

## 用法

```
python app.py (替换base_url为helicone)
```

## 参数

| Flag | Description |
|------|-------------|
| `base_url='https://oai.hconeai.com/v1'` | 代理OpenAI请求 |
| `Helicone-Auth` | 认证Header |
| `Helicone-Cache-Enabled` | 启用语义缓存 |

## 示例

### 示例 1: 一行代码接入Helicone代理

```bash
python -c "import openai; client = openai.OpenAI(api_key='sk-xxx', base_url='https://oai.hconeai.com/v1')"
```

### 示例 2: cURL通过Helicone调用API

```bash
curl https://oai.hconeai.com/v1/chat/completions -H 'Helicone-Auth: Bearer hk-xxx' -H 'Content-Type: application/json' -d '{"model":"gpt-4","messages":[]}'
```

## 关联命令

- [[portkey]]
- [[openrouter]]

## 风险提示

> ⚠️ **LOW**: 代理服务，注意数据隐私

## 参考链接

- [https://www.helicone.ai/](https://www.helicone.ai/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
