---
{
  "cmd_name": "kafka-mirror-maker",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-topics.sh",
    "debezium"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# kafka-mirror-maker

> Kafka 跨集群镜像复制工具

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-mirror-maker [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--consumer.config` |  |
| `--producer.config` |  |
| `--whitelist` |  |

## 示例

### 示例 1: 镜像所有 topic

```bash
kafka-mirror-maker.sh --consumer.config consumer.properties --producer.config producer.properties --whitelist '.*'
```

### 示例 2: 只镜像指定 topic

```bash
kafka-mirror-maker.sh --whitelist 'topic1,topic2'
```

## 关联命令

- [[kafka-topicssh]]
- [[debezium]]

## 风险提示

> ⚠️ **HIGH**: 镜像会复制大量数据并可能覆盖目标集群，请确认白名单和 offset 策略

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
