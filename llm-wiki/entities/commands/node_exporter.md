---
cmd_name: node_exporter
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Download from https://prometheus.io/download/
cmd_platforms:
- linux
- darwin
summary: "Start Prometheus Node Exporter for hardware and OS metrics"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# node_exporter

> Start Prometheus Node Exporter for hardware and OS metrics

## 安装

```bash
Download from https://prometheus.io/download/
```

## 用法

```
node_exporter [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--web.listen-address` | Listen address for metrics |
| `--collector.disable` | Disable specific collectors |

## 示例

### 示例 1: Start with default settings

```bash
node_exporter
```

### 示例 2: Start on specific port

```bash
node_exporter --web.listen-address=:9100
```

### 示例 3: Start with selected collectors

```bash
node_exporter --collector.disable-defaults --collector.cpu --collector.meminfo
```

## 风险提示

> ⚠️ **LOW**: Exposes system metrics; ensure proper access control

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
