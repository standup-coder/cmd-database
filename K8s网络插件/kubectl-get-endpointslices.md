---
{
  "cmd_name": "kubectl get endpointslices",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "kubectl built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "rlhf",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-network.yaml"
}
---

# kubectl get endpointslices

> List EndpointSlice resources showing service endpoints

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get endpointslices [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List endpoint slices in production namespace

```bash
kubectl get endpointslices -n production
```

### 示例 2: Describe specific endpoint slice

```bash
kubectl describe endpointslice myapp-endpointslice -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows service topology

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
