---
{
  "cmd_name": "pyspark",
  "cmd_category": "大数据/Spark计算",
  "cmd_dimension": "Spark计算",
  "cmd_install": "随 Apache Spark 安装，也可 pip install pyspark",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "spark-submit",
    "spark-shell"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/bigdata/spark.yaml"
}
---

# pyspark

> Spark 交互式 Python Shell

## 安装

```bash
随 Apache Spark 安装，也可 pip install pyspark
```

## 用法

```
pyspark [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--master` | 指定 Spark master |
| `--conf` | 设置 Spark 配置项 |

## 示例

### 示例 1: 本地模式启动 PySpark

```bash
pyspark --master local[*]
```

### 示例 2: 启用自适应查询执行

```bash
pyspark --conf spark.sql.adaptive.enabled=true
```

## 关联命令

- [[spark-submit]]
- [[spark-shell]]

## 风险提示

> ⚠️ **LOW**: 生产环境注意限制并发和资源占用

## 所属维度

[[Spark计算-MOC|大数据/Spark计算]]
