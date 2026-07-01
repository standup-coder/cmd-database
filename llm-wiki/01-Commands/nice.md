---
{
  "cmd_name": "nice",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "renice",
    "top"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# nice

> 以指定优先级运行命令

## 用法

```
nice [OPTIONS] [COMMAND [ARGS]]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 指定 nice 值（-20 到 19） |

## 示例

### 示例 1: 以较低优先级运行任务

```bash
nice -n 10 ./long-task
```

### 示例 2: 以较高优先级运行任务（需 root）

```bash
nice -n -5 ./critical-task
```

## 关联命令

- [[renice]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
