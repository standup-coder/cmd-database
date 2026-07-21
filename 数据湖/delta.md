---
{
  "cmd_name": "delta",
  "cmd_category": "大数据/数据湖",
  "cmd_dimension": "数据湖",
  "cmd_install": "pip install delta-spark 或在 Apache Spark 中引入 delta-core",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "spark-sql",
    "hadoop"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/data-lake.yaml"
}
---

# delta

> Delta Lake 表格式命令入口（通常通过 Spark 或 delta-rs 使用）

## 安装

```bash
pip install delta-spark 或在 Apache Spark 中引入 delta-core
```

## 用法

```
delta [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `table-details` | 查看 Delta 表元数据 |

## 示例

### 示例 1: 查看 Delta 表历史版本

```bash
spark-sql --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
          -e "DESCRIBE HISTORY delta.`/path/to/table`"

```

### 示例 2: 查看 Delta 表详情（需安装 delta-rs CLI）

```bash
delta table-details --table /path/to/table

```

## 关联命令

- [[spark-sql]]
- [[hadoop]]

## 风险提示

> ⚠️ **HIGH**: VACUUM 或 RESTORE 操作会清理/回滚历史数据，请确认保留策略

## 所属维度

[[数据湖-MOC|大数据/数据湖]]
