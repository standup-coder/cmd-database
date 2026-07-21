---
{
  "cmd_name": "st-flash",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "参考 https://github.com/stlink-org/stlink",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openocd",
    "dfu-util"
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

# st-flash

> STM32 ST-Link 烧录工具

## 安装

```bash
参考 https://github.com/stlink-org/stlink
```

## 用法

```
st-flash [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `write` | 写入 |
| `read` | 读取 |
| `erase` | 擦除 |
| `reset` |  |

## 示例

### 示例 1: 烧录到 Flash 起始地址

```bash
st-flash write firmware.bin 0x8000000
```

### 示例 2: 擦除芯片

```bash
st-flash erase
```

## 关联命令

- [[openocd]]
- [[dfu-util]]

## 风险提示

> ⚠️ **MEDIUM**: 擦除会清空 Flash

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
