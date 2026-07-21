---
{
  "cmd_name": "databricks",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install databricks-cli",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "spark-submit",
    "aws"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# databricks

> Databricks CLI

## 安装

```bash
pip install databricks-cli
```

## 用法

```
databricks [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `clusters` | 管理集群 |
| `jobs` | 管理作业 |
| `fs` | DBFS 文件 |
| `runs` |  |

## 示例

### 示例 1: 列出集群

```bash
databricks clusters list
```

### 示例 2: 立即运行作业

```bash
databricks jobs run-now --job-id 1
```

## 关联命令

- [[spark-submit]]
- [[aws]]

## 风险提示

> ⚠️ **MEDIUM**: databricks 操作会产生云费用并影响作业，请确认参数

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
