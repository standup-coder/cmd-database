---
{
  "cmd_name": "i2cset",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "随 i2c-tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "i2cget",
    "i2cdetect"
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

# i2cset

> 写入 I2C 设备寄存器

## 安装

```bash
随 i2c-tools 安装
```

## 用法

```
i2cset [OPTIONS] BUS CHIP-ADDRESS DATA-ADDRESS VALUE
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | 自动 yes |
| `-m` | 掩码 |

## 示例

### 示例 1: 写入 0xFF 到寄存器

```bash
sudo i2cset -y 1 0x50 0x00 0xFF
```

### 示例 2: 使用掩码写入低 4 位

```bash
sudo i2cset -y -m 0x0F 1 0x50 0x00 0x05
```

## 关联命令

- [[i2cget]]
- [[i2cdetect]]

## 风险提示

> ⚠️ **MEDIUM**: 错误写入可能损坏 I2C 设备配置

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
