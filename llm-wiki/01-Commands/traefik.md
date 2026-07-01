---
{
  "cmd_name": "traefik",
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
    "caddy"
  ],
  "cmd_tags": [
    "edge",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# traefik

> 云原生边缘路由/反向代理

## 用法

```
traefik [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--configFile` | 配置文件 |
| `--api.insecure` |  |
| `--providers.docker` |  |

## 示例

### 示例 1: 加载配置文件启动

```bash
traefik --configFile=traefik.toml
```

### 示例 2: Docker 提供器模式

```bash
traefik --providers.docker=true --api.insecure=true
```

## 关联命令

- [[nginx]]
- [[caddy]]

## 风险提示

> ⚠️ **MEDIUM**: 错误的 TLS 或路由配置会导致证书或服务不可达

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
