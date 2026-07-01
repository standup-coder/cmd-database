---
{
  "cmd_name": "kubectl get csinodes",
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

# kubectl get csinodes

> List CSINode resources showing node storage capabilities

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get csinodes [name] [flags]
```

## 示例

### 示例 1: List CSI node information

```bash
kubectl get csinodes
```

### 示例 2: Describe specific node's CSI capabilities

```bash
kubectl describe csinode worker-node-1
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows node storage info

## 所属维度

[[Kubernetes Storage Management-MOC|Kubernetes Storage Management]]
