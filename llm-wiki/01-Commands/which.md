---
{
  "cmd_name": "which",
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
    "whereis",
    "type",
    "command"
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

# which

> 查找命令的可执行文件路径

## 用法

```
which [选项] 命令...
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 显示所有匹配路径 |

## 示例

### 示例 1: 查找python可执行文件位置

```bash
which python
```

### 示例 2: 查找所有python路径

```bash
which -a python
```

## 关联命令

- [[whereis]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
