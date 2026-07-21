---
{
  "cmd_name": "dbt",
  "cmd_category": "大数据/数据集成与ETL",
  "cmd_dimension": "数据集成与ETL",
  "cmd_install": "pip install dbt-core 或对应 adapter（如 dbt-postgres）",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airflow",
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

# dbt

> 数据转换工具，支持 SQL 模型版本化与测试

## 安装

```bash
pip install dbt-core 或对应 adapter（如 dbt-postgres）
```

## 用法

```
dbt [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行所有模型 |
| `test` | 运行所有测试 |
| `build` | 运行模型与测试的组合命令 |

## 示例

### 示例 1: 运行项目中的所有模型

```bash
dbt run
```

### 示例 2: 运行带 daily 标签的模型及对应测试

```bash
dbt build --select tag:daily
```

## 关联命令

- [[airflow]]
- [[sqoop]]

## 风险提示

> ⚠️ **MEDIUM**: dbt run 会改写目标表，请在非生产环境或事务保护下测试

## 所属维度

[[数据集成与ETL-MOC|大数据/数据集成与ETL]]
