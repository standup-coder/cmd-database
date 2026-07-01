---
{
  "cmd_name": "gpio",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "包管理器安装 gpiod",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "i2cset",
    "raspi-gpio"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/embedded.yaml"
}
---

# gpio

> Linux GPIO 命令行工具（libgpiod）

## 安装

```bash
包管理器安装 gpiod
```

## 用法

```
gpio [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `info` | 信息 |
| `get` | 读取 |
| `set` | 设置 |
| `find` | 查找 |

## 示例

### 示例 1: 列出 GPIO 线和芯片

```bash
gpioinfo
```

### 示例 2: 设置 GPIO 25 为高

```bash
gpioset gpiochip0 25=1
```

## 关联命令

- [[i2cset]]
- [[raspi-gpio]]

## 风险提示

> ⚠️ **MEDIUM**: GPIO 控制硬件，错误电平可能损坏外设

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
