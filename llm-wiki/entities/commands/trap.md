---
cmd_name: trap
cmd_category: Shell脚本/Bash工具
cmd_dimension: Bash工具
cmd_install: ''
cmd_platforms:
- linux
- darwin
summary: "捕获信号并在脚本中执行清理操作"
cmd_level: intermediate
cmd_related:
- bash
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/shell/bash.yaml
---


# trap

> 捕获信号并在脚本中执行清理操作

## 用法

```
trap '命令' 信号
```

```
trap 信号
```

## 示例

### 示例 1: 脚本退出时清理临时文件

```bash
trap 'rm -f $tmpfile' EXIT
```

### 示例 2: 捕获 Ctrl+C 信号

```bash
trap 'echo caught SIGINT' INT
```

### 示例 3: 取消 EXIT 陷阱

```bash
trap - EXIT
```

## 关联命令

- [[bash]]

## 所属维度

[[Bash工具-MOC|Shell脚本/Bash工具]]
