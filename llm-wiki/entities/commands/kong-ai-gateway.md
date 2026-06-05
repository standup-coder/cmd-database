---
cmd_name: kong-ai-gateway
cmd_category: AI基础设施/AI网关
cmd_dimension: AI网关
cmd_install: docker pull kong:3.5
cmd_platforms:
- linux
- darwin
- windows
summary: "Kong企业级AI网关，支持LLM路由、速率限制、语义缓存、令牌消耗控制"
cmd_level: intermediate
cmd_related:
- helicone
- portkey
cmd_tags:
- gateway
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/ai-gateway.yaml
---


# kong-ai-gateway

> Kong企业级AI网关，支持LLM路由、速率限制、语义缓存、令牌消耗控制

## 安装

```bash
docker pull kong:3.5
```

## 用法

```
docker run [OPTIONS] kong:3.5
```

## 参数

| Flag | Description |
|------|-------------|
| `KONG_PLUGINS` | 启用AI相关插件 |
| `ai-proxy` | AI代理插件 |
| `ai-prompt-guard` | Prompt安全检查 |

## 示例

### 示例 1: 启动Kong AI网关

```bash
docker run -e KONG_PLUGINS=bundled,ai-proxy -p 8000:8000 kong:3.5
```

### 示例 2: 配置AI代理路由

```bash
curl http://localhost:8001/plugins -d name=ai-proxy -d config.route_type=llm/v1/chat
```

## 关联命令

- [[helicone]]
- [[portkey]]

## 风险提示

> ⚠️ **MEDIUM**: 企业级网关需正确配置安全策略

## 参考链接

- [https://konghq.com/products/kong-ai-gateway](https://konghq.com/products/kong-ai-gateway)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
