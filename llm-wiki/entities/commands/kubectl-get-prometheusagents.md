---
cmd_name: kubectl get prometheusagents
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: kubectl with Prometheus Operator v0.64+
cmd_platforms:
- linux
- darwin
- windows
summary: "List Prometheus Agent mode instances for lightweight monitoring"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- agent
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# kubectl get prometheusagents

> List Prometheus Agent mode instances for lightweight monitoring

## 安装

```bash
kubectl with Prometheus Operator v0.64+
```

## 用法

```
kubectl get prometheusagents [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List Prometheus agents in monitoring namespace

```bash
kubectl get prometheusagents -n monitoring
```

### 示例 2: Describe agent configuration for edge monitoring

```bash
kubectl describe prometheusagent edge-monitor -n monitoring
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; requires Prometheus Agent CRDs

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
