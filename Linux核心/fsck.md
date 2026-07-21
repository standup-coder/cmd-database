---
{
  "cmd_name": "fsck",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mkfs",
    "tune2fs"
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

# fsck

> 检查并修复文件系统

## 用法

```
fsck [OPTIONS] DEVICE
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | 自动回答 yes |
| `-n` | 只检查不修复 |
| `-t` | 指定文件系统类型 |

## 示例

### 示例 1: 只检查不修复

```bash
sudo fsck -n /dev/sda1
```

### 示例 2: 自动修复错误

```bash
sudo fsck -y /dev/sda1
```

## 关联命令

- [[mkfs]]
- [[tune2fs]]

## 风险提示

> ⚠️ **CRITICAL**: fsck 会修改文件系统结构，操作前请卸载分区并备份

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
