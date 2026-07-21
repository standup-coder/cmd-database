---
{
  "cmd_name": "kubectl get scrapeconfigs",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "kubectl with Prometheus Operator v0.65+",
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

# kubectl get scrapeconfigs

> List ScrapeConfig resources for external target monitoring

## 安装

```bash
kubectl with Prometheus Operator v0.65+
```

## 用法

```
kubectl get scrapeconfigs [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List scrape configurations in monitoring namespace

```bash
kubectl get scrapeconfigs -n monitoring
```

### 示例 2: Describe external database monitoring config

```bash
kubectl describe scrapeconfig external-db-monitor -n monitoring
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows external monitoring targets

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
