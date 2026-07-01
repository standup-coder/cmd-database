---
{
  "cmd_name": "mongosh",
  "cmd_category": "数据库工具/NoSQL",
  "cmd_dimension": "NoSQL",
  "cmd_install": "参考 https://www.mongodb.com/docs/mongodb-shell/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mongodump",
    "mongoexport"
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

# mongosh

> MongoDB 官方交互式 Shell

## 安装

```bash
参考 https://www.mongodb.com/docs/mongodb-shell/install/
```

## 用法

```
mongosh [OPTIONS] [CONNECTION_STRING]
```

## 参数

| Flag | Description |
|------|-------------|
| `--host` | 指定 MongoDB 服务器地址 |
| `--port` | 指定端口 |
| `--username` | 用户名 |

## 示例

### 示例 1: 连接到本地 MongoDB 数据库

```bash
mongosh mongodb://localhost:27017/mydb
```

### 示例 2: 执行 JS 查询并退出

```bash
mongosh --eval "db.users.find().limit(5)"
```

## 关联命令

- [[mongodump]]
- [[mongoexport]]

## 风险提示

> ⚠️ **MEDIUM**: 连接字符串中明文密码会泄露，请使用环境变量或凭证文件

## 所属维度

[[NoSQL-MOC|数据库工具/NoSQL]]
