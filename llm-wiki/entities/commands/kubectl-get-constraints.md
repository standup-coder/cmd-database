---
cmd_name: kubectl get constraints
cmd_category: "容器编排/K8s安全工具"
cmd_dimension: Kubernetes Security
cmd_install: kubectl with OPA Gatekeeper installed
cmd_platforms:
- linux
- darwin
- windows
summary: "List Constraint resources enforcing policies"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-security.yaml
---


# kubectl get constraints

> List Constraint resources enforcing policies

## 安装

```bash
kubectl with OPA Gatekeeper installed
```

## 用法

```
kubectl get constraints [constraint-type] [name] [flags]
```

## 示例

### 示例 1: List required labels constraints

```bash
kubectl get k8srequiredlabels
```

### 示例 2: Describe namespace labeling requirement

```bash
kubectl describe k8srequiredlabels require-namespace-labels
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows enforced policies

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
