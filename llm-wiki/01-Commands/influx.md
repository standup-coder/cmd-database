---
{
  "cmd_name": "influx",
  "cmd_category": "数据库工具/时序与OLAP",
  "cmd_dimension": "时序与OLAP",
  "cmd_install": "参考 https://docs.influxdata.com/influxdb/latest/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "clickhouse-client"
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

# influx

> InfluxDB 命令行客户端

## 安装

```bash
参考 https://docs.influxdata.com/influxdb/latest/install/
```

## 用法

```
influx [OPTIONS] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `query` | 执行 Flux 或 InfluxQL 查询 |
| `bucket` | 管理 bucket |
| `--host` | InfluxDB 服务器地址 |

## 示例

### 示例 1: 查询最近 1 小时的时序数据

```bash
influx query 'from(bucket:"metrics") |> range(start:-1h)'
```

### 示例 2: 列出所有 bucket

```bash
influx bucket list
```

## 关联命令

- [[clickhouse-client]]

## 风险提示

> ⚠️ **MEDIUM**: 删除 bucket 或大量数据不可恢复，请确认保留策略

## 所属维度

[[时序与OLAP-MOC|数据库工具/时序与OLAP]]
