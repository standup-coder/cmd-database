---
{
  "cmd_name": "clickhouse-client",
  "cmd_category": "数据库工具/时序与OLAP",
  "cmd_dimension": "时序与OLAP",
  "cmd_install": "随 ClickHouse 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "psql",
    "influx"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/timeseries.yaml"
}
---

# clickhouse-client

> ClickHouse 交互式 SQL 客户端

## 安装

```bash
随 ClickHouse 安装
```

## 用法

```
clickhouse-client [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--host` | 服务器地址 |
| `--query` | 执行 SQL 查询 |
| `--format` | 输出格式（如 JSONEachRow） |

## 示例

### 示例 1: 查询系统表

```bash
clickhouse-client --query "SELECT * FROM system.tables LIMIT 10"
```

### 示例 2: 远程统计 events 表行数

```bash
clickhouse-client --host ch.example.com --query "SELECT count() FROM events"
```

## 关联命令

- [[psql]]
- [[influx]]

## 风险提示

> ⚠️ **MEDIUM**: ClickHouse 查询可能扫描亿级数据，请关注内存和 IO 消耗

## 所属维度

[[时序与OLAP-MOC|数据库工具/时序与OLAP]]
