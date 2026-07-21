---
{
  "cmd_name": "livy-submit",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://livy.apache.org/get-started/",
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
  "source_file": "data/bigdata/extra.yaml"
}
---

# livy-submit

> 通过 Livy 提交 Spark 作业到集群

## 安装

```bash
参考 https://livy.apache.org/get-started/
```

## 用法

```
livy-submit [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--file` | 提交文件 |
| `--class` | 主类 |
| `--args` | 程序参数 |

## 示例

### 示例 1: 提交 Python 作业

```bash
livy-submit --file job.py --class main
```

### 示例 2: 通过 REST 提交

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"file":"job.py"}' http://livy:8998/batches
```

## 关联命令

- [[spark-submit]]
- [[pyspark]]

## 风险提示

> ⚠️ **MEDIUM**: REST 提交时请保护 Livy 服务端点，避免未授权访问

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
