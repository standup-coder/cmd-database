---
{
  "cmd_name": "lsscsi",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sg_scan",
    "lsblk"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/storage.yaml"
}
---

# lsscsi

> 列出 SCSI/SAS 设备

## 用法

```
lsscsi [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 详细 |
| `-l` | 长格式 |
| `-g` | 显示 sg 设备 |

## 示例

### 示例 1: 列出 SCSI 设备

```bash
lsscsi
```

### 示例 2: 长格式输出

```bash
lsscsi -l
```

## 关联命令

- [[sg_scan]]
- [[lsblk]]

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
