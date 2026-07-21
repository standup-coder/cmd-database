---
{
  "cmd_name": "mysqlbinlog",
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

# mysqlbinlog

> Process MySQL binary log files

## 安装

```bash
Included with MySQL Server installation
```

## 用法

```
mysqlbinlog [options] log_file
```

## 参数

| Flag | Description |
|------|-------------|
| `--start-datetime` | Start reading from specific datetime |
| `--stop-datetime` | Stop reading at specific datetime |
| `--database` | List only entries for specific database |
| `--base64-output` | Determine when binary log events should be displayed in base64 |

## 示例

### 示例 1: Display binary log contents

```bash
mysqlbinlog binlog.000001
```

### 示例 2: View logs from specific time

```bash
mysqlbinlog --start-datetime='2024-01-01 00:00:00' binlog.000001
```

### 示例 3: Replay binary log for specific database

```bash
mysqlbinlog --database=mydb binlog.000001 | mysql -u root -p
```

## 风险提示

> ⚠️ **HIGH**: Replaying binary logs can modify database; use with caution

## 所属维度

[[MySQL工具-MOC|Database]]
