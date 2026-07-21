---
{
  "cmd_name": "cset",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "包管理器安装 cpuset",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "taskset",
    "numactl"
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

# cset

> cpuset 资源隔离工具

## 安装

```bash
包管理器安装 cpuset
```

## 用法

```
cset [SUBCOMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `set` | 创建 cpuset |
| `proc` | 移动进程 |
| `shield` | 隔离 CPU |

## 示例

### 示例 1: 隔离 CPU 2-3

```bash
sudo cset shield --cpu=2-3
```

### 示例 2: 移动进程到 user cpuset

```bash
sudo cset proc --move --pid=1234 --set=user
```

## 关联命令

- [[taskset]]
- [[numactl]]

## 风险提示

> ⚠️ **MEDIUM**: cpuset 隔离错误会限制进程可用资源

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
