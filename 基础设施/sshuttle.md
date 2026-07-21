---
{
  "cmd_name": "sshuttle",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ssh",
    "proxychains"
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

# sshuttle

> 基于 SSH 的透明代理 VPN

## 用法

```
sshuttle [OPTIONS] [USER@]HOST [SUBNETS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 远程 SSH 主机 |
| `-v` | 详细 |
| `--dns` | 代理 DNS |

## 示例

### 示例 1: 通过跳板访问内网

```bash
sshuttle -r user@jump 192.168.0.0/16
```

### 示例 2: 全局代理并转发 DNS

```bash
sshuttle -r user@jump 0/0 --dns
```

## 关联命令

- [[ssh]]
- [[proxychains]]

## 风险提示

> ⚠️ **MEDIUM**: sshuttle 会改变系统路由，请确认目标子网和 DNS 配置

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
