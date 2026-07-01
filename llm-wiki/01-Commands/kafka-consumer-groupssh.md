---
{
  "cmd_name": "kafka-consumer-groups.sh",
  "cmd_category": "大数据/Kafka工具",
  "cmd_dimension": "Kafka工具",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-topics.sh",
    "kafka-console-consumer"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/kafka-cli.yaml"
}
---

# kafka-consumer-groups.sh

> Kafka 消费者组管理

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-consumer-groups.sh [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | 指定 Kafka broker 地址 |
| `--describe` | 查看消费者组详情 |
| `--reset-offsets` | 重置消费位移 |

## 示例

### 示例 1: 查看消费者组消费进度

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group mygroup
```

### 示例 2: 重置消费组到最新位置

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group mygroup --reset-offsets --to-latest --execute --all-topics
```

## 关联命令

- [[kafka-topics.sh]]
- [[kafka-console-consumer]]

## 风险提示

> ⚠️ **HIGH**: 重置 offset 会导致消息跳过或重复消费，生产环境务必谨慎

## 所属维度

[[Kafka工具-MOC|大数据/Kafka工具]]
