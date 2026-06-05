---
cmd_name: export
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related: []
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 设置或显示环境变量
created: '2026-06-04'
source_file: data/os/common.yaml
---
# export

> 设置或显示环境变量

## 安装

```bash
已预装
```

## 用法

```
export [选项] [名称[=值]...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 以可复用格式显示所有变量 |
| `-n` | 从导出列表中移除变量 |

## 示例

### 添加路径到PATH

```bash
export PATH=$PATH:/usr/local/bin
```

### 设置环境变量

```bash
export MY_VAR=value
```

### 显示所有导出的变量

```bash
export -p
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
