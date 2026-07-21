---
{
  "cmd_name": "spark-submit",
  "cmd_category": "大数据/Spark计算",
  "cmd_dimension": "Spark计算",
  "cmd_install": "参考 https://spark.apache.org/downloads.html",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "spark-shell",
    "pyspark"
  ],
  "cmd_tags": [
    "application",
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/spark.yaml"
}
---

# spark-submit

> 提交 Spark 应用程序到集群

## 安装

```bash
参考 https://spark.apache.org/downloads.html
```

## 用法

```
spark-submit [OPTIONS] APP_FILE [APP_ARGUMENTS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--master` | 指定集群主节点地址（如 yarn、spark://host:7077、local[*]） |
| `--deploy-mode` | 部署模式（client 或 cluster） |
| `--class` | Java/Scala 应用的主类 |

## 示例

### 示例 1: 本地模式提交 Scala 应用

```bash
spark-submit --master local[*] --class MyApp myapp.jar
```

### 示例 2: 以 cluster 模式提交到 YARN

```bash
spark-submit --master yarn --deploy-mode cluster myapp.py
```

## 关联命令

- [[spark-shell]]
- [[pyspark]]

## 风险提示

> ⚠️ **MEDIUM**: 提交到共享集群时请注意资源占用，避免耗尽队列资源

## 所属维度

[[Spark计算-MOC|大数据/Spark计算]]
