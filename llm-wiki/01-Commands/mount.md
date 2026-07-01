---
{
  "cmd_name": "mount",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "umount",
    "lsblk"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# mount

> 挂载文件系统

## 用法

```
mount [OPTIONS] [DEVICE] [DIRECTORY]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t` | 指定文件系统类型 |
| `-o` | 指定挂载选项 |
| `-a` | 挂载 /etc/fstab 中所有设备 |

## 示例

### 示例 1: 挂载分区到 /mnt

```bash
sudo mount /dev/sdb1 /mnt
```

### 示例 2: 挂载 /etc/fstab 中定义的所有设备

```bash
sudo mount -a
```

## 关联命令

- [[umount]]
- [[lsblk]]

## 风险提示

> ⚠️ **HIGH**: 挂载到错误目录会覆盖现有数据，请确认目标目录为空或已备份

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
