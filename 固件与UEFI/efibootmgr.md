---
{
  "cmd_name": "efibootmgr",
  "cmd_category": "硬件/固件与UEFI",
  "cmd_dimension": "固件与UEFI",
  "cmd_install": "多数 Linux 预装或 efibootmgr 包",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "efivar",
    "grub-install"
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

# efibootmgr

> 管理 UEFI 启动项

## 安装

```bash
多数 Linux 预装或 efibootmgr 包
```

## 用法

```
efibootmgr [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 详细 |
| `-c` | 创建 |
| `-b` | 指定条目 |
| `-B` | 删除 |
| `-n` | 设置下次启动 |

## 示例

### 示例 1: 列出启动项

```bash
efibootmgr -v
```

### 示例 2: 添加启动项

```bash
sudo efibootmgr -c -d /dev/sda -p 1 -l '\EFI\ubuntu\grubx64.efi' -L Ubuntu
```

## 关联命令

- [[efivar]]

## 风险提示

> ⚠️ **CRITICAL**: 删除或修改错误的启动项会导致系统无法启动

## 所属维度

[[固件与UEFI-MOC|硬件/固件与UEFI]]
