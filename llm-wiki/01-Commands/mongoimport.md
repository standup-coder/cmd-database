---
{
  "cmd_name": "mongoimport",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 MongoDB Database Tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mongoexport",
    "mongosh"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# mongoimport

> 将 JSON/CSV/TSV 导入 MongoDB

## 安装

```bash
随 MongoDB Database Tools 安装
```

## 用法

```
mongoimport [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--db` | 数据库 |
| `--collection` | 集合 |
| `--file` | 输入文件 |
| `--headerline` |  |

## 示例

### 示例 1: 导入 JSON

```bash
mongoimport --db mydb --collection users --file users.json
```

### 示例 2: 导入 CSV

```bash
mongoimport --db mydb --collection users --type=csv --headerline --file users.csv
```

## 关联命令

- [[mongoexport]]
- [[mongosh]]

## 风险提示

> ⚠️ **MEDIUM**: 导入会写入目标集合，可能覆盖现有数据

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
