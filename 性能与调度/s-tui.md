---
{
  "cmd_name": "s-tui",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "pip install s-tui 或包管理器",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "stress",
    "turbostat"
  ],
  "cmd_tags": [
    "monitoring",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/perf.yaml"
}
---

# s-tui

> 终端 CPU 压力与监控 TUI

## 安装

```bash
pip install s-tui 或包管理器
```

## 用法

```
s-tui [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--no-mouse` |  |
| `--csv` |  |
| `--time` |  |

## 示例

### 示例 1: 启动交互式监控

```bash
s-tui
```

### 示例 2: 记录 300 秒数据

```bash
s-tui --csv stress.csv --time 300
```

## 关联命令

- [[stress]]
- [[turbostat]]

## 风险提示

> ⚠️ **MEDIUM**: 运行 stress 测试会提升温度和功耗，注意散热

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]
