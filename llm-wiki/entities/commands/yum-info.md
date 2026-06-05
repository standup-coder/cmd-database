---
cmd_name: yum info
cmd_category: "操作系统/CentOS系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on CentOS/RHEL
cmd_platforms:
- linux
summary: "Show package information"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/centos.yaml
---


# yum info

> Show package information

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
yum info <package>
```

## 示例

### 示例 1: Show nginx package details

```bash
yum info nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
