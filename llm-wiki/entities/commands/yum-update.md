---
cmd_name: yum update
cmd_category: "操作系统/CentOS系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on CentOS/RHEL
cmd_platforms:
- linux
summary: "Update all installed packages"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/os/centos.yaml
---


# yum update

> Update all installed packages

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo yum update
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | Automatic yes to prompts |

## 示例

### 示例 1: Update all packages

```bash
sudo yum update
```

### 示例 2: Update without prompts

```bash
sudo yum update -y
```

## 风险提示

> ⚠️ **MEDIUM**: May break compatibility; test in non-production first

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
