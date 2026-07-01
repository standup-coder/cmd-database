---
{
  "cmd_name": "dnsmasq",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "unbound",
    "systemd-resolved"
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

# dnsmasq

> 轻量级 DNS 转发与 DHCP 服务器

## 用法

```
dnsmasq [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--test` | 测试配置 |
| `--no-daemon` | 前台运行 |
| `--server` | 上游 DNS |

## 示例

### 示例 1: 检查配置

```bash
dnsmasq --test
```

### 示例 2: 前台运行并记录查询

```bash
dnsmasq --no-daemon --log-queries
```

## 风险提示

> ⚠️ **MEDIUM**: dnsmasq 作为 DNS/DHCP 服务，错误配置会导致网络解析异常

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
