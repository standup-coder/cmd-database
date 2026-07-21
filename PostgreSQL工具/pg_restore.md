---
{
  "cmd_name": "pg_restore",
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
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/postgresql.yaml"
}
---

# pg_restore

> Restore PostgreSQL database from archive

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
pg_restore [options] filename
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | Database name |
| `-U` | Database user name |
| `-c` | Clean (drop) database objects before recreating |
| `-C` | Create database before restoring |
| `-t` | Restore specific table |

## 示例

### 示例 1: Restore database from dump file

```bash
pg_restore -d mydb mydb.dump
```

### 示例 2: Create and restore database

```bash
pg_restore -C -d postgres mydb.dump
```

### 示例 3: Clean and restore database

```bash
pg_restore -c -d mydb mydb.dump
```

## 风险提示

> ⚠️ **HIGH**: Can overwrite existing data; backup before restoring

## 所属维度

[[MySQL工具-MOC|Database]]
