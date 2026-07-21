---
{
  "cmd_name": "rabbitmqctl",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 RabbitMQ 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kafka-topics.sh",
    "mqtt"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# rabbitmqctl

> RabbitMQ 消息队列管理 CLI

## 安装

```bash
随 RabbitMQ 安装
```

## 用法

```
rabbitmqctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `list_queues` | 列出队列 |
| `list_exchanges` |  |
| `add_user` |  |
| `set_permissions` |  |

## 示例

### 示例 1: 列出队列

```bash
rabbitmqctl list_queues
```

### 示例 2: 添加管理员

```bash
rabbitmqctl add_user admin password && rabbitmqctl set_user_tags admin administrator
```

## 关联命令

- [[kafka-topics.sh]]

## 风险提示

> ⚠️ **MEDIUM**: 修改用户/权限会影响消息队列访问，请确认策略

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
