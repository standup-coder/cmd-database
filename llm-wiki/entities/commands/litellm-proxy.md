---
cmd_name: litellm-proxy
cmd_category: AI基础设施/监控与评估
cmd_dimension: 监控与评估
cmd_install: pip install litellm[proxy]
cmd_platforms:
- linux
- darwin
- windows
summary: "LiteLLM代理网关，统一管理100+ LLM API，支持负载均衡、速率限制、成本追踪"
cmd_level: intermediate
cmd_related:
- vllm
- langfuse
cmd_tags:
- monitoring
- gateway
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/monitoring.yaml
---


# litellm-proxy

> LiteLLM代理网关，统一管理100+ LLM API，支持负载均衡、速率限制、成本追踪

## 安装

```bash
pip install litellm[proxy]
```

## 用法

```
litellm [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config` | 配置文件路径 |
| `--model` | 默认模型 |
| `--port` | 代理端口 |

## 示例

### 示例 1: 启动LLM代理网关

```bash
litellm --config proxy_config.yaml
```

### 示例 2: 快速启动单模型代理

```bash
litellm --model gpt-4 --port 8000
```

## 关联命令

- [[vllm]]
- [[langfuse]]

## 风险提示

> ⚠️ **MEDIUM**: 代理网关需配置认证防止未授权访问

## 参考链接

- [https://docs.litellm.ai/docs/simple_proxy](https://docs.litellm.ai/docs/simple_proxy)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
