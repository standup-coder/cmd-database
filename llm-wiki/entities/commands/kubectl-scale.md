---
cmd_name: kubectl scale
cmd_category: "容器编排/Kubernetes命令"
cmd_dimension: Container Orchestration
cmd_install: Download from https://kubernetes.io/docs/tasks/tools/
cmd_platforms:
- linux
- darwin
- windows
summary: "Set a new size for a deployment, replica set, or replication controller"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/kubernetes.yaml
---


# kubectl scale

> Set a new size for a deployment, replica set, or replication controller

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl scale [resource] [name] --replicas=[count]
```

## 参数

| Flag | Description |
|------|-------------|
| `--replicas` | Number of replicas |
| `-n` | Namespace |

## 示例

### 示例 1: Scale deployment to 3 replicas

```bash
kubectl scale deployment nginx --replicas=3
```

### 示例 2: Scale down to zero (stop all pods)

```bash
kubectl scale deployment nginx --replicas=0
```

### 示例 3: Scale statefulset to 5 replicas

```bash
kubectl scale statefulset mysql --replicas=5
```

## 风险提示

> ⚠️ **HIGH**: Scaling to 0 stops all instances; can cause service outage

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
