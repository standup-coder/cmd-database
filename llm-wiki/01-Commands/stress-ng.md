---
{
  "cmd_name": "stress-ng",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "包管理器安装，如 sudo apt install stress-ng",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "stress",
    "fio"
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

# stress-ng

> 更全面的系统压力测试

## 安装

```bash
包管理器安装，如 sudo apt install stress-ng
```

## 用法

```
stress-ng [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--cpu` | 8 |
| `--disk` | 4 |
| `--vm` | 4 |
| `--timeout` | 60s |
| `--metrics-brief` |  |

## 示例

### 示例 1: CPU 压测

```bash
stress-ng --cpu 8 --timeout 60s --metrics-brief
```

### 示例 2: 顺序 IO 压测

```bash
stress-ng --class io --sequential 4 --timeout 60s
```

## 关联命令

- [[stress]]
- [[fio]]

## 风险提示

> ⚠️ **HIGH**: stress-ng 有大量测试，错误使用会压垮系统

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
