---
{
  "cmd_name": "kafka-topics.sh",
  "cmd_category": "大数据/Kafka工具",
  "cmd_dimension": "Kafka工具",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kafka-console-producer",
    "kafka-console-consumer"
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

# kafka-topics.sh

> Kafka Topic 创建、查看与管理

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-topics.sh [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | 指定 Kafka  broker 地址 |
| `--create` | 创建 Topic |
| `--list` | 列出所有 Topic |

## 示例

### 示例 1: 列出所有 Topic

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

### 示例 2: 创建 3 分区的 Topic

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic mytopic --partitions 3 --replication-factor 1
```

## 关联命令

- [[kafka-console-producer]]
- [[kafka-console-consumer]]

## 风险提示

> ⚠️ **MEDIUM**: 删除 Topic 会丢失数据，请确认 retention 和备份策略

## 所属维度

[[Kafka工具-MOC|大数据/Kafka工具]]
