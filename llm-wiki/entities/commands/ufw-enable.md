---
cmd_name: ufw enable
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu
cmd_platforms:
- linux
summary: "Enable Ubuntu firewall"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
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

## 风险提示

> ⚠️ **HIGH**: May block SSH access; configure rules first

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
