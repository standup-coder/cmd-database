---
{
  "cmd_name": "chrt",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "nice",
    "taskset"
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

# chrt

> 设置实时调度策略

## 用法

```
chrt [OPTIONS] [PRIO] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | FIFO |
| `-r` | RR |
| `-o` | OTHER |
| `-p` | 修改 PID |

## 示例

### 示例 1: 以 FIFO 优先级 99 运行

```bash
sudo chrt -f 99 ./app
```

### 示例 2: 查看 PID 调度策略

```bash
chrt -p 1234
```

## 关联命令

- [[nice]]
- [[taskset]]

## 风险提示

> ⚠️ **HIGH**: 实时调度可能饿死其他进程，需谨慎使用

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
