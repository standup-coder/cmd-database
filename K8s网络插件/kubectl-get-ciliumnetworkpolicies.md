---
{
  "cmd_name": "kubectl get ciliumnetworkpolicies",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "kubectl with Cilium installed",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-network.yaml"
}
---

# kubectl get ciliumnetworkpolicies

> List CiliumNetworkPolicy resources for advanced networking

## 安装

```bash
kubectl with Cilium installed
```

## 用法

```
kubectl get ciliumnetworkpolicies [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List Cilium policies in production namespace

```bash
kubectl get cnp -n production
```

### 示例 2: List policies across all namespaces

```bash
kubectl get cnp -A
```

### 示例 3: Describe specific Cilium policy

```bash
kubectl describe cnp app-policy -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows advanced policies

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
