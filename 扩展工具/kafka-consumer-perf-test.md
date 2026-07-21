---
{
  "cmd_name": "kafka-consumer-perf-test",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kafka-producer-perf-test",
    "kafka-consumer-groups.sh"
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

# kafka-consumer-perf-test

> Kafka 消费者性能测试

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-consumer-perf-test [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--topic` | 目标 topic |
| `--messages` | 消费消息数 |
| `--threads` | 线程数 |

## 示例

### 示例 1: 测试消费者性能

```bash
kafka-consumer-perf-test.sh --topic test --messages 100000 --threads 4
```

### 示例 2: 小批量测试

```bash
kafka-consumer-perf-test.sh --topic test --messages 10000
```

## 关联命令

- [[kafka-producer-perf-test]]
- [[kafka-consumer-groupssh]]

## 风险提示

> ⚠️ **MEDIUM**: 消费压测可能影响同一 consumer group 的正式消费者

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
