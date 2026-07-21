---
{
  "cmd_name": "kafka-producer-perf-test",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-consumer-perf-test",
    "kafka-topics.sh"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/extra.yaml"
}
---

# kafka-producer-perf-test

> Kafka 生产者性能测试

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-producer-perf-test [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--topic` | 目标 topic |
| `--num-records` | 记录数 |
| `--record-size` | 记录大小 |
| `--throughput` | 吞吐量 |

## 示例

### 示例 1: 测试生产者性能

```bash
kafka-producer-perf-test.sh --topic test --num-records 100000 --record-size 1024 --throughput 1000
```

### 示例 2: 小批量测试

```bash
kafka-producer-perf-test.sh --topic test --num-records 10000 --record-size 512
```

## 关联命令

- [[kafka-consumer-perf-test]]
- [[kafka-topicssh]]

## 风险提示

> ⚠️ **HIGH**: 压测会写入大量数据到 Kafka，请确认 topic 配置和磁盘空间

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
