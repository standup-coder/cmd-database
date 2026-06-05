---
cmd_name: kubectl label nodes
cmd_category: "容器编排/K8s集群管理"
cmd_dimension: Kubernetes Cluster Management
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "Add or remove labels from nodes"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-cluster.yaml
---


# kubectl label nodes

> Add or remove labels from nodes

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl label nodes [node-name] [key]=[value]
```

## 示例

### 示例 1: Add label to node

```bash
kubectl label nodes worker-node-1 disktype=ssd
```

### 示例 2: Remove label from node

```bash
kubectl label nodes worker-node-1 disktype-
```

### 示例 3: Label all nodes

```bash
kubectl label nodes --all disktype=ssd
```

## 风险提示

> ⚠️ **LOW**: Labels affect scheduling but don't impact running pods

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
