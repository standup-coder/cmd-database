---
{
  "cmd_name": "kubectl get pvc",
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

# kubectl get pvc

> List PersistentVolumeClaim resources

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get pvc [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |
| `-o` | Output format: wide, yaml, json |

## 示例

### 示例 1: List PVCs in production namespace

```bash
kubectl get pvc -n production
```

### 示例 2: List all PVCs with detailed info

```bash
kubectl get pvc -A -o wide
```

### 示例 3: Describe specific PVC

```bash
kubectl describe pvc data-volume -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows volume claims

## 所属维度

[[Kubernetes Storage Management-MOC|Kubernetes Storage Management]]
