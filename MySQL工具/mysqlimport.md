---
{
  "cmd_name": "mysqlimport",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Included with MySQL Server installation",
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

# mysqlimport

> Import data from text files into MySQL tables

## 安装

```bash
Included with MySQL Server installation
```

## 用法

```
mysqlimport [options] database file.txt
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | Username for authentication |
| `-p` | Prompt for password |
| `--local` | Read input files from client host |
| `--replace` | Replace existing rows with same unique key |
| `--ignore` | Ignore duplicate rows |

## 示例

### 示例 1: Import data from text file

```bash
mysqlimport -u root -p mydb data.txt
```

### 示例 2: Import with replace mode from local file

```bash
mysqlimport -u root -p --local --replace mydb employees.txt
```

## 风险提示

> ⚠️ **HIGH**: Can overwrite or modify existing data

## 所属维度

[[MySQL工具-MOC|Database]]
