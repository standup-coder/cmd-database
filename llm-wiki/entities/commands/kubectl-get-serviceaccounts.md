---
cmd_name: kubectl get serviceaccounts
cmd_category: "容器编排/K8s安全工具"
cmd_dimension: Kubernetes Security
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "List ServiceAccount resources for pod identities"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-security.yaml
---


# kubectl get serviceaccounts

> List ServiceAccount resources for pod identities

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get serviceaccounts [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List service accounts in production namespace

```bash
kubectl get sa -n production
```

### 示例 2: List service accounts across all namespaces

```bash
kubectl get sa -A
```

### 示例 3: Describe default service account

```bash
kubectl describe sa default -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows service account identities

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
