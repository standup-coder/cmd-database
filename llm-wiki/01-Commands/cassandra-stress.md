---
{
  "cmd_name": "cassandra-stress",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Apache Cassandra 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "cqlsh",
    "nodetool"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# cassandra-stress

> Cassandra 压力测试工具

## 安装

```bash
随 Apache Cassandra 安装
```

## 用法

```
cassandra-stress [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `user` | 自定义 profile |
| `write` | 写压测 |
| `read` | 读压测 |
| `-node` | 目标节点 |

## 示例

### 示例 1: 写入压力测试

```bash
cassandra-stress write -node 127.0.0.1
```

### 示例 2: 5 分钟读压测

```bash
cassandra-stress read duration=5m -rate threads=50
```

## 关联命令

- [[cqlsh]]

## 风险提示

> ⚠️ **HIGH**: 压测会大量消耗 Cassandra 资源，请避开业务高峰并获授权

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
