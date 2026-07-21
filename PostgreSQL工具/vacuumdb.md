---
{
  "cmd_name": "vacuumdb",
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

# vacuumdb

> Garbage-collect and analyze a PostgreSQL database

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
vacuumdb [options] dbname
```

## 参数

| Flag | Description |
|------|-------------|
| `-U` | Database user name |
| `-z` | Also run analyze |
| `-f` | Full vacuum |
| `-t` | Vacuum specific table |
| `-a` | Vacuum all databases |

## 示例

### 示例 1: Vacuum database

```bash
vacuumdb mydb
```

### 示例 2: Vacuum and analyze database

```bash
vacuumdb -z mydb
```

### 示例 3: Full vacuum (reclaims more space)

```bash
vacuumdb -f mydb
```

### 示例 4: Vacuum all databases

```bash
vacuumdb -a
```

## 风险提示

> ⚠️ **MEDIUM**: Full vacuum locks tables; may impact performance

## 所属维度

[[MySQL工具-MOC|Database]]
