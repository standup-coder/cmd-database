---
{
  "cmd_name": "kubectl get ciliumclusterwidenetworkpolicies",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "kubectl with Cilium installed",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-network.yaml"
}
---

# kubectl get ciliumclusterwidenetworkpolicies

> List CiliumClusterwideNetworkPolicy resources

## 安装

```bash
kubectl with Cilium installed
```

## 用法

```
kubectl get ciliumclusterwidenetworkpolicies [name] [flags]
```

## 示例

### 示例 1: List cluster-wide Cilium policies

```bash
kubectl get ccnp
```

### 示例 2: Describe cluster-wide policy

```bash
kubectl describe ccnp deny-all-traffic
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows cluster policies

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
