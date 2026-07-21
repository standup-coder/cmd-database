---
{
  "cmd_name": "lsblk",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "df",
    "fdisk"
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

# lsblk

> 列出块设备信息

## 用法

```
lsblk [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 显示文件系统 |
| `-m` | 显示权限信息 |
| `-o` | 指定输出列 |

## 示例

### 示例 1: 列出块设备树

```bash
lsblk
```

### 示例 2: 显示文件系统和 UUID

```bash
lsblk -f
```

## 关联命令

- [[df]]
- [[fdisk]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
