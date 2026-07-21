---
{
  "cmd_name": "mongorestore",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 MongoDB Database Tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mongodump",
    "mongosh"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# mongorestore

> 从 mongodump 备份恢复 MongoDB 数据

## 安装

```bash
随 MongoDB Database Tools 安装
```

## 用法

```
mongorestore [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--uri` | 连接 URI |
| `--nsInclude` | 包含命名空间 |
| `--drop` | 恢复前删除 |

## 示例

### 示例 1: 恢复备份

```bash
mongorestore --uri='mongodb://localhost:27017' /backup/mongo
```

### 示例 2: 恢复指定数据库

```bash
mongorestore --db mydb /backup/mongo/mydb
```

## 关联命令

- [[mongodump]]
- [[mongosh]]

## 风险提示

> ⚠️ **HIGH**: --drop 会清空现有集合，恢复前请确认备份正确

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
