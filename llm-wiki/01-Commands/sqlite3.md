---
{
  "cmd_name": "sqlite3",
  "cmd_category": "数据库工具/NoSQL",
  "cmd_dimension": "NoSQL",
  "cmd_install": "多数 Linux/macOS 预装，或从 https://sqlite.org/download.html 安装",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mysql",
    "psql"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/nosql.yaml"
}
---

# sqlite3

> SQLite 命令行数据库客户端

## 安装

```bash
多数 Linux/macOS 预装，或从 https://sqlite.org/download.html 安装
```

## 用法

```
sqlite3 [OPTIONS] DATABASE [SQL]
```

## 参数

| Flag | Description |
|------|-------------|
| `-header` | 显示列标题 |
| `-csv` | 以 CSV 模式输出 |
| `-init` | 启动时执行的 SQL 文件 |

## 示例

### 示例 1: 列出数据库中的所有表

```bash
sqlite3 mydb.db ".tables"
```

### 示例 2: 执行 SQL 查询并退出

```bash
sqlite3 mydb.db "SELECT * FROM users LIMIT 5"
```

## 关联命令

- [[mysql]]
- [[psql]]

## 风险提示

> ⚠️ **LOW**: SQLite 为文件级数据库，请确保有文件写权限并定期备份

## 所属维度

[[NoSQL-MOC|数据库工具/NoSQL]]
