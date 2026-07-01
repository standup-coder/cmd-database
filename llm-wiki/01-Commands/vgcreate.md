---
{
  "cmd_name": "vgcreate",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "pvcreate",
    "lvcreate"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# vgcreate

> 创建卷组（LVM）

## 用法

```
vgcreate [OPTIONS] VOLUME_GROUP PHYSICAL_VOLUME...
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 指定物理扩展大小 |
| `-v` | 详细输出 |

## 示例

### 示例 1: 创建卷组 vg0

```bash
sudo vgcreate vg0 /dev/sdb /dev/sdc
```

### 示例 2: 指定 PE 大小

```bash
sudo vgcreate -s 16M vg1 /dev/sdd
```

## 关联命令

- [[pvcreate]]
- [[lvcreate]]

## 风险提示

> ⚠️ **HIGH**: 创建卷组会占用物理卷，请确认目标设备

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
