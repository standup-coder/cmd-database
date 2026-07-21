---
{
  "cmd_name": "iceberg",
  "cmd_category": "大数据/数据湖",
  "cmd_dimension": "数据湖",
  "cmd_install": "参考 https://iceberg.apache.org/getting-started/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "spark-sql",
    "presto"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/data-lake.yaml"
}
---

# iceberg

> Apache Iceberg 表格式命令

## 安装

```bash
参考 https://iceberg.apache.org/getting-started/
```

## 用法

```
iceberg [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--catalog` | 指定 Catalog |

## 示例

### 示例 1: 使用 Spark SQL 查询 Iceberg 表

```bash
spark-sql --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions -e "SELECT * FROM catalog.db.table"
```

### 示例 2: 查看表快照（需对应 CLI 工具）

```bash
iceberg snapshot --table catalog.db.table
```

## 关联命令

- [[spark-sql]]
- [[presto]]

## 风险提示

> ⚠️ **MEDIUM**: 修改表结构或合并快照可能影响查询计划，请先在测试表验证

## 所属维度

[[数据湖-MOC|大数据/数据湖]]
