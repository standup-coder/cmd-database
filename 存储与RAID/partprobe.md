---
{
  "cmd_name": "partprobe",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "parted",
    "fdisk"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/storage.yaml"
}
---

# partprobe

> 通知内核分区表变化

## 用法

```
partprobe [OPTIONS] [DEVICE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 不更新 |
| `-s` | 显示摘要 |

## 示例

### 示例 1: 通知所有设备

```bash
sudo partprobe
```

### 示例 2: 通知 sdb

```bash
sudo partprobe /dev/sdb
```

## 关联命令

- [[parted]]
- [[fdisk]]

## 风险提示

> ⚠️ **MEDIUM**: 分区表变更可能影响已挂载文件系统，请确认无冲突

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
