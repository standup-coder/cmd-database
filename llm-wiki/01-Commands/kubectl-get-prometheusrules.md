---
{
  "cmd_name": "kubectl get prometheusrules",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "kubectl with Prometheus Operator CRDs",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# kubectl get prometheusrules

> List PrometheusRule resources containing alerting and recording rules

## 安装

```bash
kubectl with Prometheus Operator CRDs
```

## 用法

```
kubectl get prometheusrules [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List Prometheus rules in monitoring namespace

```bash
kubectl get prometheusrules -n monitoring
```

### 示例 2: List rules across all namespaces

```bash
kubectl get prometheusrules -A
```

### 示例 3: Describe Kubernetes alerting rules

```bash
kubectl describe prometheusrule k8s-alerts -n monitoring
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows alert rules

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
