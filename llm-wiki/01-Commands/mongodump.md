---
{
  "cmd_name": "mongodump",
  "cmd_category": "数据库工具/NoSQL",
  "cmd_dimension": "NoSQL",
  "cmd_install": "随 MongoDB Database Tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mongosh",
    "mongorestore"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/nosql.yaml"
}
---

# mongodump

> MongoDB 逻辑备份工具

## 安装

```bash
随 MongoDB Database Tools 安装
```

## 用法

```
mongodump [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--uri` | MongoDB 连接 URI |
| `--db` | 指定备份的数据库 |
| `--out` | 输出目录 |

## 示例

### 示例 1: 备份所有数据库到指定目录

```bash
mongodump --uri="mongodb://localhost:27017" --out=/backup/mongo
```

### 示例 2: 备份指定集合

```bash
mongodump --db mydb --collection users
```

## 关联命令

- [[mongosh]]
- [[mongorestore]]

## 风险提示

> ⚠️ **MEDIUM**: 备份大量数据会影响数据库性能，建议在业务低峰期执行

## 所属维度

[[NoSQL-MOC|数据库工具/NoSQL]]
