---
{
  "cmd_name": "picocom",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "包管理器安装，如 sudo apt install picocom",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "minicom",
    "screen"
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

# picocom

> 极简串口终端

## 安装

```bash
包管理器安装，如 sudo apt install picocom
```

## 用法

```
picocom [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--baud` | 波特率 |
| `--flow` | 流控 |
| `--imap` |  |
| `--omap` |  |

## 示例

### 示例 1: 连接串口

```bash
picocom -b 115200 /dev/ttyUSB0
```

### 示例 2: 回显模式

```bash
picocom --echo -b 9600 /dev/ttyUSB0
```

## 关联命令

- [[minicom]]

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
