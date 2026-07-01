---
{
  "cmd_name": "hdparm",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "smartctl",
    "lsblk"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# hdparm

> 查看和设置 SATA/IDE 硬盘参数

## 用法

```
hdparm [OPTIONS] [DEVICE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-I` | 显示详细信息 |
| `-t` | 缓存读测速 |
| `-T` | 缓存读测速 |
| `-y` | 进入待机 |

## 示例

### 示例 1: 查看硬盘信息

```bash
sudo hdparm -I /dev/sda
```

### 示例 2: 测速

```bash
sudo hdparm -tT /dev/sda
```

## 关联命令

- [[smartctl]]
- [[lsblk]]

## 风险提示

> ⚠️ **MEDIUM**: 设置电源管理或安全擦除参数可能影响硬盘寿命或数据

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
