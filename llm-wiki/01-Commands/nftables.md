---
{
  "cmd_name": "nftables",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "iptables",
    "ip"
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

# nftables

> 新一代 nftables 防火墙（nft 命令）

## 用法

```
nft [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `list` | ruleset 列出规则 |
| `add` | table 创建表 |
| `add` | chain 创建链 |
| `add` | rule 添加规则 |

## 示例

### 示例 1: 列出所有规则

```bash
sudo nft list ruleset
```

### 示例 2: 创建 filter 表

```bash
sudo nft add table ip filter
```

## 关联命令

- [[iptables]]
- [[ip]]

## 风险提示

> ⚠️ **HIGH**: nftables 规则直接影响网络策略，请在本地测试后再应用

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
