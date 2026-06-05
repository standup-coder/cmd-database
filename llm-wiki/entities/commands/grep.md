---
cmd_name: grep
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "在文件中搜索文本模式"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/common.yaml
---


# grep

> 在文件中搜索文本模式

## 用法

```
grep [选项] 模式 [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略大小写 |
| `-r, -R` | 递归搜索目录 |
| `-n` | 显示行号 |
| `-v` | 反向匹配（显示不匹配的行） |
| `-E` | 使用扩展正则表达式 |
| `-w` | 匹配整个单词 |
| `-c` | 只显示匹配的行数 |
| `-l` | 只显示匹配的文件名 |

## 示例

### 示例 1: 在系统日志中搜索包含error的行

```bash
grep 'error' /var/log/syslog
```

### 示例 2: 递归搜索当前目录下所有包含TODO的文件（忽略大小写）

```bash
grep -ri 'TODO' .
```

### 示例 3: 使用正则表达式搜索IP地址

```bash
grep -E '192\.168\.[0-9]+\.[0-9]+' access.log
```

## 参考链接

- [https://www.gnu.org/software/grep/manual/](https://www.gnu.org/software/grep/manual/)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
