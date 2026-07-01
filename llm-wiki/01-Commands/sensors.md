---
{
  "cmd_name": "sensors",
  "cmd_category": "硬件/传感器与电源",
  "cmd_dimension": "传感器与电源",
  "cmd_install": "包管理器安装 lm-sensors",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "powertop",
    "hddtemp"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/sensors.yaml"
}
---

# sensors

> 读取硬件传感器数据（lm-sensors）

## 安装

```bash
包管理器安装 lm-sensors
```

## 用法

```
sensors [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 原始值 |
| `-f` | 华氏度 |
| `-A` | 平均 |
| `-s` | 计算 |

## 示例

### 示例 1: 显示 CPU/主板温度

```bash
sensors
```

### 示例 2: 显示原始传感器值

```bash
sensors -u coretemp-isa-0000
```

## 关联命令

- [[powertop]]
- [[hddtemp]]

## 所属维度

[[传感器与电源-MOC|硬件/传感器与电源]]
