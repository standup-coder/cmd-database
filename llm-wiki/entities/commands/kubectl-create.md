---
cmd_name: kubectl create
cmd_category: "容器编排/Kubernetes命令"
cmd_dimension: Container Orchestration
cmd_install: Download from https://kubernetes.io/docs/tasks/tools/
cmd_platforms:
- linux
- darwin
- windows
summary: "Create a resource from a file or stdin"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/kubernetes.yaml
---


# kubectl create

> Create a resource from a file or stdin

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl create [resource] [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Filename to use to create the resource |
| `-n` | Target namespace |

## 示例

### 示例 1: Create resource from file

```bash
kubectl create -f pod.yaml
```

### 示例 2: Create a new namespace

```bash
kubectl create namespace production
```

### 示例 3: Create deployment from image

```bash
kubectl create deployment nginx --image=nginx
```

## 风险提示

> ⚠️ **MEDIUM**: Creates new resources in cluster

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
