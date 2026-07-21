---
{
  "cmd_name": "taskset",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "numactl",
    "chrt"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/perf.yaml"
}
---

# taskset

> 设置或查看进程 CPU 亲和性

## 用法

```
taskset [OPTIONS] [MASK | -c LIST] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | CPU 列表 |
| `-p` | 修改现有 PID |
| `-a` | 所有线程 |

## 示例

### 示例 1: 绑定到 CPU 0

```bash
taskset -c 0 ./app
```

### 示例 2: 修改 PID 1234 亲和性

```bash
taskset -pc 0-3 1234
```

## 关联命令

- [[numactl]]
- [[chrt]]

## 风险提示

> ⚠️ **MEDIUM**: 错误的亲和性会降低性能或导致调度不均

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
