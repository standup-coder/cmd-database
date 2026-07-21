---
{
  "cmd_name": "airflow",
  "cmd_category": "大数据/数据集成与ETL",
  "cmd_dimension": "数据集成与ETL",
  "cmd_install": "pip install apache-airflow",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dbt",
    "sqoop"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/etl.yaml"
}
---

# airflow

> Apache Airflow 工作流调度命令

## 安装

```bash
pip install apache-airflow
```

## 用法

```
airflow [OPTIONS] COMMAND [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `dags list` | 列出所有 DAG |
| `dags trigger` | 手动触发 DAG |
| `tasks test` | 测试单个任务 |

## 示例

### 示例 1: 列出所有 DAG

```bash
airflow dags list
```

### 示例 2: 触发指定 DAG 的特定执行日期

```bash
airflow dags trigger my_dag -e "2024-01-01"
```

## 关联命令

- [[dbt]]
- [[sqoop]]

## 风险提示

> ⚠️ **MEDIUM**: 手动触发或回填 DAG 可能影响下游依赖和数据一致性

## 所属维度

[[数据集成与ETL-MOC|大数据/数据集成与ETL]]
