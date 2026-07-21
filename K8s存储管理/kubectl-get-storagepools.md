---
{
  "cmd_name": "kubectl get storagepools",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl with specific storage provider CRDs",
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

# kubectl get storagepools

> List StoragePool resources (specific storage systems)

## 安装

```bash
kubectl with specific storage provider CRDs
```

## 用法

```
kubectl get storagepools [name] [flags]
```

## 示例

### 示例 1: List storage pools (depends on storage provider)

```bash
kubectl get storagepools
```

### 示例 2: Describe specific storage pool

```bash
kubectl describe storagepool pool-ssd-fast
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows storage pools

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
