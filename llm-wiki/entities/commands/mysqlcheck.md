---
cmd_name: mysqlcheck
cmd_category: "数据库工具/MySQL工具"
cmd_dimension: Database
cmd_install: Included with MySQL Server installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Check, repair, analyze, and optimize MySQL tables"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/database/mysql.yaml
---


# mysqlcheck

> Check, repair, analyze, and optimize MySQL tables

## 安装

```bash
Included with MySQL Server installation
```

## 用法

```
mysqlcheck [options] database [tables]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | Username for authentication |
| `-p` | Prompt for password |
| `--check` | Check tables for errors |
| `--repair` | Repair corrupted tables |
| `--analyze` | Analyze tables for better query performance |
| `--optimize` | Optimize tables |
| `--all-databases` | Check all databases |

## 示例

### 示例 1: Check all tables in database

```bash
mysqlcheck -u root -p --check mydb
```

### 示例 2: Repair specific table

```bash
mysqlcheck -u root -p --repair mydb mytable
```

### 示例 3: Optimize all tables in all databases

```bash
mysqlcheck -u root -p --optimize --all-databases
```

### 示例 4: Analyze tables for query optimization

```bash
mysqlcheck -u root -p --analyze mydb
```

## 风险提示

> ⚠️ **MEDIUM**: Repair operations may cause data loss if table is severely corrupted

## 所属维度

[[Redis工具-MOC|Database]]
