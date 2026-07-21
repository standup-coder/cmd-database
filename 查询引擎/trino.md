---
{
  "cmd_name": "trino",
  "cmd_category": "大数据/查询引擎",
  "cmd_dimension": "查询引擎",
  "cmd_install": "参考 https://trino.io/docs/current/installation.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "presto",
    "hive"
  ],
  "cmd_tags": [
    "data",
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/query-engines.yaml"
}
---

# trino

> Trino 分布式 SQL 查询引擎 CLI

## 安装

```bash
参考 https://trino.io/docs/current/installation.html
```

## 用法

```
trino [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--server` | 指定 Trino 协调节点 |
| `--catalog` | 指定 Catalog |
| `--user` | 指定用户名 |

## 示例

### 示例 1: 连接 Trino 并指定用户

```bash
trino --server localhost:8080 --catalog postgresql --user admin
```

### 示例 2: 列出所有 Catalog

```bash
trino --server localhost:8080 --execute "SHOW CATALOGS"
```

## 关联命令

- [[presto]]
- [[hive]]

## 风险提示

> ⚠️ **MEDIUM**: 复杂联邦查询可能产生高并发，请监控集群负载

## 所属维度

[[查询引擎-MOC|大数据/查询引擎]]
