---
{
  "cmd_name": "spark-shell",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/bigdata/spark.yaml"
}
---

# spark-shell

> Spark 交互式 Scala REPL

## 安装

```bash
随 Apache Spark 安装
```

## 用法

```
spark-shell [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--master` | 指定 Spark master |
| `--driver-memory` | 设置 Driver 内存 |

## 示例

### 示例 1: 本地模式启动 Spark Shell

```bash
spark-shell --master local[*]
```

### 示例 2: 指定 Driver 内存启动

```bash
spark-shell --driver-memory 4g
```

## 关联命令

- [[spark-submit]]
- [[pyspark]]

## 风险提示

> ⚠️ **LOW**: 注意不要在共享集群上分配过大内存

## 所属维度

[[Spark计算-MOC|大数据/Spark计算]]
