---
{
  "cmd_name": "mkdir",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "rmdir",
    "cd"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# mkdir

> 创建目录

## 用法

```
mkdir [OPTIONS] DIRECTORY...
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 递归创建父目录 |
| `-v` | 显示创建过程 |
| `-m` | 设置权限模式 |

## 示例

### 示例 1: 递归创建目录

```bash
mkdir -p /tmp/a/b
```

### 示例 2: 创建权限为 700 的目录

```bash
mkdir -m 700 mydir
```

## 关联命令

- [[rmdir]]
- [[cd]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
