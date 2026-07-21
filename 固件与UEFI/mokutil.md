---
{
  "cmd_name": "mokutil",
  "cmd_category": "硬件/固件与UEFI",
  "cmd_dimension": "固件与UEFI",
  "cmd_install": "包管理器安装 mokutil",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "efibootmgr",
    "fwupd"
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

# mokutil

> 管理 UEFI Secure Boot MOK

## 安装

```bash
包管理器安装 mokutil
```

## 用法

```
mokutil [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--sb-state` |  |
| `--list-enrolled` |  |
| `--import` |  |
| `--delete` |  |

## 示例

### 示例 1: 查看 Secure Boot 状态

```bash
mokutil --sb-state
```

### 示例 2: 导入 MOK

```bash
sudo mokutil --import MOK.der
```

## 关联命令

- [[efibootmgr]]
- [[fwupd]]

## 风险提示

> ⚠️ **HIGH**: 错误的 MOK 管理可能导致驱动无法加载或安全策略破坏

## 所属维度

[[固件与UEFI-MOC|硬件/固件与UEFI]]
