---
cmd_name: kubectl get servicemonitors
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: kubectl with Prometheus Operator CRDs
cmd_platforms:
- linux
- darwin
- windows
summary: "List ServiceMonitor resources for automatic service discovery"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# kubectl get servicemonitors

> List ServiceMonitor resources for automatic service discovery

## 安装

```bash
kubectl with Prometheus Operator CRDs
```

## 用法

```
kubectl get servicemonitors [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List ServiceMonitors in monitoring namespace

```bash
kubectl get servicemonitors -n monitoring
```

### 示例 2: List ServiceMonitors across all namespaces

```bash
kubectl get servicemonitors -A
```

### 示例 3: Describe specific ServiceMonitor configuration

```bash
kubectl describe servicemonitor myapp-monitor -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows monitoring targets

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
