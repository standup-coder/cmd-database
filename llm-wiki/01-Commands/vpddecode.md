---
{
  "cmd_name": "vpddecode",
  "cmd_category": "硬件/固件与UEFI",
  "cmd_dimension": "固件与UEFI",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dmidecode",
    "biosdecode"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/firmware.yaml"
}
---

# vpddecode

> 解析 VPD（重要产品数据）

## 用法

```
vpddecode [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 只显示系统 |
| `-b` | 只显示 baseboard |

## 示例

### 示例 1: 显示 VPD

```bash
vpddecode
```

### 示例 2: 以 root 解析 VPD

```bash
sudo vpddecode
```

## 关联命令

- [[dmidecode]]
- [[biosdecode]]

## 所属维度

[[固件与UEFI-MOC|硬件/固件与UEFI]]
