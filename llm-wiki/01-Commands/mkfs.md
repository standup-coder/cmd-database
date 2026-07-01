---
{
  "cmd_name": "mkfs",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "fsck",
    "parted"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# mkfs

> 创建文件系统

## 用法

```
mkfs [OPTIONS] [-t TYPE] DEVICE
```

## 参数

| Flag | Description |
|------|-------------|
| `-t` | 指定类型 |
| `-L` | 设置卷标 |
| `-V` | 详细输出 |

## 示例

### 示例 1: 格式化为 ext4

```bash
sudo mkfs -t ext4 /dev/sdb1
```

### 示例 2: 格式化为 XFS 并设置卷标

```bash
sudo mkfs.xfs -L data /dev/sdc1
```

## 关联命令

- [[fsck]]
- [[parted]]

## 风险提示

> ⚠️ **CRITICAL**: mkfs 会清除设备上所有数据，请确认目标分区正确

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
