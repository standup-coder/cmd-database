---
{
  "cmd_name": "thermald",
  "cmd_category": "硬件/传感器与电源",
  "cmd_dimension": "传感器与电源",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tlp",
    "sensors"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/sensors.yaml"
}
---

# thermald

> Intel 平台热量管理守护进程

## 用法

```
thermald [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--no-daemon` |  |
| `--dbus-enable` |  |
| `--config-file` |  |

## 示例

### 示例 1: 前台启动

```bash
sudo thermald --no-daemon
```

### 示例 2: 系统服务启动

```bash
sudo systemctl start thermald
```

## 关联命令

- [[tlp]]
- [[sensors]]

## 风险提示

> ⚠️ **MEDIUM**: thermald 会主动调节 CPU，配置错误可能导致降频

## 所属维度

[[传感器与电源-MOC|硬件/传感器与电源]]
