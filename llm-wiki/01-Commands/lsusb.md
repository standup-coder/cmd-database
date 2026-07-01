---
{
  "cmd_name": "lsusb",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lspci",
    "dmesg"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# lsusb

> 列出 USB 设备

## 用法

```
lsusb [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 详细 |
| `-t` | 树状 |
| `-s` | 指定总线/设备 |

## 示例

### 示例 1: 列出 USB 设备

```bash
lsusb
```

### 示例 2: 查看罗技设备详情

```bash
lsusb -v -d 046d:
```

## 关联命令

- [[lspci]]
- [[dmesg]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
