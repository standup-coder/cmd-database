---
{
  "cmd_name": "mysqldump",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Included with MySQL Server installation",
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
  "source_file": "data/database/mysql.yaml"
}
---

# mysqldump

> MySQL database backup utility

## 安装

```bash
Included with MySQL Server installation
```

## 用法

```
mysqldump [options] [database] > backup.sql
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | Username for authentication |
| `-p` | Prompt for password |
| `-h` | Host to connect to |
| `--all-databases` | Dump all databases |
| `--single-transaction` | Use transaction for consistent backup (InnoDB) |
| `--routines` | Include stored procedures and functions |
| `--triggers` | Include triggers |

## 示例

### 示例 1: Backup single database

```bash
mysqldump -u root -p mydb > mydb_backup.sql
```

### 示例 2: Backup all databases

```bash
mysqldump -u root -p --all-databases > all_backup.sql
```

### 示例 3: Full backup with stored procedures and triggers

```bash
mysqldump -u root -p --single-transaction --routines --triggers mydb > mydb_full.sql
```

### 示例 4: Backup specific tables

```bash
mysqldump -u root -p mydb table1 table2 > tables_backup.sql
```

## 风险提示

> ⚠️ **MEDIUM**: Large databases may take significant time and disk space

## 所属维度

[[MySQL工具-MOC|Database]]
