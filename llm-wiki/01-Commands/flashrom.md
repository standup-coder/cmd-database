---
{
  "cmd_name": "flashrom",
  "cmd_category": "硬件/固件与UEFI",
  "cmd_dimension": "固件与UEFI",
  "cmd_install": "包管理器安装 flashrom",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "fwupd",
    "dmidecode"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/hardware/firmware.yaml"
}
---

# flashrom

> 读取/写入/擦除闪存芯片

## 安装

```bash
包管理器安装 flashrom
```

## 用法

```
flashrom [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 读取 |
| `-w` | 写入 |
| `-v` | 校验 |
| `-p` | 编程器 |

## 示例

### 示例 1: 备份主板 BIOS

```bash
flashrom -p internal -r backup.rom
```

### 示例 2: 刷写 BIOS

```bash
flashrom -p internal -w new.rom
```

## 关联命令

- [[fwupd]]
- [[dmidecode]]

## 风险提示

> ⚠️ **CRITICAL**: 刷写 BIOS 失败可能导致主板变砖，请谨慎

## 所属维度

[[固件与UEFI-MOC|硬件/固件与UEFI]]
