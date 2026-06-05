---
cmd_name: source
cmd_category: Shell脚本/Bash工具
cmd_dimension: Bash工具
cmd_install: ''
cmd_platforms:
- linux
- darwin
summary: "在当前 Shell 环境中执行脚本（不创建子进程）"
cmd_level: intermediate
cmd_related:
- bash
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/shell/bash.yaml
---


# source

> 在当前 Shell 环境中执行脚本（不创建子进程）

## 用法

```
source 文件名
```

```
. 文件名
```

## 示例

### 示例 1: 重新加载 bash 配置

```bash
source ~/.bashrc
```

### 示例 2: 加载系统环境变量

```bash
. /etc/profile
```

### 示例 3: 加载环境变量后运行应用

```bash
source env.sh && run_app
```

## 关联命令

- [[bash]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改当前 Shell 环境，可能影响后续命令

## 所属维度

[[Bash工具-MOC|Shell脚本/Bash工具]]
