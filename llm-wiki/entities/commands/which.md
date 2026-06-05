---
cmd_name: which
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- whereis
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 查找命令的可执行文件路径
created: '2026-06-04'
source_file: data/os/common.yaml
---
# which

> 查找命令的可执行文件路径

## 安装

```bash
已预装
```

## 用法

```
which [选项] 命令...
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 显示所有匹配路径 |

## 示例

### 查找python可执行文件位置

```bash
which python
```

### 查找所有python路径

```bash
which -a python
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
