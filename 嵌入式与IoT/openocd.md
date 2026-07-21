---
{
  "cmd_name": "openocd",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "包管理器安装，如 sudo apt install openocd",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "st-flash",
    "avrdude"
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

# openocd

> 开源片上调试器

## 安装

```bash
包管理器安装，如 sudo apt install openocd
```

## 用法

```
openocd [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 配置文件 |
| `-c` | 命令 |
| `-d` | 调试级别 |

## 示例

### 示例 1: 连接 STM32

```bash
openocd -f interface/stlink.cfg -f target/stm32f4x.cfg
```

### 示例 2: 烧录

```bash
openocd -f interface/stlink.cfg -c 'program firmware.bin verify reset exit'
```

## 关联命令

- [[st-flash]]
- [[avrdude]]

## 风险提示

> ⚠️ **MEDIUM**: 调试操作可读写内存，请确认目标设备

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
