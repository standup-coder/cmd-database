---
{
  "cmd_name": "kubectl get volumesnapshot",
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

# kubectl get volumesnapshot

> List VolumeSnapshot resources for backup and restore

## 安装

```bash
kubectl with CSI snapshot controller
```

## 用法

```
kubectl get volumesnapshot [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List volume snapshots in production namespace

```bash
kubectl get volumesnapshot -n production
```

### 示例 2: List snapshots across all namespaces

```bash
kubectl get volumesnapshot -A
```

### 示例 3: Describe specific volume snapshot

```bash
kubectl describe volumesnapshot db-backup-20260204 -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows backup snapshots

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
