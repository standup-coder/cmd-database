---
{
  "cmd_name": "kubectl get csidrivers",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl built-in command",
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

# kubectl get csidrivers

> List CSIDriver resources for Container Storage Interface drivers

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get csidrivers [name] [flags]
```

## 示例

### 示例 1: List all CSI drivers

```bash
kubectl get csidrivers
```

### 示例 2: Describe specific CSI driver

```bash
kubectl describe csidriver hostpath.csi.k8s.io
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows storage drivers

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
