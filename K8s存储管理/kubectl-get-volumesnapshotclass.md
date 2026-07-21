---
{
  "cmd_name": "kubectl get volumesnapshotclass",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl with CSI snapshot controller",
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

# kubectl get volumesnapshotclass

> List VolumeSnapshotClass resources defining snapshot provisioners

## 安装

```bash
kubectl with CSI snapshot controller
```

## 用法

```
kubectl get volumesnapshotclass [name] [flags]
```

## 示例

### 示例 1: List all volume snapshot classes

```bash
kubectl get volumesnapshotclass
```

### 示例 2: Describe specific snapshot class

```bash
kubectl describe volumesnapshotclass csi-hostpath-snapclass
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows snapshot provisioners

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
