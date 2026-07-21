---
{
  "cmd_name": "sensors-detect",
  "cmd_category": "硬件/传感器与电源",
  "cmd_dimension": "传感器与电源",
  "cmd_install": "随 lm-sensors 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sensors",
    "dmidecode"
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

# sensors-detect

> 检测系统中的传感器芯片

## 安装

```bash
随 lm-sensors 安装
```

## 用法

```
sensors-detect [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--auto` | 自动模式 |
| `--interactive` | 交互模式 |

## 示例

### 示例 1: 自动检测传感器

```bash
sudo sensors-detect --auto
```

### 示例 2: 交互式检测传感器

```bash
sudo sensors-detect --interactive
```

## 关联命令

- [[sensors]]
- [[dmidecode]]

## 风险提示

> ⚠️ **MEDIUM**: 自动检测会加载内核模块，请确认系统兼容性

## 所属维度

[[传感器与电源-MOC|硬件/传感器与电源]]
