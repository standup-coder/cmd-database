---
cmd_name: find
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "在目录树中搜索文件"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/os/common.yaml
---


# find

> 在目录树中搜索文件

## 用法

```
find [路径...] [表达式]
```

## 参数

| Flag | Description |
|------|-------------|
| `-name pattern` | 按文件名搜索 |
| `-type [f\|d\|l]` | 按类型搜索（f:文件, d:目录, l:符号链接） |
| `-mtime n` | 按修改时间搜索（n天前） |
| `-size n` | 按文件大小搜索 |
| `-exec command {} \;` | 对找到的文件执行命令 |
| `-delete` | 删除找到的文件 |

## 示例

### 示例 1: 在当前目录下查找所有.log文件

```bash
find . -name '*.log'
```

### 示例 2: 删除/tmp下7天前的文件

```bash
find /tmp -type f -mtime +7 -delete
```

### 示例 3: 查找大于100MB的文件

```bash
find . -type f -size +100M
```

## 风险提示

> ⚠️ **HIGH**: 使用-delete选项可能误删重要文件，建议先用-print预览

## 参考链接

- [https://man7.org/linux/man-pages/man1/find.1.html](https://man7.org/linux/man-pages/man1/find.1.html)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
