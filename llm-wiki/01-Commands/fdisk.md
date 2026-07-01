---
{
  "cmd_name": "fdisk",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "parted",
    "lsblk"
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

# fdisk

> 磁盘分区表管理工具

## 用法

```
fdisk [OPTIONS] DEVICE
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 列出分区表 |
| `-n` | 创建新分区 |
| `-d` | 删除分区 |

## 示例

### 示例 1: 列出所有磁盘分区

```bash
sudo fdisk -l
```

### 示例 2: 进入交互式分区管理

```bash
sudo fdisk /dev/sdb
```

## 关联命令

- [[parted]]
- [[lsblk]]

## 风险提示

> ⚠️ **CRITICAL**: 修改分区表会破坏数据，操作前务必备份并确认磁盘

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
