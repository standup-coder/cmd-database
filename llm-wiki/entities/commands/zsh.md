---
cmd_name: zsh
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: apt install zsh (Ubuntu) 或 brew install zsh (macOS)
cmd_platforms:
- linux
- darwin
cmd_level: intermediate
cmd_related:
- bash
- sh
cmd_tags:
- linux
- darwin
- intermediate
cmd_risk_level: low
summary: Z Shell，功能强大的交互式Shell，兼容Bash
created: '2026-06-04'
source_file: data/os/common.yaml
---
# zsh

> Z Shell，功能强大的交互式Shell，兼容Bash

## 安装

```bash
apt install zsh (Ubuntu) 或 brew install zsh (macOS)
```

## 用法

```
zsh [选项] [脚本文件] [参数...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 执行命令字符串 |
| `-l` | 作为登录Shell启动 |

## 示例

### 启动Zsh Shell

```bash
zsh
```

### 将Zsh设为默认Shell

```bash
chsh -s $(which zsh)
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
