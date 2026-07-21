---
{
  "cmd_name": "createdb",
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

# createdb

> Create a new PostgreSQL database

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
createdb [options] dbname
```

## 参数

| Flag | Description |
|------|-------------|
| `-U` | Database user name |
| `-h` | Database host |
| `-O` | Database owner |
| `-E` | Encoding |

## 示例

### 示例 1: Create new database

```bash
createdb mydb
```

### 示例 2: Create database with specific owner

```bash
createdb -U postgres -O admin mydb
```

### 示例 3: Create database with UTF8 encoding

```bash
createdb -E UTF8 mydb
```

## 风险提示

> ⚠️ **MEDIUM**: Creates new database; requires appropriate privileges

## 所属维度

[[MySQL工具-MOC|Database]]
