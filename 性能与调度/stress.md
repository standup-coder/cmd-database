---
{
  "cmd_name": "stress",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "包管理器安装，如 sudo apt install stress",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "stress-ng",
    "s-tui"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/hardware/perf.yaml"
}
---

# stress

> 简单的系统压力测试

## 安装

```bash
包管理器安装，如 sudo apt install stress
```

## 用法

```
stress [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--cpu` | CPU 数 |
| `--io` | IO 线程 |
| `--vm` | 内存 workers |
| `--timeout` |  |

## 示例

### 示例 1: CPU 压测 60 秒

```bash
stress --cpu 4 --timeout 60s
```

### 示例 2: 内存压测

```bash
stress --vm 2 --vm-bytes 1G --timeout 60s
```

## 关联命令

- [[stress-ng]]
- [[s-tui]]

## 风险提示

> ⚠️ **HIGH**: 压测会消耗系统资源，可能导致响应变慢或 OOM

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
