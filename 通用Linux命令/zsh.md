---
{
  "cmd_name": "zsh",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "apt install zsh (Ubuntu) 或 brew install zsh (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "bash",
    "sh",
    "oh-my-zsh"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
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

### 示例 1: 启动Zsh Shell

```bash
zsh
```

### 示例 2: 将Zsh设为默认Shell

```bash
chsh -s $(which zsh)
```

## 关联命令

- [[bash]]
- [[sh]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
