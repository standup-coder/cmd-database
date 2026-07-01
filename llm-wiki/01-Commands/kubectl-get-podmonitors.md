---
{
  "cmd_name": "kubectl get podmonitors",
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

# kubectl get podmonitors

> List PodMonitor resources for direct pod monitoring

## 安装

```bash
kubectl with Prometheus Operator CRDs
```

## 用法

```
kubectl get podmonitors [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List PodMonitors in monitoring namespace

```bash
kubectl get podmonitors -n monitoring
```

### 示例 2: Describe batch job monitoring configuration

```bash
kubectl describe podmonitor batch-jobs-monitor -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows pod monitoring configs

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
