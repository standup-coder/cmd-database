---
{
  "cmd_name": "dropdb",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Included with PostgreSQL",
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
  "source_file": "data/database/postgresql.yaml"
}
---

# dropdb

> Remove a PostgreSQL database

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
dropdb [options] dbname
```

## 参数

| Flag | Description |
|------|-------------|
| `-U` | Database user name |
| `-h` | Database host |
| `-i` | Prompt before deletion |

## 示例

### 示例 1: Drop database

```bash
dropdb mydb
```

### 示例 2: Drop with confirmation prompt

```bash
dropdb -i mydb
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes database; cannot be undone

## 所属维度

[[MySQL工具-MOC|Database]]
