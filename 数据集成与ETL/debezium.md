---
{
  "cmd_name": "debezium",
  "cmd_category": "大数据/数据集成与ETL",
  "cmd_dimension": "数据集成与ETL",
  "cmd_install": "参考 https://debezium.io/documentation/reference/stable/install.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-topics.sh",
    "airflow"
  ],
  "cmd_tags": [
    "deployment",
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/etl.yaml"
}
---

# debezium

> CDC（变更数据捕获）工具，常通过 Kafka Connect 部署

## 安装

```bash
参考 https://debezium.io/documentation/reference/stable/install.html
```

## 用法

```
debezium [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `connector` | 管理 Kafka Connect 连接器 |

## 示例

### 示例 1: 注册 Debezium MySQL 源连接器

```bash
curl -X POST http://localhost:8083/connectors -d @debezium-mysql-source.json
```

### 示例 2: 查看连接器状态

```bash
curl http://localhost:8083/connectors/inventory-connector/status
```

## 关联命令

- [[kafka-topics.sh]]
- [[airflow]]

## 风险提示

> ⚠️ **HIGH**: CDC 会读取数据库 binlog，可能影响主库性能并涉及敏感数据变更

## 所属维度

[[数据集成与ETL-MOC|大数据/数据集成与ETL]]
