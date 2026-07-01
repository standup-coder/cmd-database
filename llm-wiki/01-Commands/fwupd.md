---
{
  "cmd_name": "fwupd",
  "cmd_category": "硬件/固件与UEFI",
  "cmd_dimension": "固件与UEFI",
  "cmd_install": "包管理器安装 fwupd",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "efibootmgr",
    "flashrom"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/hardware/firmware.yaml"
}
---

# fwupd

> Linux 固件更新守护进程与工具

## 安装

```bash
包管理器安装 fwupd
```

## 用法

```
fwupdmgr [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `get-devices` |  |
| `get-updates` |  |
| `update` |  |
| `refresh` |  |

## 示例

### 示例 1: 列出可更新设备

```bash
fwupdmgr get-devices
```

### 示例 2: 安装可用固件更新

```bash
fwupdmgr update
```

## 关联命令

- [[efibootmgr]]
- [[flashrom]]

## 风险提示

> ⚠️ **HIGH**: 固件更新失败可能导致硬件变砖，请确保电源稳定

## 所属维度

[[固件与UEFI-MOC|硬件/固件与UEFI]]
