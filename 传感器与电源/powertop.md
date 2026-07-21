---
{
  "cmd_name": "powertop",
  "cmd_category": "硬件/传感器与电源",
  "cmd_dimension": "传感器与电源",
  "cmd_install": "包管理器安装，如 sudo apt install powertop",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tlp",
    "sensors"
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

# powertop

> 电源消耗与节能诊断

## 安装

```bash
包管理器安装，如 sudo apt install powertop
```

## 用法

```
powertop [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--calibrate` | 校准 |
| `--html` | 生成报告 |
| `--auto-tune` | 自动调优 |

## 示例

### 示例 1: 交互式电源分析

```bash
powertop
```

### 示例 2: 自动优化电源

```bash
sudo powertop --auto-tune
```

## 关联命令

- [[tlp]]
- [[sensors]]

## 风险提示

> ⚠️ **MEDIUM**: --auto-tune 会修改设备省电设置，可能影响性能或外设

## 所属维度

[[传感器与电源-MOC|硬件/传感器与电源]]
