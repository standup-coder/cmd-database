---
cmd_name: amtool alert query
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Installed with Alertmanager
cmd_platforms:
- linux
- darwin
- windows
summary: "Query active alerts from Alertmanager"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# amtool alert query

> Query active alerts from Alertmanager

## 安装

```bash
Installed with Alertmanager
```

## 用法

```
amtool alert query [matcher]
```

## 示例

### 示例 1: List all active alerts

```bash
amtool alert query
```

### 示例 2: Query specific alert

```bash
amtool alert query alertname=HighCPU
```

### 示例 3: Query critical alerts

```bash
amtool alert query --alertmanager.url=http://localhost:9093 severity=critical
```

## 风险提示

> ⚠️ **LOW**: Read-only query operation

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
