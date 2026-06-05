---
cmd_name: pwd
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "显示当前工作目录的完整路径"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/common.yaml
---


# pwd

> 显示当前工作目录的完整路径

## 用法

```
pwd [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-L` | 显示逻辑路径（默认） |
| `-P` | 显示物理路径（解析符号链接） |

## 示例

### 示例 1: 显示当前目录

```bash
pwd
```

## 参考链接

- [https://man7.org/linux/man-pages/man1/pwd.1.html](https://man7.org/linux/man-pages/man1/pwd.1.html)

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
