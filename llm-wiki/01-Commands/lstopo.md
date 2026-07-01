---
{
  "cmd_name": "lstopo",
  "cmd_category": "硬件/系统信息",
  "cmd_dimension": "系统信息",
  "cmd_install": "随 hwloc 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hwloc",
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

# lstopo

> 图形/文本化硬件拓扑查看器

## 安装

```bash
随 hwloc 安装
```

## 用法

```
lstopo [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 详细 |
| `--no-io` |  |
| `--of` | png |
| `--output-format` |  |

## 示例

### 示例 1: 文本显示拓扑

```bash
lstopo
```

### 示例 2: 导出拓扑图

```bash
lstopo topology.png
```

## 关联命令

- [[hwloc]]
- [[numactl]]

## 所属维度

[[系统信息-MOC|硬件/系统信息]]
