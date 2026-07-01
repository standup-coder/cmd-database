---
{
  "cmd_name": "lvcreate",
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
    "pvcreate"
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

# lvcreate

> 创建逻辑卷（LVM）

## 用法

```
lvcreate [OPTIONS] -n NAME -L SIZE VOLUME_GROUP
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 逻辑卷名 |
| `-L` | 指定大小 |
| `-l` | 指定 LE 数 |
| `-s` | 创建快照 |

## 示例

### 示例 1: 在 vg0 上创建 100G 逻辑卷

```bash
sudo lvcreate -n lv0 -L 100G vg0
```

### 示例 2: 创建快照

```bash
sudo lvcreate -s -n snap -L 10G /dev/vg0/lv0
```

## 关联命令

- [[vgcreate]]
- [[pvcreate]]

## 风险提示

> ⚠️ **HIGH**: 逻辑卷操作影响存储布局，请确认大小和卷组

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
