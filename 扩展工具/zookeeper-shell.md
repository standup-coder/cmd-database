---
{
  "cmd_name": "zookeeper-shell",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Apache ZooKeeper 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kafka-topics.sh",
    "hdfs"
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

# zookeeper-shell

> ZooKeeper 命令行客户端

## 安装

```bash
随 Apache ZooKeeper 安装
```

## 用法

```
zookeeper-shell [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-server` | 指定服务器 |

## 示例

### 示例 1: 连接本地 ZooKeeper

```bash
zookeeper-shell localhost:2181
```

### 示例 2: 列出根节点

```bash
echo 'ls /' | zookeeper-shell localhost:2181
```

## 关联命令

- [[kafka-topicssh]]
- [[hdfs]]

## 风险提示

> ⚠️ **MEDIUM**: 删除 ZooKeeper 节点可能影响 Kafka/HBase 等依赖服务

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
