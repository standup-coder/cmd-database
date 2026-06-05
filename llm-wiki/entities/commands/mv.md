---
cmd_name: mv
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "移动或重命名文件和目录"
cmd_level: intermediate
cmd_related:
- cp
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/os/common.yaml
---


# mv

> 移动或重命名文件和目录

## 用法

```
mv [选项] 源文件 目标文件
```

```
mv [选项] 源文件... 目标目录
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 覆盖前提示确认 |
| `-f` | 强制覆盖 |
| `-n` | 不覆盖已存在的文件 |
| `-v` | 显示详细信息 |

## 示例

### 示例 1: 重命名文件

```bash
mv oldname.txt newname.txt
```

### 示例 2: 移动文件到/tmp目录

```bash
mv file.txt /tmp/
```

### 示例 3: 交互式移动所有txt文件

```bash
mv -i *.txt /backup/
```

## 关联命令

- [[cp]]

## 风险提示

> ⚠️ **MEDIUM**: 移动文件会改变文件位置，可能导致依赖该路径的程序出错

## 参考链接

- [https://man7.org/linux/man-pages/man1/mv.1.html](https://man7.org/linux/man-pages/man1/mv.1.html)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
