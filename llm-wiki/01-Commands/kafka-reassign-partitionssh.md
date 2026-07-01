---
{
  "cmd_name": "kafka-reassign-partitions.sh",
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
    "kafka-configs.sh"
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

# kafka-reassign-partitions.sh

> Kafka 分区重分配工具

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-reassign-partitions.sh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bootstrap-server` |  |
| `--topics-to-move-json-file` |  |
| `--generate` |  |
| `--execute` |  |
| `--verify` |  |

## 示例

### 示例 1: 生成分配计划

```bash
kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --topics-to-move-json-file topics.json --broker-list 0,1,2 --generate
```

### 示例 2: 执行重分配

```bash
kafka-reassign-partitions.sh --reassignment-json-file plan.json --execute
```

## 关联命令

- [[kafka-topics.sh]]
- [[kafka-configs.sh]]

## 风险提示

> ⚠️ **HIGH**: 分区重分配会移动大量数据并影响性能，请先在低峰期验证

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
