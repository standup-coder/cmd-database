---
{
  "cmd_name": "cypher-shell",
  "cmd_category": "数据库工具/NoSQL",
  "cmd_dimension": "NoSQL",
  "cmd_install": "随 Neo4j 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "neo4j-admin"
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

# cypher-shell

> Neo4j 图数据库 Cypher 查询命令行客户端

## 安装

```bash
随 Neo4j 安装
```

## 用法

```
cypher-shell [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 用户名 |
| `-p` | 密码 |
| `-d` | 指定数据库 |

## 示例

### 示例 1: 连接本地 Neo4j

```bash
cypher-shell -u neo4j -p password
```

### 示例 2: 执行 Cypher 查询并退出

```bash
cypher-shell -u neo4j -p password -d mydb "MATCH (n) RETURN count(n)"
```

## 关联命令

- [[neo4j-admin]]

## 风险提示

> ⚠️ **MEDIUM**: MATCH ... DELETE 等写操作会修改图数据，执行前请确认查询影响范围

## 所属维度

[[NoSQL-MOC|数据库工具/NoSQL]]
