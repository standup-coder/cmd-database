---
{
  "cmd_name": "kafka-console-consumer",
  "cmd_category": "大数据/Kafka工具",
  "cmd_dimension": "Kafka工具",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kafka-topics.sh",
    "kafka-console-producer"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/bigdata/kafka-cli.yaml"
}
---

# kafka-console-consumer

> Kafka 命令行消费者

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-console-consumer.sh [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | 指定 Kafka broker 地址 |
| `--topic` | 指定消费 Topic |
| `--from-beginning` | 从头开始消费 |

## 示例

### 示例 1: 从头消费 Topic 消息

```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mytopic --from-beginning
```

### 示例 2: 最多消费 10 条消息

```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mytopic --max-messages 10
```

## 关联命令

- [[kafka-topics.sh]]
- [[kafka-console-producer]]

## 风险提示

> ⚠️ **LOW**: 消费生产 Topic 可能涉及敏感数据，请遵守数据合规要求

## 所属维度

[[Kafka工具-MOC|大数据/Kafka工具]]
