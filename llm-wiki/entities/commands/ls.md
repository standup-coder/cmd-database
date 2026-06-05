---
cmd_name: ls
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "列出目录内容"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/common.yaml
---


# ls

> 列出目录内容

## 用法

```
ls [选项] [文件或目录]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 使用长格式列表 |
| `-a` | 显示所有文件（包括隐藏文件） |
| `-h` | 以人类可读的格式显示文件大小 |
| `-R` | 递归列出子目录 |
| `-t` | 按修改时间排序 |
| `-r` | 反向排序 |

## 示例

### 示例 1: 以长格式列出所有文件，包括隐藏文件

```bash
ls -la
```

### 示例 2: 以人类可读格式列出/var/log目录

```bash
ls -lh /var/log
```

### 示例 3: 按时间反向排序列出文件

```bash
ls -ltr
```

## 参考链接

- [https://man7.org/linux/man-pages/man1/ls.1.html](https://man7.org/linux/man-pages/man1/ls.1.html)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
