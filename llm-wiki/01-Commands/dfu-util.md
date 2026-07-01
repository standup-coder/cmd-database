---
{
  "cmd_name": "dfu-util",
  "cmd_category": "硬件/嵌入式与IoT",
  "cmd_dimension": "嵌入式与IoT",
  "cmd_install": "包管理器安装，如 sudo apt install dfu-util",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "esptool",
    "st-flash"
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

# dfu-util

> USB DFU 设备固件更新

## 安装

```bash
包管理器安装，如 sudo apt install dfu-util
```

## 用法

```
dfu-util [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 列出 |
| `-D` | 下载固件 |
| `-U` | 上传 |
| `-a` | 接口 |

## 示例

### 示例 1: 列出 DFU 设备

```bash
dfu-util -l
```

### 示例 2: 下载固件

```bash
dfu-util -a 0 -D firmware.dfu
```

## 关联命令

- [[esptool]]
- [[st-flash]]

## 风险提示

> ⚠️ **MEDIUM**: 固件更新失败可能使设备无法启动

## 所属维度

[[嵌入式与IoT-MOC|硬件/嵌入式与IoT]]
