---
{
  "cmd_name": "mysqlshow",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/mysql.yaml"
}
---

# mysqlshow

> Display database, table, and column information

## 安装

```bash
Included with MySQL Server installation
```

## 用法

```
mysqlshow [options] [database [table [column]]]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | Username for authentication |
| `-p` | Prompt for password |
| `-h` | Host to connect to |
| `--status` | Show table status information |

## 示例

### 示例 1: Show all databases

```bash
mysqlshow -u root -p
```

### 示例 2: Show tables in database

```bash
mysqlshow -u root -p mydb
```

### 示例 3: Show columns in table

```bash
mysqlshow -u root -p mydb mytable
```

### 示例 4: Show table status with detailed information

```bash
mysqlshow -u root -p --status mydb
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Database-MOC|Database]]
