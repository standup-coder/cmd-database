---
cmd_name: kubectl get prometheuses
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: kubectl with Prometheus Operator CRDs
cmd_platforms:
- linux
- darwin
- windows
summary: "List Prometheus instances managed by Prometheus Operator"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# kubectl get prometheuses

> List Prometheus instances managed by Prometheus Operator

## 安装

```bash
kubectl with Prometheus Operator CRDs
```

## 用法

```
kubectl get prometheuses [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |
| `-o` | Output format (wide, yaml, json) |

## 示例

### 示例 1: List Prometheus instances in monitoring namespace

```bash
kubectl get prometheuses -n monitoring
```

### 示例 2: List all Prometheus instances with detailed info

```bash
kubectl get prometheuses -A -o wide
```

### 示例 3: Get detailed YAML configuration

```bash
kubectl get prometheuses kube-prometheus-stack-prometheus -n monitoring -o yaml
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; requires Prometheus Operator

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
