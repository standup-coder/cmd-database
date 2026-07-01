---
{
  "cmd_name": "mysqladmin",
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
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/database/mysql.yaml"
}
---

# mysqladmin

> MySQL server administration utility

## 安装

```bash
Included with MySQL Server installation
```

## 用法

```
mysqladmin [options] command [command-options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | Username for authentication |
| `-p` | Prompt for password |
| `-h` | Host to connect to |

## 示例

### 示例 1: Display server status

```bash
mysqladmin -u root -p status
```

### 示例 2: Show active processes

```bash
mysqladmin -u root -p processlist
```

### 示例 3: Create new database

```bash
mysqladmin -u root -p create newdb
```

### 示例 4: Drop database

```bash
mysqladmin -u root -p drop olddb
```

### 示例 5: Shutdown MySQL server

```bash
mysqladmin -u root -p shutdown
```

## 风险提示

> ⚠️ **CRITICAL**: Can shutdown server or drop databases; use with extreme caution

## 所属维度

[[Database-MOC|Database]]
