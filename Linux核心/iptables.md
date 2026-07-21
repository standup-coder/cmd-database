---
{
  "cmd_name": "iptables",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "nftables",
    "ip",
    "ufw"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# iptables

> IPv4 包过滤与 NAT 防火墙

## 用法

```
iptables [OPTIONS] -t table -A chain rule
```

## 参数

| Flag | Description |
|------|-------------|
| `-A` | 追加规则 |
| `-D` | 删除规则 |
| `-L` | 列出规则 |
| `-F` | 清空规则 |

## 示例

### 示例 1: 列出当前规则

```bash
sudo iptables -L -v -n
```

### 示例 2: 允许 SSH

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

## 关联命令

- [[nftables]]
- [[ip]]

## 风险提示

> ⚠️ **HIGH**: 错误的规则会阻断合法流量或放行攻击，修改前请保存并测试

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
