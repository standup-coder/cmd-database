---
cmd_name: whereis
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- which
- locate
- find
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 定位命令的二进制、源码和手册页文件
created: '2026-06-04'
source_file: data/os/common.yaml
---
# whereis

> 定位命令的二进制、源码和手册页文件

## 安装

```bash
已预装
```

## 用法

```
whereis [选项] 命令...
```

## 参数

| Flag | Description |
|------|-------------|
| `-b` | 只搜索二进制文件 |
| `-m` | 只搜索手册页 |
| `-s` | 只搜索源码 |

## 示例

### 查找python的所有相关文件

```bash
whereis python
```

### 只查找python二进制文件

```bash
whereis -b python
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
