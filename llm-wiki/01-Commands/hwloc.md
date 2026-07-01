---
{
  "cmd_name": "hwloc",
  "cmd_category": "硬件/系统信息",
  "cmd_dimension": "系统信息",
  "cmd_install": "包管理器安装，如 sudo apt install hwloc",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lstopo",
    "numactl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/info.yaml"
}
---

# hwloc

> 硬件拓扑抽象层工具

## 安装

```bash
包管理器安装，如 sudo apt install hwloc
```

## 用法

```
hwloc [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--objects` |  |
| `--no-io` |  |
| `--of` | xml\|txt |

## 示例

### 示例 1: 显示硬件拓扑

```bash
hwloc-ls
```

### 示例 2: 显示摘要信息

```bash
hwloc-info
```

## 关联命令

- [[lstopo]]
- [[numactl]]

## 所属维度

[[系统信息-MOC|硬件/系统信息]]
