---
{
  "cmd_name": "iw",
  "cmd_category": "硬件/网络硬件",
  "cmd_dimension": "网络硬件",
  "cmd_install": "多数 Linux 预装或包管理器安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "iwconfig",
    "nmcli"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/network.yaml"
}
---

# iw

> 新一代无线设备配置工具

## 安装

```bash
多数 Linux 预装或包管理器安装
```

## 用法

```
iw [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `dev` | 设备 |
| `list` | 列出 |
| `scan` | 扫描 |
| `connect` | 连接 |
| `set` | 设置 |

## 示例

### 示例 1: 列出无线设备

```bash
iw dev
```

### 示例 2: 扫描 WiFi

```bash
sudo iw dev wlan0 scan
```

## 关联命令

- [[iwconfig]]
- [[nmcli]]

## 风险提示

> ⚠️ **MEDIUM**: iw 可直接修改无线接口，请确认操作对象

## 所属维度

[[网络硬件-MOC|硬件/网络硬件]]
