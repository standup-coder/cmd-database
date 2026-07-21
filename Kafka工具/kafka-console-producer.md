---
{
  "cmd_name": "kafka-console-producer",
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
    "kafka-console-consumer"
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

# kafka-console-producer

> Kafka 命令行生产者

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-console-producer.sh [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | 指定 Kafka broker 地址 |
| `--topic` | 指定目标 Topic |

## 示例

### 示例 1: 从标准输入发送消息

```bash
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic mytopic
```

### 示例 2: 发送单条消息

```bash
echo "hello" | kafka-console-producer.sh --bootstrap-server localhost:9092 --topic mytopic
```

## 关联命令

- [[kafka-topicssh]]
- [[kafka-console-consumer]]

## 风险提示

> ⚠️ **LOW**: 向生产 Topic 发送测试数据可能污染业务数据，请注意环境

## 所属维度

[[Kafka工具-MOC|大数据/Kafka工具]]
