---
cmd_name: rpm -e
cmd_category: "操作系统/CentOS系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on CentOS/RHEL
cmd_platforms:
- linux
summary: "Erase (remove) installed package"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/os/centos.yaml
---


# rpm -e

> Erase (remove) installed package

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo rpm -e <package>
```

## 示例

### 示例 1: Remove nginx package

```bash
sudo rpm -e nginx
```

## 风险提示

> ⚠️ **HIGH**: May break dependencies; use yum remove instead

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
