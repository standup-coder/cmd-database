---
cmd_name: prometheus
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Download from https://prometheus.io/download/
cmd_platforms:
- linux
- darwin
- windows
summary: "Start Prometheus monitoring server"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# prometheus

> Start Prometheus monitoring server

## 安装

```bash
Download from https://prometheus.io/download/
```

## 用法

```
prometheus [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config.file` | Prometheus configuration file path |
| `--web.listen-address` | Address to listen on for web interface |
| `--storage.tsdb.path` | Base path for metrics storage |

## 示例

### 示例 1: Start Prometheus with config file

```bash
prometheus --config.file=prometheus.yml
```

### 示例 2: Start Prometheus on specific port

```bash
prometheus --config.file=prometheus.yml --web.listen-address=:9090
```

### 示例 3: Start with custom storage path

```bash
prometheus --config.file=prometheus.yml --storage.tsdb.path=/data/prometheus
```

## 风险提示

> ⚠️ **MEDIUM**: Running with incorrect config may impact monitoring

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
