---
{
  "cmd_name": "redis-cli MONITOR",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Included with Redis installation",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/redis.yaml"
}
---

# redis-cli MONITOR

> Monitor all commands processed by Redis server

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-cli MONITOR
```

## 示例

### 示例 1: Stream all commands in real-time

```bash
redis-cli MONITOR
```

### 示例 2: 只监控前 20 条命令

```bash
redis-cli MONITOR | head -n 20
```

## 风险提示

> ⚠️ **MEDIUM**: Can significantly impact performance on busy servers

## 所属维度

[[Database-MOC|Database]]
