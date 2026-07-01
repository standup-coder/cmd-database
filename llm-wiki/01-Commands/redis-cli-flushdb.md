---
{
  "cmd_name": "redis-cli FLUSHDB",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Included with Redis installation",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/database/redis.yaml"
}
---

# redis-cli FLUSHDB

> Delete all keys in current database

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-cli FLUSHDB [ASYNC]
```

## 示例

### 示例 1: Delete all keys in current database

```bash
redis-cli FLUSHDB
```

### 示例 2: Delete asynchronously (non-blocking)

```bash
redis-cli FLUSHDB ASYNC
```

### 示例 3: Delete all keys in all databases

```bash
redis-cli FLUSHALL
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes all data; cannot be undone

## 所属维度

[[Database-MOC|Database]]
