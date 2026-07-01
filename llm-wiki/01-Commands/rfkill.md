---
{
  "cmd_name": "rfkill",
  "cmd_category": "硬件/网络硬件",
  "cmd_dimension": "网络硬件",
  "cmd_install": "多数 Linux 预装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "iw",
    "bluetoothctl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/network.yaml"
}
---

# rfkill

> 无线设备软开关管理

## 安装

```bash
多数 Linux 预装
```

## 用法

```
rfkill [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `list` | 列出 |
| `block` | 禁用 |
| `unblock` | 启用 |
| `event` | 事件 |

## 示例

### 示例 1: 列出无线设备状态

```bash
rfkill list
```

### 示例 2: 启用 WiFi

```bash
sudo rfkill unblock wifi
```

## 关联命令

- [[iw]]
- [[bluetoothctl]]

## 所属维度

[[网络硬件-MOC|硬件/网络硬件]]
