---
{
  "cmd_name": "neo4j-admin",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Neo4j 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "cypher-shell",
    "neo4j"
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

# neo4j-admin

> Neo4j 图数据库管理工具

## 安装

```bash
随 Neo4j 安装
```

## 用法

```
neo4j-admin [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `database` | 管理数据库 |
| `dump` | 备份 |
| `load` | 恢复 |
| `check-consistency` |  |

## 示例

### 示例 1: 备份数据库

```bash
neo4j-admin database dump neo4j --to-path=/backup
```

### 示例 2: 恢复数据库

```bash
neo4j-admin database load neo4j --from-path=/backup
```

## 关联命令

- [[cypher-shell]]

## 风险提示

> ⚠️ **HIGH**: dump/load 会操作数据库文件，操作前请停止服务并备份

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
