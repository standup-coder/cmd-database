---
{
  "cmd_name": "kubectl top pvc",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl with metrics-server and storage metrics",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-storage-management.yaml"
}
---

# kubectl top pvc

> Show PVC resource usage (if metrics available)

## 安装

```bash
kubectl with metrics-server and storage metrics
```

## 用法

```
kubectl top pvc [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: Show PVC usage in production namespace

```bash
kubectl top pvc -n production
```

### 示例 2: Show usage across all namespaces

```bash
kubectl top pvc -A
```

## 风险提示

> ⚠️ **LOW**: Read-only metrics display

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
