---
{
  "cmd_name": "kubectl delete pv",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "rag",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-storage-management.yaml"
}
---

# kubectl delete pv

> Delete PersistentVolume resources

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl delete pv [name] [flags]
```

## 示例

### 示例 1: Delete orphaned persistent volume

```bash
kubectl delete pv orphaned-pv-12345
```

### 示例 2: Delete all PVs (very dangerous)

```bash
kubectl delete pv --all
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes storage volumes

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
