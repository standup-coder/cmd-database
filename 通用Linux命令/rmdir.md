---
{
  "cmd_name": "rmdir",
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
    "rm",
    "mkdir",
    "rm -rf"
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

# rmdir

> 删除空目录

## 用法

```
rmdir [选项] 目录...
```

## 参数

| Flag | Description |
|------|-------------|
| `-p, --parents` | 删除目录及其祖先空目录 |
| `-v, --verbose` | 显示每个被删除的目录 |

## 示例

### 示例 1: 删除空目录

```bash
rmdir emptydir
```

### 示例 2: 删除c、b、a（如果都为空）

```bash
rmdir -p a/b/c
```

## 关联命令

- [[rm]]
- [[mkdir]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
