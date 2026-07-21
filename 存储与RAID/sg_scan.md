---
{
  "cmd_name": "sg_scan",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lsscsi",
    "smartctl"
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

# sg_scan

> 扫描 SCSI 通用设备

## 用法

```
sg_scan [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 查询 |
| `-s` | 同步 |

## 示例

### 示例 1: 扫描 sg 设备

```bash
sg_scan
```

### 示例 2: 查询设备信息

```bash
sg_scan -i
```

## 关联命令

- [[lsscsi]]
- [[smartctl]]

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
