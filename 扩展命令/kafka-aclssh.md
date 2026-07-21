---
{
  "cmd_name": "kafka-acls.sh",
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

# kafka-acls.sh

> Kafka ACL 权限管理

## 安装

```bash
随 Apache Kafka 安装
```

## 用法

```
kafka-acls.sh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--add` | 添加 |
| `--remove` | 删除 |
| `--list` | 列出 |
| `--allow-principal` |  |
| `--operation` |  |

## 示例

### 示例 1: 列出 ACL

```bash
kafka-acls.sh --bootstrap-server localhost:9092 --list
```

### 示例 2: 添加读权限

```bash
kafka-acls.sh --add --allow-principal User:alice --operation Read --topic mytopic
```

## 关联命令

- [[kafka-topics.sh]]
- [[kafka-configs.sh]]

## 风险提示

> ⚠️ **HIGH**: 错误的 ACL 会导致服务无法访问或过度授权

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
