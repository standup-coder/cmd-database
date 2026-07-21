---
{
  "cmd_name": "spark-sql",
  "cmd_category": "大数据/Spark计算",
  "cmd_dimension": "Spark计算",
  "cmd_install": "随 Apache Spark 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "spark-submit",
    "pyspark"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/spark.yaml"
}
---

# spark-sql

> Spark SQL 交互式命令行

## 安装

```bash
随 Apache Spark 安装
```

## 用法

```
spark-sql [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--database` | 指定默认数据库 |
| `-e` | 直接执行 SQL 语句 |

## 示例

### 示例 1: 执行单条 SQL 查询

```bash
spark-sql -e "SELECT * FROM sales LIMIT 10"
```

### 示例 2: 进入指定数据库的交互式会话

```bash
spark-sql --database mydb
```

## 关联命令

- [[spark-submit]]
- [[pyspark]]

## 风险提示

> ⚠️ **MEDIUM**: 直接执行 SQL 可能扫描大量数据，建议先 LIMIT 验证

## 所属维度

[[Spark计算-MOC|大数据/Spark计算]]
