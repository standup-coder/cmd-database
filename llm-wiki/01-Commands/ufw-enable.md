---
{
  "cmd_name": "ufw enable",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
---

# ufw enable

> Enable Ubuntu firewall

## 安装

```bash
Pre-installed on Ubuntu
```

## 用法

```
sudo ufw enable
```

## 示例

### 示例 1: Activate firewall

```bash
sudo ufw enable
```

### 示例 2: 非交互式启用防火墙

```bash
sudo ufw enable --force
```

## 风险提示

> ⚠️ **HIGH**: May block SSH access; configure rules first

## 所属维度

[[Operating System-MOC|Operating System]]
