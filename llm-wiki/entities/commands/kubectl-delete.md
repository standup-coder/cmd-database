---
cmd_name: kubectl delete
cmd_category: "容器编排/Kubernetes命令"
cmd_dimension: Container Orchestration
cmd_install: Download from https://kubernetes.io/docs/tasks/tools/
cmd_platforms:
- linux
- darwin
- windows
summary: "Delete resources by filenames, resources and names, or by label selectors"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/kubernetes.yaml
---


# kubectl delete

> Delete resources by filenames, resources and names, or by label selectors

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl delete [resource] [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Delete resources defined in file |
| `-n` | Target namespace |
| `-l` | Delete by label selector |
| `--force` | Force immediate deletion |
| `--grace-period` | Period of time in seconds given to resource to terminate gracefully |

## 示例

### 示例 1: Delete a pod

```bash
kubectl delete pod mypod
```

### 示例 2: Delete resources defined in file

```bash
kubectl delete -f deployment.yaml
```

### 示例 3: Delete all pods with label app=nginx

```bash
kubectl delete pods -l app=nginx
```

### 示例 4: Force delete pod immediately

```bash
kubectl delete pod mypod --force --grace-period=0
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes resources; can cause service outages

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
