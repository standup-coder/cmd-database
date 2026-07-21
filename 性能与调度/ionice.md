---
{
  "cmd_name": "ionice",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nice",
    "cgexec"
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

# ionice

> 设置进程 I/O 调度优先级

## 用法

```
ionice [OPTIONS] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 类别 |
| `-n` | 优先级 |
| `-p` | 修改 PID |

## 示例

### 示例 1: 将 PID 设为 idle IO 类

```bash
ionice -c 3 -p 1234
```

### 示例 2: 高优先级 IO 运行

```bash
ionice -c 2 -n 0 ./backup
```

## 关联命令

- [[nice]]
- [[cgexec]]

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
