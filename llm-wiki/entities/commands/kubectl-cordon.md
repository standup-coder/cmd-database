---
cmd_name: kubectl cordon
cmd_category: "容器编排/Kubernetes命令"
cmd_dimension: Container Orchestration
cmd_install: Download from https://kubernetes.io/docs/tasks/tools/
cmd_platforms:
- linux
- darwin
- windows
summary: "Mark node as unschedulable"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/kubernetes.yaml
---


# kubectl cordon

> Mark node as unschedulable

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl cordon [node-name]
```

## 示例

### 示例 1: Mark node as unschedulable

```bash
kubectl cordon node-1
```

### 示例 2: Mark node as schedulable again

```bash
kubectl uncordon node-1
```

## 风险提示

> ⚠️ **MEDIUM**: Prevents new pods from scheduling on node; existing pods continue running

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
