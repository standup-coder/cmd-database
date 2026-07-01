---
{
  "cmd_name": "avrdude",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "包管理器安装，如 sudo apt install avrdude",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "esptool",
    "openocd"
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

# avrdude

> AVR 单片机烧录

## 安装

```bash
包管理器安装，如 sudo apt install avrdude
```

## 用法

```
avrdude [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 芯片 |
| `-c` | 编程器 |
| `-P` | 端口 |
| `-U` | memop |
| `-b` | 波特率 |

## 示例

### 示例 1: 读取 Flash

```bash
avrdude -p m328p -c usbasp -U flash:r:backup.hex:i
```

### 示例 2: 写入 Flash

```bash
avrdude -p m328p -c usbasp -U flash:w:firmware.hex:i
```

## 关联命令

- [[esptool]]
- [[openocd]]

## 风险提示

> ⚠️ **MEDIUM**: 错误的熔丝位设置会锁死芯片

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
