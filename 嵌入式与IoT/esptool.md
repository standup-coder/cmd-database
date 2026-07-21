---
{
  "cmd_name": "esptool",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "pip install esptool",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "minicom",
    "dfu-util"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/embedded.yaml"
}
---

# esptool

> ESP8266/ESP32 烧录工具

## 安装

```bash
pip install esptool
```

## 用法

```
esptool.py [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `--port` | 串口 |
| `--baud` | 波特率 |
| `flash_id` |  |
| `erase_flash` |  |
| `write_flash` |  |

## 示例

### 示例 1: 读取 Flash ID

```bash
esptool.py --port /dev/ttyUSB0 flash_id
```

### 示例 2: 烧录固件

```bash
esptool.py --port /dev/ttyUSB0 write_flash 0x0 firmware.bin
```

## 关联命令

- [[minicom]]
- [[dfu-util]]

## 风险提示

> ⚠️ **MEDIUM**: 擦除/烧写 Flash 会清空设备，请确认端口和地址

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
