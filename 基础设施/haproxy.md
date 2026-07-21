---
{
  "cmd_name": "haproxy",
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

# haproxy

> TCP/HTTP 负载均衡器

## 用法

```
haproxy [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 检查配置 |
| `-f` | 配置文件 |
| `-sf` | 平滑切换 |

## 示例

### 示例 1: 检查配置

```bash
haproxy -c -f /etc/haproxy/haproxy.cfg
```

### 示例 2: 启动 haproxy

```bash
sudo haproxy -f /etc/haproxy/haproxy.cfg
```

## 关联命令

- [[nginx]]
- [[traefik]]

## 风险提示

> ⚠️ **MEDIUM**: 负载均衡配置错误会导致流量异常，修改后请检查

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
