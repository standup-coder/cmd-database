---
{
  "cmd_name": "kubectl port-forward svc/alertmanager-operated",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "kubectl built-in command",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# kubectl port-forward svc/alertmanager-operated

> Port forward to access Alertmanager UI

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl port-forward svc/[alertmanager-service] [local-port]:9093
```

## 示例

### 示例 1: Access Alertmanager UI locally on port 9093

```bash
kubectl port-forward svc/alertmanager-operated 9093:9093 -n monitoring
```

### 示例 2: Access Alertmanager from kube-prometheus-stack

```bash
kubectl port-forward svc/kube-prometheus-stack-alertmanager 9093:9093 -n monitoring
```

## 风险提示

> ⚠️ **MEDIUM**: Exposes alert management interface

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
