---
cmd_name: kubectl exec -it
cmd_category: "容器编排/K8s存储增强"
cmd_dimension: Kubernetes Storage Management
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "Enter pod to diagnose storage issues"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- rag
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-storage-management.yaml
---


# kubectl exec -it

> Enter pod to diagnose storage issues

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl exec -it [pod-name] -- [command]
```

## 示例

### 示例 1: Check disk space usage in pod

```bash
kubectl exec -it storage-pod -- df -h
```

### 示例 2: List files in mounted volume

```bash
kubectl exec -it storage-pod -- ls -la /data
```

### 示例 3: Monitor I/O statistics

```bash
kubectl exec -it storage-pod -- iostat -x 1 5
```

### 示例 4: Check persistent volume mounts

```bash
kubectl exec -it storage-pod -- mount | grep persistent
```

## 风险提示

> ⚠️ **MEDIUM**: Can execute commands in pod filesystem

## 所属维度

[[K8s存储增强-MOC|Kubernetes Storage Management]]
