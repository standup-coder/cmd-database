---
cmd_name: rmdir
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- rm
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 删除空目录
created: '2026-06-04'
source_file: data/os/common.yaml
---
# rmdir

> 删除空目录

## 安装

```bash
已预装
```

## 用法

```
rmdir [选项] 目录...
```

## 参数

| Flag | Description |
|------|-------------|
| `-p, --parents` | 删除目录及其祖先空目录 |
| `-v, --verbose` | 显示每个被删除的目录 |

## 示例

### 删除空目录

```bash
rmdir emptydir
```

### 删除c、b、a（如果都为空）

```bash
rmdir -p a/b/c
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
