---
{
  "cmd_name": "kubectl delete pvc",
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

# kubectl delete pvc

> Delete PersistentVolumeClaim resources

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl delete pvc [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `--force` | Force deletion (dangerous) |

## 示例

### 示例 1: Delete unused PVC

```bash
kubectl delete pvc old-data-volume -n development
```

### 示例 2: Delete all PVCs in test namespace

```bash
kubectl delete pvc --all -n test
```

## 风险提示

> ⚠️ **CRITICAL**: Deletes persistent data permanently

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
