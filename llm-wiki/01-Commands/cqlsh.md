---
{
  "cmd_name": "cqlsh",
  "cmd_category": "数据库工具/NoSQL",
  "cmd_dimension": "NoSQL",
  "cmd_install": "随 Apache Cassandra 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cassandra-stress"
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

# cqlsh

> Cassandra CQL 交互式 Shell

## 安装

```bash
随 Apache Cassandra 安装
```

## 用法

```
cqlsh [OPTIONS] [HOST [PORT]]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 用户名 |
| `-p` | 密码 |
| `-k` | 指定默认 keyspace |

## 示例

### 示例 1: 以用户名连接本地 Cassandra

```bash
cqlsh localhost 9042 -u cassandra
```

### 示例 2: 列出所有 keyspace 后退出

```bash
cqlsh -e "DESCRIBE KEYSPACES"
```

## 关联命令

- [[cassandra-stress]]

## 风险提示

> ⚠️ **MEDIUM**: 命令行传入密码会留在历史记录，建议使用 .cqlshrc 配置文件

## 所属维度

[[NoSQL-MOC|数据库工具/NoSQL]]
