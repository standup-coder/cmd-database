---
cmd_name: cp
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "复制文件或目录"
cmd_level: intermediate
cmd_related:
- mv
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/os/common.yaml
---


# cp

> 复制文件或目录

## 用法

```
cp [选项] 源文件 目标文件
```

```
cp [选项] 源文件... 目标目录
```

## 参数

| Flag | Description |
|------|-------------|
| `-r, -R` | 递归复制目录 |
| `-i` | 覆盖前提示确认 |
| `-f` | 强制覆盖 |
| `-p` | 保留文件属性 |
| `-a` | 归档模式，等同于-dpR |
| `-v` | 显示详细信息 |

## 示例

### 示例 1: 复制文件

```bash
cp file1.txt file2.txt
```

### 示例 2: 递归复制目录

```bash
cp -r dir1 dir2
```

### 示例 3: 归档复制，保留所有属性

```bash
cp -a /source/* /backup/
```

## 关联命令

- [[mv]]

## 风险提示

> ⚠️ **MEDIUM**: 使用-f可能意外覆盖重要文件

## 参考链接

- [https://man7.org/linux/man-pages/man1/cp.1.html](https://man7.org/linux/man-pages/man1/cp.1.html)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
