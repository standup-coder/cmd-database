---
{
  "cmd_name": "kubectl get csistoragecapacities",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl with CSI storage capacity tracking",
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

# kubectl get csistoragecapacities

> List CSIStorageCapacity resources showing storage availability

## 安装

```bash
kubectl with CSI storage capacity tracking
```

## 用法

```
kubectl get csistoragecapacities [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List storage capacities in production namespace

```bash
kubectl get csistoragecapacities -n production
```

### 示例 2: List capacities across all namespaces

```bash
kubectl get csistoragecapacities -A
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows storage availability

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
