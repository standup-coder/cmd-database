---
{
  "cmd_name": "ycqlsh",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 YugabyteDB 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cqlsh",
    "ysqlsh"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# ycqlsh

> YugabyteDB Cassandra 兼容 CQL Shell

## 安装

```bash
随 YugabyteDB 安装
```

## 用法

```
ycqlsh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 执行 CQL |
| `-k` | keyspace |
| `--ssl` |  |

## 示例

### 示例 1: 连接 YCQL

```bash
ycqlsh localhost 9042
```

### 示例 2: 列出 keyspace

```bash
ycqlsh -e 'DESCRIBE KEYSPACES;'
```

## 关联命令

- [[cqlsh]]
- [[ysqlsh]]

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
