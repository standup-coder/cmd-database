---
cmd_name: rm
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "删除文件或目录"
cmd_level: advanced
cmd_related:
- mv
cmd_tags:
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/os/common.yaml
---


# rm

> 删除文件或目录

## 用法

```
rm [选项] 文件或目录...
```

## 参数

| Flag | Description |
|------|-------------|
| `-r, -R` | 递归删除目录及其内容 |
| `-f` | 强制删除，忽略不存在的文件，不提示确认 |
| `-i` | 删除前提示确认 |
| `-v` | 显示详细信息 |

## 示例

### 示例 1: 删除单个文件

```bash
rm file.txt
```

### 示例 2: 强制递归删除目录

```bash
rm -rf /tmp/test
```

### 示例 3: 交互式删除所有.log文件

```bash
rm -i *.log
```

## 关联命令

- [[mv]]

## 风险提示

> ⚠️ **CRITICAL**: rm -rf可能导致数据永久丢失，使用前必须仔细确认路径

## 参考链接

- [https://man7.org/linux/man-pages/man1/rm.1.html](https://man7.org/linux/man-pages/man1/rm.1.html)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
