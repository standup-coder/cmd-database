---
{
  "cmd_name": "whereis",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "unix"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "which",
    "locate",
    "find"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# whereis

> 定位命令的二进制、源码和手册页文件

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

### 示例 1: 查找python的所有相关文件

```bash
whereis python
```

### 示例 2: 只查找python二进制文件

```bash
whereis -b python
```

## 关联命令

- [[which]]
- [[locate]]
- [[find]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
