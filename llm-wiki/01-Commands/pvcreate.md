---
{
  "cmd_name": "pvcreate",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "vgcreate",
    "lvcreate"
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

# pvcreate

> 初始化物理卷（LVM）

## 用法

```
pvcreate [OPTIONS] DEVICE
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 强制 |
| `-y` | 自动 yes |
| `--dataalignment` | 对齐 |

## 示例

### 示例 1: 将磁盘初始化为物理卷

```bash
sudo pvcreate /dev/sdb
```

### 示例 2: 强制初始化

```bash
sudo pvcreate -f /dev/sdc1
```

## 关联命令

- [[vgcreate]]
- [[lvcreate]]

## 风险提示

> ⚠️ **CRITICAL**: pvcreate 会覆盖设备上的分区信息，请确认无重要数据

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
