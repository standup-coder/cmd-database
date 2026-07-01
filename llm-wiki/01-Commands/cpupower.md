---
{
  "cmd_name": "cpupower",
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
    "perf"
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

# cpupower

> CPU 频率与空闲状态管理

## 安装

```bash
linux-tools-common 包
```

## 用法

```
cpupower [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `frequency-info` | 频率信息 |
| `frequency-set` | 设置频率 |
| `idle-info` | 空闲状态 |
| `set` | 策略 |

## 示例

### 示例 1: 查看 CPU 频率策略

```bash
cpupower frequency-info
```

### 示例 2: 设置为性能模式

```bash
sudo cpupower frequency-set -g performance
```

## 关联命令

- [[turbostat]]
- [[perf]]

## 风险提示

> ⚠️ **MEDIUM**: 强制设置频率策略可能影响功耗和散热

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
