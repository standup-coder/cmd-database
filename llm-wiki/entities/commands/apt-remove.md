---
cmd_name: apt remove
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu/Debian
cmd_platforms:
- linux
summary: "Remove installed packages"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# apt remove

> Remove installed packages

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
sudo apt remove <package>
```

## 参数

| Flag | Description |
|------|-------------|
| `--purge` | Remove package and configuration files |

## 示例

### 示例 1: Remove nginx (keep config)

```bash
sudo apt remove nginx
```

### 示例 2: Remove nginx and its config files

```bash
sudo apt remove --purge nginx
```

## 风险提示

> ⚠️ **HIGH**: Removing system packages may break system

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]
