---
{
  "cmd_name": "pulsar",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "docker pull apachepulsar/pulsar",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka",
    "redis"
  ],
  "cmd_tags": [
    "monitoring",
    "data",
    "distributed",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# pulsar

> Apache Pulsar分布式消息流平台，用于AI流水线事件驱动和数据流处理

## 安装

```bash
docker pull apachepulsar/pulsar
```

## 用法

```
pulsar-admin [COMMAND] [OPTIONS]
```

```
pulsar-client [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `topics create` | 创建Topic |
| `topics produce` | 生产消息 |
| `topics consume` | 消费消息 |

## 示例

### 示例 1: 创建AI事件Topic

```bash
pulsar-admin topics create persistent://public/default/ml-events
```

### 示例 2: 发送模型推理事件

```bash
pulsar-client produce ml-events --messages '{"model":"v1","latency":120}'
```

## 关联命令

- [[kafka]]
- [[redis]]

## 风险提示

> ⚠️ **MEDIUM**: 消息队列配置不当可能导致数据丢失

## 参考链接

- [https://pulsar.apache.org/](https://pulsar.apache.org/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
