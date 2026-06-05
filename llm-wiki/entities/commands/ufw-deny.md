---
cmd_name: ufw deny
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu
cmd_platforms:
- linux
summary: "Deny firewall rule"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# ufw deny

> Deny firewall rule

## 安装

```bash
Pre-installed on Ubuntu
```

## 用法

```
sudo ufw deny <port/service>
```

## 示例

### 示例 1: Block telnet port

```bash
sudo ufw deny 23
```

## 风险提示

> ⚠️ **MEDIUM**: May block legitimate traffic

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
