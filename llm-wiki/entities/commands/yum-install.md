---
cmd_name: yum install
cmd_category: "操作系统/CentOS系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on CentOS/RHEL
cmd_platforms:
- linux
summary: "Install new packages"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/os/centos.yaml
---


# yum install

> Install new packages

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo yum install <package>
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | Automatic yes to prompts |

## 示例

### 示例 1: Install nginx web server

```bash
sudo yum install nginx
```

### 示例 2: Install multiple packages

```bash
sudo yum install vim git wget -y
```

## 风险提示

> ⚠️ **MEDIUM**: Installing from untrusted repositories may introduce security risks

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
