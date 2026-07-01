---
{
  "cmd_name": "pg_dump",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Included with PostgreSQL",
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
  "source_file": "data/database/postgresql.yaml"
}
---

# pg_dump

> PostgreSQL database backup utility

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
pg_dump [options] dbname > output.sql
```

## 参数

| Flag | Description |
|------|-------------|
| `-U` | Database user name |
| `-h` | Database host |
| `-F` | Output format (c=custom, t=tar, p=plain) |
| `-t` | Dump specific table |
| `--schema-only` | Dump only schema, no data |
| `--data-only` | Dump only data, no schema |

## 示例

### 示例 1: Backup database to SQL file

```bash
pg_dump mydb > mydb_backup.sql
```

### 示例 2: Backup in custom format

```bash
pg_dump -U postgres -Fc mydb > mydb.dump
```

### 示例 3: Backup only database schema

```bash
pg_dump --schema-only mydb > schema.sql
```

### 示例 4: Backup specific table

```bash
pg_dump -t mytable mydb > table_backup.sql
```

## 风险提示

> ⚠️ **MEDIUM**: Large databases may take significant time and disk space

## 所属维度

[[Database-MOC|Database]]
