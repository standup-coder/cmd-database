---
cmd_name: cat
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "连接文件并输出到标准输出"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/common.yaml
---


# cat

> 连接文件并输出到标准输出

## 用法

```
cat [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 对输出的所有行编号 |
| `-b` | 对非空行编号 |
| `-s` | 压缩连续的空行为一行 |
| `-E` | 在每行末尾显示$符号 |
| `-T` | 将TAB字符显示为^I |

## 示例

### 示例 1: 显示文件内容

```bash
cat file.txt
```

### 示例 2: 合并多个文件

```bash
cat file1.txt file2.txt > combined.txt
```

### 示例 3: 显示文件内容并添加行号

```bash
cat -n script.sh
```

## 参考链接

- [https://man7.org/linux/man-pages/man1/cat.1.html](https://man7.org/linux/man-pages/man1/cat.1.html)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
