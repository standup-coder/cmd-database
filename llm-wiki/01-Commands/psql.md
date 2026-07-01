---
{
  "cmd_name": "psql",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Install PostgreSQL package",
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

# psql

> PostgreSQL interactive terminal

## 安装

```bash
Install PostgreSQL package
```

## 用法

```
psql [options] [dbname [username]]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | Database server host |
| `-p` | Database server port |
| `-U` | Database user name |
| `-d` | Database name |
| `-c` | Execute single command and exit |
| `-f` | Execute commands from file |

## 示例

### 示例 1: Connect as postgres user

```bash
psql -U postgres
```

### 示例 2: Connect to specific database

```bash
psql -h localhost -U admin -d mydb
```

### 示例 3: Execute single SQL command

```bash
psql -c 'SELECT version();'
```

### 示例 4: Execute SQL from file

```bash
psql -f script.sql
```

## 风险提示

> ⚠️ **HIGH**: Direct database access; can modify or delete data

## 所属维度

[[Database-MOC|Database]]
