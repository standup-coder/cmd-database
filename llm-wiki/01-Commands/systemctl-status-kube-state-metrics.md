---
{
  "cmd_name": "systemctl status kube-state-metrics",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Usually deployed as Kubernetes deployment",
  "cmd_platforms": [
    "linux"
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

# systemctl status kube-state-metrics

> Check kube-state-metrics service status

## 安装

```bash
Usually deployed as Kubernetes deployment
```

## 用法

```
systemctl status kube-state-metrics
```

## 示例

### 示例 1: View kube-state-metrics status

```bash
systemctl status kube-state-metrics
```

### 示例 2: Start kube-state-metrics service

```bash
systemctl start kube-state-metrics
```

### 示例 3: Restart kube-state-metrics service

```bash
systemctl restart kube-state-metrics
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
