---
{
  "cmd_name": "hddtemp",
  "cmd_category": "硬件/传感器与电源",
  "cmd_dimension": "传感器与电源",
  "cmd_install": "包管理器安装，如 sudo apt install hddtemp",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "smartctl",
    "sensors"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/sensors.yaml"
}
---

# hddtemp

> 显示硬盘温度

## 安装

```bash
包管理器安装，如 sudo apt install hddtemp
```

## 用法

```
hddtemp [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 单位 |
| `-n` | 数值输出 |
| `-d` | 守护进程 |

## 示例

### 示例 1: 查看 sda 温度

```bash
sudo hddtemp /dev/sda
```

### 示例 2: 只输出温度值

```bash
hddtemp -n /dev/sda
```

## 关联命令

- [[smartctl]]
- [[sensors]]

## 所属维度

[[传感器与电源-MOC|硬件/传感器与电源]]
