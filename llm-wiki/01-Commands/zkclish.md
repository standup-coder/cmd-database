---
{
  "cmd_name": "zkCli.sh",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Apache ZooKeeper 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "zookeeper-shell",
    "kafka-topics.sh"
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

# zkCli.sh

> ZooKeeper 命令行客户端

## 安装

```bash
随 Apache ZooKeeper 安装
```

## 用法

```
zkCli.sh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-server` | 服务器 |
| `-timeout` | 超时 |

## 示例

### 示例 1: 连接 ZooKeeper

```bash
zkCli.sh -server localhost:2181
```

### 示例 2: 列出根节点

```bash
echo 'ls /' | zkCli.sh -server localhost:2181
```

## 关联命令

- [[zookeeper-shell]]
- [[kafka-topics.sh]]

## 风险提示

> ⚠️ **MEDIUM**: 删除 ZooKeeper 节点会影响依赖服务，请确认

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
