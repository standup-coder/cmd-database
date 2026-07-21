---
{
  "cmd_name": "redis-check-aof",
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
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/redis.yaml"
}
---

# redis-check-aof

> Check and repair Redis AOF (Append-Only File)

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-check-aof [--fix] <file.aof>
```

## 参数

| Flag | Description |
|------|-------------|
| `--fix` | Attempt to fix corrupted AOF file |

## 示例

### 示例 1: Check AOF file for corruption

```bash
redis-check-aof appendonly.aof
```

### 示例 2: Fix corrupted AOF file

```bash
redis-check-aof --fix appendonly.aof
```

## 风险提示

> ⚠️ **HIGH**: Fixing may truncate corrupted data; backup file first

## 所属维度

[[MySQL工具-MOC|Database]]
