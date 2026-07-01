---
{
  "cmd_name": "pgbench",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 PostgreSQL 客户端安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "psql",
    "pg_dump"
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

# pgbench

> PostgreSQL 基准测试工具

## 安装

```bash
随 PostgreSQL 客户端安装
```

## 用法

```
pgbench [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 初始化测试数据 |
| `-c` | 并发客户端 |
| `-t` | 每个客户端事务数 |
| `-T` | 测试时长 |

## 示例

### 示例 1: 初始化测试数据

```bash
pgbench -i mydb
```

### 示例 2: 10 并发压测 60 秒

```bash
pgbench -c 10 -T 60 mydb
```

## 关联命令

- [[psql]]
- [[pg_dump]]

## 风险提示

> ⚠️ **HIGH**: 压测会消耗 PG 资源，请在测试实例上执行

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
