---
{
  "cmd_name": "kubectl patch storageclass",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-storage-management.yaml"
}
---

# kubectl patch storageclass

> Modify StorageClass configuration

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl patch storageclass [name] -p [patch-content]
```

## 示例

### 示例 1: Remove default storage class annotation

```bash
kubectl patch sc slow-hdd -p '{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
```

### 示例 2: Set storage class as default

```bash
kubectl patch sc fast-ssd -p '{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

## 风险提示

> ⚠️ **MEDIUM**: Changes storage provisioning behavior

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
