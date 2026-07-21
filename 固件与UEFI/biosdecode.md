---
{
  "cmd_name": "biosdecode",
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
    "vpddecode"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/firmware.yaml"
}
---

# biosdecode

> 解析 BIOS 信息

## 用法

```
biosdecode [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 转储 |
| `-h` | 帮助 |

## 示例

### 示例 1: 解析 BIOS

```bash
biosdecode
```

### 示例 2: 以 root 解析 BIOS

```bash
sudo biosdecode
```

## 关联命令

- [[dmidecode]]
- [[vpddecode]]

## 所属维度

[[固件与UEFI-MOC|硬件/固件与UEFI]]
