---
{
  "cmd_name": "minicom",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "包管理器安装，如 sudo apt install minicom",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "picocom",
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

# minicom

> 串口通信终端

## 安装

```bash
包管理器安装，如 sudo apt install minicom
```

## 用法

```
minicom [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-D` | 设备 |
| `-b` | 波特率 |
| `-C` | 捕获日志 |
| `-s` | 配置 |

## 示例

### 示例 1: 连接串口

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

### 示例 2: 记录日志

```bash
minicom -C capture.log -D /dev/ttyUSB0
```

## 关联命令

- [[picocom]]

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
