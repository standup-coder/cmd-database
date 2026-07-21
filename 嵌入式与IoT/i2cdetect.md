---
{
  "cmd_name": "i2cdetect",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "包管理器安装 i2c-tools",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "i2cget",
    "i2cset"
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

# i2cdetect

> 扫描 I2C 总线上的设备

## 安装

```bash
包管理器安装 i2c-tools
```

## 用法

```
i2cdetect [OPTIONS] BUS
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | 自动 yes |
| `-r` | 读扫描 |
| `-q` | 快速扫描 |
| `-a` | 扫描全部地址 |

## 示例

### 示例 1: 扫描 I2C-1

```bash
sudo i2cdetect -y 1
```

### 示例 2: 列出 I2C 总线

```bash
sudo i2cdetect -l
```

## 关联命令

- [[i2cget]]
- [[i2cset]]

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
