---
cmd_name: kubectl get rolebindings
cmd_category: "容器编排/K8s安全工具"
cmd_dimension: Kubernetes Security
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "List RoleBinding resources linking users to roles"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-security.yaml
---


# kubectl get rolebindings

> List RoleBinding resources linking users to roles

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get rolebindings [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List role bindings in production namespace

```bash
kubectl get rolebindings -n production
```

### 示例 2: List role bindings across all namespaces

```bash
kubectl get rolebindings -A
```

### 示例 3: Describe specific role binding

```bash
kubectl describe rolebinding dev-team-rb -n development
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows access assignments

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
