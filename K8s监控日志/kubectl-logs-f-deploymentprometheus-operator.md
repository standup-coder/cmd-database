---
{
  "cmd_name": "kubectl logs -f deployment/prometheus-operator",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# kubectl logs -f deployment/prometheus-operator

> Stream logs from Prometheus Operator for troubleshooting

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl logs -f deployment/[prometheus-operator-deployment] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `--since` | Show logs from specific time |
| `--tail` | Number of lines to show from end |

## 示例

### 示例 1: Stream operator logs for real-time monitoring

```bash
kubectl logs -f deployment/prometheus-operator -n monitoring
```

### 示例 2: View last hour of operator logs

```bash
kubectl logs deployment/prometheus-operator -n monitoring --since=1h
```

### 示例 3: View last 100 lines of logs

```bash
kubectl logs deployment/prometheus-operator -n monitoring --tail=100
```

## 风险提示

> ⚠️ **LOW**: Read-only log viewing; may contain sensitive information

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
