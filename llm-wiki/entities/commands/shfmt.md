---
cmd_name: shfmt
cmd_category: Shell脚本/Bash工具
cmd_dimension: Bash工具
cmd_install: brew install shfmt (macOS) 或 go install mvdan.cc/sh/v3/cmd/shfmt@latest
cmd_platforms:
- linux
- darwin
summary: "Shell 脚本格式化工具"
cmd_level: intermediate
cmd_related:
- shellcheck
- bash
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/shell/bash.yaml
---


# shfmt

> Shell 脚本格式化工具

## 安装

```bash
brew install shfmt (macOS) 或 go install mvdan.cc/sh/v3/cmd/shfmt@latest
```

## 用法

```
shfmt [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-w` | 直接修改文件（写回） |
| `-i` | 缩进宽度（默认 0，即自动检测） |
| `-bn` | 二元运算符放在下一行 |
| `-ci` | case 缩进 |
| `-d` | 仅显示需要格式化的差异 |

## 示例

### 示例 1: 格式化并写回文件

```bash
shfmt -w script.sh
```

### 示例 2: 4 空格缩进格式化所有 sh 文件

```bash
shfmt -w -i 4 *.sh
```

### 示例 3: 仅显示格式差异

```bash
shfmt -d script.sh
```

## 关联命令

- [[shellcheck]]
- [[bash]]

## 所属维度

[[Bash工具-MOC|Shell脚本/Bash工具]]
