---
cmd_name: kafka
cmd_category: 容器编排/消息队列
cmd_dimension: 消息队列
cmd_install: 参考 https://kafka.apache.org/quickstart
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related: []
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: Apache Kafka分布式消息队列
created: '2026-06-04'
source_file: data/container/kafka.yaml
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

### 启动Kafka服务器

```bash
kafka-server-start.sh config/server.properties
```

### 创建Topic

```bash
kafka-topics.sh --create --topic mytopic --bootstrap-server localhost:9092
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[消息队列-MOC|容器编排/消息队列]]
