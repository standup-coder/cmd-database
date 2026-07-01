---
{
  "cmd_name": "efivar",
  "cmd_category": "硬件/固件与UEFI",
  "cmd_dimension": "固件与UEFI",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "efibootmgr",
    "mokutil"
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

# efivar

> 读取和写入 UEFI 变量

## 用法

```
efivar [OPTIONS] [NAME]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 列出 |
| `-p` | 打印 |
| `-a` | 追加 |
| `-f` | 文件 |

## 示例

### 示例 1: 列出 UEFI 变量

```bash
efivar -l
```

### 示例 2: 打印启动顺序

```bash
efivar -p -n BootOrder
```

## 关联命令

- [[efibootmgr]]
- [[mokutil]]

## 风险提示

> ⚠️ **HIGH**: 修改 UEFI 变量可能导致启动失败或安全策略变更

## 所属维度

[[固件与UEFI-MOC|硬件/固件与UEFI]]
