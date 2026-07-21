---
{
  "cmd_name": "kubectl get httproutes",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "kubectl with Gateway API CRDs installed",
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

# kubectl get httproutes

> List HTTPRoute resources (Gateway API)

## 安装

```bash
kubectl with Gateway API CRDs installed
```

## 用法

```
kubectl get httproutes [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List HTTP routes in production namespace

```bash
kubectl get httproutes -n production
```

### 示例 2: Describe specific HTTP route

```bash
kubectl describe httproute api-route -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows routing rules

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
