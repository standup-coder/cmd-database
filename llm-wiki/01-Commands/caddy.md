---
{
  "cmd_name": "caddy",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nginx",
    "traefik"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# caddy

> 易用且默认 HTTPS 的 Web 服务器

## 用法

```
caddy [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 启动 |
| `reverse-proxy` | 快速反向代理 |
| `file-server` | 静态文件 |

## 示例

### 示例 1: 启动 Caddy

```bash
caddy run
```

### 示例 2: 快速反向代理

```bash
caddy reverse-proxy --from :80 --to localhost:8080
```

## 关联命令

- [[nginx]]
- [[traefik]]

## 风险提示

> ⚠️ **MEDIUM**: Caddy 会自动申请证书，请确认域名解析和防火墙

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
