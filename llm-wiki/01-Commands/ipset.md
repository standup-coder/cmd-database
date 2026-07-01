---
{
  "cmd_name": "ipset",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "iptables",
    "nftables"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# ipset

> IP 集合管理，常与 iptables 配合

## 用法

```
ipset [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建集合 |
| `add` | 添加成员 |
| `del` | 删除成员 |
| `list` | 列出 |

## 示例

### 示例 1: 创建 IP 黑名单集合

```bash
sudo ipset create blacklist hash:ip
```

### 示例 2: 添加 IP

```bash
sudo ipset add blacklist 1.2.3.4
```

## 关联命令

- [[iptables]]
- [[nftables]]

## 风险提示

> ⚠️ **MEDIUM**: 误删或误加 IP 会影响防火墙策略，请确认集合用途

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
