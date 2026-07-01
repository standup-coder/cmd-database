---
{
  "cmd_name": "ksql",
  "cmd_category": "大数据/Kafka工具",
  "cmd_dimension": "Kafka工具",
  "cmd_install": "参考 https://docs.confluent.io/platform/current/ksqldb/index.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kafka-topics.sh"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/kafka-cli.yaml"
}
---

# ksql

> ksqlDB 交互式 SQL 引擎 CLI

## 安装

```bash
参考 https://docs.confluent.io/platform/current/ksqldb/index.html
```

## 用法

```
ksql [OPTIONS] [URL]
```

## 参数

| Flag | Description |
|------|-------------|
| `--execute` | 执行单条 SQL 后退出 |

## 示例

### 示例 1: 连接到本地 ksqlDB 服务

```bash
ksql http://localhost:8088
```

### 示例 2: 执行 SQL 并退出

```bash
ksql http://localhost:8088 --execute "SHOW TOPICS;"
```

## 关联命令

- [[kafka-topics.sh]]

## 风险提示

> ⚠️ **MEDIUM**: CREATE STREAM/TABLE 会持久化到 Kafka Topic，请确认配置

## 所属维度

[[Kafka工具-MOC|大数据/Kafka工具]]
