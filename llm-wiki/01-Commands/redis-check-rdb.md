---
{
  "cmd_name": "redis-check-rdb",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/redis.yaml"
}
---

# redis-check-rdb

> Check Redis RDB snapshot file

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-check-rdb <dump.rdb>
```

## 示例

### 示例 1: Check RDB file integrity

```bash
redis-check-rdb dump.rdb
```

### 示例 2: 详细输出 RDB 检查结果

```bash
redis-check-rdb --verbose dump.rdb
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; safe to use

## 所属维度

[[Database-MOC|Database]]
