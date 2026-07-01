---
{
  "cmd_name": "presto",
  "cmd_category": "大数据/查询引擎",
  "cmd_dimension": "查询引擎",
  "cmd_install": "参考 https://prestodb.io/docs/current/installation.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "trino",
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

# presto

> Presto 分布式 SQL 查询引擎 CLI

## 安装

```bash
参考 https://prestodb.io/docs/current/installation.html
```

## 用法

```
presto [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--server` | 指定 Presto 协调节点 |
| `--catalog` | 指定 Catalog |
| `--schema` | 指定 Schema |

## 示例

### 示例 1: 连接 Presto 并指定 catalog/schema

```bash
presto --server localhost:8080 --catalog hive --schema default
```

### 示例 2: 执行分布式查询

```bash
presto --server localhost:8080 --execute "SELECT count(*) FROM hive.default.users"
```

## 关联命令

- [[trino]]
- [[hive]]

## 风险提示

> ⚠️ **MEDIUM**: 跨源查询可能扫描大量数据，请关注资源队列和成本

## 所属维度

[[查询引擎-MOC|大数据/查询引擎]]
