---
{
  "cmd_name": "i2cget",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "随 i2c-tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "i2cset",
    "i2cdetect"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/embedded.yaml"
}
---

# i2cget

> 读取 I2C 设备寄存器

## 安装

```bash
随 i2c-tools 安装
```

## 用法

```
i2cget [OPTIONS] BUS CHIP-ADDRESS DATA-ADDRESS
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | 自动 yes |
| `-f` | 强制访问 |

## 示例

### 示例 1: 读取 I2C 设备 0x50 的 0x00 寄存器

```bash
sudo i2cget -y 1 0x50 0x00
```

### 示例 2: 强制读取 I2C 寄存器

```bash
sudo i2cget -y -f 1 0x50 0x00
```

## 关联命令

- [[i2cset]]
- [[i2cdetect]]

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
