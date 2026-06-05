---
cmd_name: sh
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- bash
- zsh
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: Bourne Shell，标准的Unix命令解释器
created: '2026-06-04'
source_file: data/os/common.yaml
---
# sh

> Bourne Shell，标准的Unix命令解释器

## 安装

```bash
已预装
```

## 用法

```
sh [选项] [脚本文件] [参数...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 执行命令字符串 |
| `-x` | 打印执行的每条命令 |
| `-e` | 命令失败时立即退出 |

## 示例

### 执行命令字符串

```bash
sh -c 'echo hello'
```

### 执行shell脚本并传递参数

```bash
sh script.sh arg1 arg2
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
