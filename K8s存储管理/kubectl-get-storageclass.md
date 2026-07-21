---
{
  "cmd_name": "kubectl get storageclass",
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

# kubectl get storageclass

> List StorageClass resources defining storage provisioners

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get storageclass [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | Output format: wide, yaml, json |

## 示例

### 示例 1: List all storage classes

```bash
kubectl get sc
```

### 示例 2: Get detailed YAML of storage classes

```bash
kubectl get sc -o yaml
```

### 示例 3: Describe specific storage class

```bash
kubectl describe sc fast-ssd
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows storage provisioners

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
