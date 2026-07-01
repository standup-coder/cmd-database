---
{
  "cmd_name": "kafka",
  "cmd_category": "容器编排/消息队列",
  "cmd_dimension": "消息队列",
  "cmd_install": "参考 https://kafka.apache.org/quickstart",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "zookeeper",
    "kafka-console-producer",
    "kafka-console-consumer"
  ],
  "cmd_tags": [
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/bigdata/kafka.yaml"
}
---

# kafka

> Apache Kafka分布式消息队列

## 安装

```bash
参考 https://kafka.apache.org/quickstart
```

## 用法

```
kafka-server-start.sh [选项] server.properties
```

## 参数

| Flag | Description |
|------|-------------|
| `--override` | 覆盖配置属性 |

## 示例

### 示例 1: 启动Kafka服务器

```bash
kafka-server-start.sh config/server.properties
```

### 示例 2: 创建Topic

```bash
kafka-topics.sh --create --topic mytopic --bootstrap-server localhost:9092
```

## 关联命令

- [[kafka-console-producer]]
- [[kafka-console-consumer]]

## 所属维度

[[消息队列-MOC|容器编排/消息队列]]
