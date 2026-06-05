---
cmd_name: kubectl get thanosrulers
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: kubectl with Thanos Operator CRDs
cmd_platforms:
- linux
- darwin
- windows
summary: "List Thanos Ruler instances for distributed alerting"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# kubectl get thanosrulers

> List Thanos Ruler instances for distributed alerting

## 安装

```bash
kubectl with Thanos Operator CRDs
```

## 用法

```
kubectl get thanosrulers [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List Thanos rulers in monitoring namespace

```bash
kubectl get thanosrulers -n monitoring
```

### 示例 2: Describe Thanos ruler configuration

```bash
kubectl describe thanosruler production-ruler -n monitoring
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; requires Thanos deployment

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
