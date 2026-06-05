---
cmd_name: shellcheck
cmd_category: Shell脚本/Bash工具
cmd_dimension: Bash工具
cmd_install: apt install shellcheck (Ubuntu) 或 brew install shellcheck (macOS)
cmd_platforms:
- linux
- darwin
summary: "Shell 脚本静态分析工具，检测常见错误和最佳实践"
cmd_level: intermediate
cmd_related:
- bash
- shfmt
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/shell/bash.yaml
---


# shellcheck

> Shell 脚本静态分析工具，检测常见错误和最佳实践

## 安装

```bash
apt install shellcheck (Ubuntu) 或 brew install shellcheck (macOS)
```

## 用法

```
shellcheck [选项] [脚本文件]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 排除指定错误代码 |
| `-s` | 指定 shell 方言 (bash/sh/dash) |
| `-f` | 输出格式 (tty/json/checkstyle) |
| `-S` | 严重级别 (error/warning/info/style) |

## 示例

### 示例 1: 检查脚本中的问题

```bash
shellcheck script.sh
```

### 示例 2: 排除指定警告

```bash
shellcheck -e SC2086 script.sh
```

### 示例 3: JSON 格式输出

```bash
shellcheck -f json script.sh
```

### 示例 4: 指定 bash 方言

```bash
shellcheck -s bash script.sh
```

## 关联命令

- [[bash]]
- [[shfmt]]

## 所属维度

[[Bash工具-MOC|Shell脚本/Bash工具]]
