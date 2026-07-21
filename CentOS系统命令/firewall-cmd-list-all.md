---
{
  "cmd_name": "firewall-cmd --list-all",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS/RHEL 7+",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/centos.yaml"
}
---

# firewall-cmd --list-all

> List all firewall rules

## 安装

```bash
Pre-installed on CentOS/RHEL 7+
```

## 用法

```
sudo firewall-cmd --list-all
```

## 示例

### 示例 1: Show all firewall settings

```bash
sudo firewall-cmd --list-all
```

### 示例 2: List open ports in public zone

```bash
sudo firewall-cmd --zone=public --list-ports
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[通用Linux命令-MOC|Operating System]]
