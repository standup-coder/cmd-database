---
{
  "cmd_name": "kubectl port-forward svc/grafana",
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

# kubectl port-forward svc/grafana

> Port forward to access Grafana dashboard

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl port-forward svc/grafana [local-port]:3000
```

## 示例

### 示例 1: Access Grafana dashboard locally on port 3000

```bash
kubectl port-forward svc/grafana 3000:3000 -n monitoring
```

### 示例 2: Access Grafana from kube-prometheus-stack

```bash
kubectl port-forward svc/kube-prometheus-stack-grafana 3000:80 -n monitoring
```

## 风险提示

> ⚠️ **MEDIUM**: Exposes dashboard interface; may contain sensitive data

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
