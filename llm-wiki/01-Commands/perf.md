---
{
  "cmd_name": "perf",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "linux-tools-common 包",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "turbostat",
    "strace"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/perf.yaml"
}
---

# perf

> Linux 性能分析工具

## 安装

```bash
linux-tools-common 包
```

## 用法

```
perf [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `top` | 实时热点 |
| `record` | 记录 |
| `report` | 报告 |
| `stat` | 统计 |
| `list` | 事件 |

## 示例

### 示例 1: 实时查看热点函数

```bash
sudo perf top
```

### 示例 2: 记录并分析

```bash
sudo perf record -g ./app && sudo perf report
```

## 关联命令

- [[turbostat]]
- [[strace]]

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
