---
{
  "cmd_name": "kubectl taint nodes",
  "cmd_category": "Kubernetes Cluster Management",
  "cmd_dimension": "Kubernetes Cluster Management",
  "cmd_install": "kubectl built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# kubectl taint nodes

> Add or remove taints from nodes

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl taint nodes [node-name] [key]=[value]:[effect]
```

## 示例

### 示例 1: Add NoSchedule taint to node

```bash
kubectl taint nodes worker-node-1 key=value:NoSchedule
```

### 示例 2: Add NoExecute taint to node

```bash
kubectl taint nodes worker-node-1 key=value:NoExecute
```

### 示例 3: Remove NoSchedule taint from node

```bash
kubectl taint nodes worker-node-1 key:NoSchedule-
```

## 风险提示

> ⚠️ **MEDIUM**: Affects pod scheduling; may cause service disruption

## 所属维度

[[Kubernetes Cluster Management-MOC|Kubernetes Cluster Management]]
