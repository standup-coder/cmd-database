---
cmd_name: kubectl get clusterrolebindings
cmd_category: "容器编排/K8s安全工具"
cmd_dimension: Kubernetes Security
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "List ClusterRoleBinding resources for cluster-wide access"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-security.yaml
---


# kubectl get clusterrolebindings

> List ClusterRoleBinding resources for cluster-wide access

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get clusterrolebindings [name] [flags]
```

## 示例

### 示例 1: List all cluster role bindings

```bash
kubectl get clusterrolebindings
```

### 示例 2: Describe cluster-admin binding

```bash
kubectl describe clusterrolebinding cluster-admin
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows cluster access mappings

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
