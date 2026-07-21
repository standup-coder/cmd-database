---
{
  "cmd_name": "istioctl proxy-config",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "Istio service mesh installation",
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

# istioctl proxy-config

> Inspect Envoy proxy configuration

## 安装

```bash
Istio service mesh installation
```

## 用法

```
istioctl proxy-config [resource-type] [pod-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `clusters` | Show cluster configuration |
| `listeners` | Show listener configuration |
| `routes` | Show route configuration |

## 示例

### 示例 1: Show listener configuration for specific pod

```bash
istioctl proxy-config listeners myapp-pod-123456-abcde
```

### 示例 2: Show cluster config in production namespace

```bash
istioctl proxy-config clusters myapp-pod -n production
```

### 示例 3: Show specific route configuration

```bash
istioctl proxy-config routes myapp-pod --name http.80
```

## 风险提示

> ⚠️ **LOW**: Read-only configuration inspection

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
