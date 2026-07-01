---
{
  "cmd_name": "influxd",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://docs.influxdata.com/influxdb/latest/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "influx",
    "telegraf"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# influxd

> InfluxDB 数据库服务守护进程

## 安装

```bash
参考 https://docs.influxdata.com/influxdb/latest/install/
```

## 用法

```
influxd [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bolt-path` |  |
| `--engine-path` |  |
| `--http-bind-address` |  |
| `--reporting-disabled` |  |

## 示例

### 示例 1: 前台启动 InfluxDB

```bash
influxd
```

### 示例 2: 指定 HTTP 地址

```bash
influxd --http-bind-address=:8086
```

## 关联命令

- [[influx]]

## 风险提示

> ⚠️ **MEDIUM**: influxd 会监听网络端口，请配置认证和防火墙

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
