---
{
  "cmd_name": "bluetoothctl",
  "cmd_category": "硬件/网络硬件",
  "cmd_dimension": "网络硬件",
  "cmd_install": "随 bluez 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "rfkill",
    "hciconfig"
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

# bluetoothctl

> 蓝牙设备管理交互式工具

## 安装

```bash
随 bluez 安装
```

## 用法

```
bluetoothctl [OPTIONS] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `scan on` | 启用蓝牙扫描 |
| `pair` | 配对设备 |
| `connect` | 连接设备 |
| `trust` | 信任设备 |
| `remove` | 删除设备 |

## 示例

### 示例 1: 扫描蓝牙设备

```bash
bluetoothctl scan on
```

### 示例 2: 配对设备

```bash
bluetoothctl pair 00:11:22:33:44:55
```

## 关联命令

- [[rfkill]]

## 所属维度

[[网络硬件-MOC|硬件/网络硬件]]
