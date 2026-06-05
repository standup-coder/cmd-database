---
cmd_name: rpm -i
cmd_category: "操作系统/CentOS系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on CentOS/RHEL
cmd_platforms:
- linux
summary: "Install RPM package file"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/os/centos.yaml
---


# rpm -i

> Install RPM package file

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo rpm -i <package.rpm>
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | Verbose output |
| `-h` | Print hash marks during installation |

## 示例

### 示例 1: Install RPM with progress

```bash
sudo rpm -ivh package.rpm
```

## 风险提示

> ⚠️ **HIGH**: Installing untrusted RPM files may compromise system

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
