---
{
  "cmd_name": "kafka-connect",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Apache Kafka 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kafka-topics.sh",
    "debezium"
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

# kafka-connect

> Kafka Connect 连接器管理 CLI

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-connect [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `standalone` | 单机模式 |
| `distributed` | 分布式模式 |

## 示例

### 示例 1: 启动单机连接器

```bash
connect-standalone.sh connect-standalone.properties source.properties
```

### 示例 2: 启动分布式 Connect

```bash
connect-distributed.sh connect-distributed.properties
```

## 关联命令

- [[kafka-topicssh]]
- [[debezium]]

## 风险提示

> ⚠️ **MEDIUM**: 连接器配置错误会导致数据重复或丢失，请验证 topic 与 schema

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
