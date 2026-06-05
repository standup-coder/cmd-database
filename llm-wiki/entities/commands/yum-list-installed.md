---
cmd_name: yum list installed
cmd_category: "操作系统/CentOS系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on CentOS/RHEL
cmd_platforms:
- linux
summary: "List all installed packages"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/centos.yaml
---


# yum list installed

> List all installed packages

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
yum list installed
```

## 示例

### 示例 1: Show all installed packages

```bash
yum list installed
```

### 示例 2: Find nginx-related packages

```bash
yum list installed | grep nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
