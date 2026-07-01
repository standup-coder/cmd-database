---
{
  "cmd_name": "tlp",
  "cmd_category": "硬件/传感器与电源",
  "cmd_dimension": "传感器与电源",
  "cmd_install": "包管理器安装，如 sudo apt install tlp",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "powertop",
    "thermald"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/sensors.yaml"
}
---

# tlp

> Linux 笔记本电源管理

## 安装

```bash
包管理器安装，如 sudo apt install tlp
```

## 用法

```
tlp [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 启动 |
| `stat` | 状态 |
| `bat` | 电池模式 |
| `ac` | 电源模式 |

## 示例

### 示例 1: 启动 TLP

```bash
sudo tlp start
```

### 示例 2: 切换到电池模式

```bash
sudo tlp bat
```

## 关联命令

- [[powertop]]
- [[thermald]]

## 风险提示

> ⚠️ **MEDIUM**: 电源配置错误可能导致性能下降或 USB 掉线

## 所属维度

[[传感器与电源-MOC|硬件/传感器与电源]]
