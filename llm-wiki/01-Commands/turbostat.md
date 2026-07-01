---
{
  "cmd_name": "turbostat",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "linux-tools-common 包",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "perf",
    "cpupower"
  ],
  "cmd_tags": [
    "monitoring",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/perf.yaml"
}
---

# turbostat

> Intel CPU 频率与功耗监控

## 安装

```bash
linux-tools-common 包
```

## 用法

```
turbostat [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--show` | 显示列 |
| `--interval` |  |
| `--Summary` |  |

## 示例

### 示例 1: 监控 CPU

```bash
sudo turbostat
```

### 示例 2: 每秒显示核心频率

```bash
sudo turbostat --interval 1 --show Core,CPU,Avg_MHz,Busy%
```

## 关联命令

- [[perf]]
- [[cpupower]]

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
