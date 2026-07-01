---
{
  "cmd_name": "portkey",
  "cmd_category": "AI基础设施/AI网关",
  "cmd_dimension": "AI网关",
  "cmd_install": "pip install portkey-ai",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "helicone",
    "litellm-proxy"
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

# portkey

> Portkey AI网关，支持语义缓存、智能重试、负载均衡、多模型Fallback

## 安装

```bash
pip install portkey-ai
```

## 用法

```
python app.py (使用portkey库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Portkey(api_key=...)` | 初始化客户端 |
| `Config` | 配置缓存、重试、路由策略 |
| `cache` | 语义缓存配置 |

## 示例

### 示例 1: 初始化Portkey客户端

```bash
python -c "from portkey_ai import Portkey; client = Portkey(api_key='pk-xxx')"
```

### 示例 2: 配置缓存+重试+Fallback

```bash
python app.py --cache_enabled --retry_count=3 --fallback_models=gpt-4,gpt-3.5-turbo
```

## 关联命令

- [[helicone]]
- [[litellm-proxy]]

## 风险提示

> ⚠️ **LOW**: 网关代理，注意数据隐私

## 参考链接

- [https://portkey.ai/](https://portkey.ai/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
