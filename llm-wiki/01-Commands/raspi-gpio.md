---
{
  "cmd_name": "raspi-gpio",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "Raspberry Pi OS 预装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gpio",
    "i2cset"
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

# raspi-gpio

> 树莓派 GPIO 工具

## 安装

```bash
Raspberry Pi OS 预装
```

## 用法

```
raspi-gpio [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `get` | 读取 |
| `set` | 设置 |
| `func` | 功能 |

## 示例

### 示例 1: 读取 GPIO 25

```bash
raspi-gpio get 25
```

### 示例 2: 设置 GPIO25 输出高

```bash
raspi-gpio set 25 op dh
```

## 关联命令

- [[gpio]]
- [[i2cset]]

## 风险提示

> ⚠️ **MEDIUM**: 同样需要注意外设电平保护

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
