---
cmd_name: promtool query instant
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Installed with Prometheus
cmd_platforms:
- linux
- darwin
- windows
summary: "Execute instant PromQL query"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# promtool query instant

> Execute instant PromQL query

## 安装

```bash
Installed with Prometheus
```

## 用法

```
promtool query instant [server-url] [query]
```

## 示例

### 示例 1: Query instance status

```bash
promtool query instant http://localhost:9090 'up'
```

### 示例 2: Query request rate

```bash
promtool query instant http://localhost:9090 'rate(http_requests_total[5m])'
```

### 示例 3: Query memory metrics

```bash
promtool query instant http://localhost:9090 'node_memory_MemAvailable_bytes'
```

## 风险提示

> ⚠️ **LOW**: Read-only query operation

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
