---
cmd_name: dpkg -r
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu/Debian
cmd_platforms:
- linux
summary: "Remove installed package"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# dpkg -r

> Remove installed package

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
sudo dpkg -r <package>
```

## 示例

### 示例 1: Remove nginx package

```bash
sudo dpkg -r nginx
```

## 风险提示

> ⚠️ **HIGH**: May leave configuration files; use apt remove instead

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
