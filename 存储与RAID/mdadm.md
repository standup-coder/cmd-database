---
{
  "cmd_name": "mdadm",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "多数 Linux 预装或包管理器安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "lvm",
    "smartctl"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/hardware/storage.yaml"
}
---

# mdadm

> Linux 软 RAID 管理

## 安装

```bash
多数 Linux 预装或包管理器安装
```

## 用法

```
mdadm [OPTIONS] MODE DEVICE
```

## 参数

| Flag | Description |
|------|-------------|
| `--create` | 创建 |
| `--assemble` | 组装 |
| `--detail` | 详情 |
| `--stop` | 停止 |
| `--manage` | 管理 |

## 示例

### 示例 1: 查看 RAID 详情

```bash
sudo mdadm --detail /dev/md0
```

### 示例 2: 创建 RAID1

```bash
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc
```

## 关联命令

- [[smartctl]]

## 风险提示

> ⚠️ **CRITICAL**: 创建/停止 RAID 会擦除或暴露数据，请备份并确认设备

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
