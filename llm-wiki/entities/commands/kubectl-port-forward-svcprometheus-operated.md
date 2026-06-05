---
cmd_name: kubectl port-forward svc/prometheus-operated
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "Port forward to access Prometheus web UI"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# kubectl port-forward svc/prometheus-operated

> Port forward to access Prometheus web UI

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl port-forward svc/[prometheus-service] [local-port]:9090
```

## 示例

### 示例 1: Access Prometheus UI locally on port 9090

```bash
kubectl port-forward svc/prometheus-operated 9090:9090 -n monitoring
```

### 示例 2: Access Prometheus from kube-prometheus-stack

```bash
kubectl port-forward svc/kube-prometheus-stack-prometheus 9090:9090 -n monitoring
```

### 示例 3: Access Thanos Query frontend

```bash
kubectl port-forward svc/thanos-query 9090:9090 -n monitoring
```

## 风险提示

> ⚠️ **MEDIUM**: Exposes monitoring interface; may contain sensitive metrics

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
