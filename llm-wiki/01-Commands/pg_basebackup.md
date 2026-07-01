---
{
  "cmd_name": "pg_basebackup",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/postgresql.yaml"
}
---

# pg_basebackup

> Take a base backup of a PostgreSQL cluster

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
pg_basebackup [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-D` | Output directory |
| `-U` | Database user |
| `-h` | Database host |
| `-F` | Output format (p=plain, t=tar) |
| `-z` | Compress tar output |

## 示例

### 示例 1: Create base backup

```bash
pg_basebackup -D /backup/pg -U replication
```

### 示例 2: Create compressed tar backup

```bash
pg_basebackup -D /backup/pg -Ft -z
```

## 风险提示

> ⚠️ **MEDIUM**: Requires replication privileges; backup may be large

## 所属维度

[[Database-MOC|Database]]
