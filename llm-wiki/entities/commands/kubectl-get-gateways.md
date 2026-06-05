---
cmd_name: kubectl get gateways
cmd_category: "容器编排/K8s网络插件"
cmd_dimension: Kubernetes Networking
cmd_install: kubectl with Gateway API CRDs installed
cmd_platforms:
- linux
- darwin
- windows
summary: "List Gateway resources (Gateway API)"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-network.yaml
---


# kubectl get gateways

> List Gateway resources (Gateway API)

## 安装

```bash
kubectl with Gateway API CRDs installed
```

## 用法

```
kubectl get gateways [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List gateways in production namespace

```bash
kubectl get gateways -n production
```

### 示例 2: List gateways across all namespaces

```bash
kubectl get gateways -A
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows gateway resources

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
