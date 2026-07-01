---
{
  "cmd_name": "parted",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "fdisk",
    "mkfs"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# parted

> 高级磁盘分区工具

## 用法

```
parted [OPTIONS] [DEVICE] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 列出分区 |
| `mklabel` | 创建分区表 |
| `mkpart` | 创建分区 |

## 示例

### 示例 1: 列出所有分区

```bash
sudo parted -l
```

### 示例 2: 创建 GPT 分区表

```bash
sudo parted /dev/sdb mklabel gpt
```

## 关联命令

- [[fdisk]]
- [[mkfs]]

## 风险提示

> ⚠️ **CRITICAL**: 分区操作会清除数据，请确认目标磁盘并已备份

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
