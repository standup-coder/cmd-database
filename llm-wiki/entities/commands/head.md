---
cmd_name: head
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- tail
- cat
- less
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 显示文件开头部分
created: '2026-06-04'
source_file: data/os/common.yaml
---
# head

> 显示文件开头部分

## 安装

```bash
已预装
```

## 用法

```
head [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n <N>` | 显示前N行（默认10行） |
| `-c <N>` | 显示前N字节 |
| `-q` | 不显示文件名标题 |

## 示例

### 显示文件前20行

```bash
head -n 20 file.txt
```

### 显示文件前100字节

```bash
head -c 100 file.bin
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
