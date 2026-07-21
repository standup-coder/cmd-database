---
{
  "cmd_name": "kafka-configs.sh",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-topics.sh",
    "kafka-consumer-groups.sh"
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

# kafka-configs.sh

> Kafka 配置管理工具

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-configs.sh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--entity-type` | 实体类型 |
| `--entity-name` | 实体名称 |
| `--alter` | 修改配置 |

## 示例

### 示例 1: 查看 topic 配置

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name mytopic --describe
```

### 示例 2: 修改 retention

```bash
kafka-configs.sh --alter --add-config retention.ms=86400000 --entity-type topics --entity-name mytopic
```

## 关联命令

- [[kafka-topicssh]]
- [[kafka-consumer-groupssh]]

## 风险提示

> ⚠️ **HIGH**: 修改 topic/broker 配置会影响性能和数据保留策略，请评估影响

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
