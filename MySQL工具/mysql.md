---
{
  "cmd_name": "mysql",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Install MySQL Server or Client package",
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
  "source_file": "data/database/mysql.yaml"
}
---

# mysql

> MySQL command-line client for database operations

## 安装

```bash
Install MySQL Server or Client package
```

## 用法

```
mysql [options] [database]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | Username for authentication |
| `-p` | Prompt for password |
| `-h` | Host to connect to |
| `-P` | Port number |
| `-D` | Database name |
| `-e` | Execute SQL statement and exit |

## 示例

### 示例 1: Connect as root user with password prompt

```bash
mysql -u root -p
```

### 示例 2: Connect to specific database on host

```bash
mysql -h localhost -u admin -p mydb
```

### 示例 3: Execute SQL command and exit

```bash
mysql -u root -p -e 'SHOW DATABASES;'
```

### 示例 4: Connect to remote MySQL server

```bash
mysql -h 192.168.1.100 -P 3306 -u user -p
```

## 风险提示

> ⚠️ **HIGH**: Direct database access; can modify or delete data

## 所属维度

[[MySQL工具-MOC|Database]]
