---
cmd_name: kubectl get ingressclasses
cmd_category: "容器编排/K8s网络插件"
cmd_dimension: Kubernetes Networking
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "List IngressClass resources defining ingress controller types"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-network.yaml
---


# kubectl get ingressclasses

> List IngressClass resources defining ingress controller types

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get ingressclasses [name] [flags]
```

## 示例

### 示例 1: List all ingress classes

```bash
kubectl get ingressclasses
```

### 示例 2: Describe nginx ingress class

```bash
kubectl describe ingressclass nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows controller configurations

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
