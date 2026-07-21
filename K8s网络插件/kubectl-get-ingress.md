---
{
  "cmd_name": "kubectl get ingress",
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
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-network.yaml"
}
---

# kubectl get ingress

> List Ingress resources for external access

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get ingress [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |
| `-o` | Output format (wide, yaml, json) |

## 示例

### 示例 1: List ingresses in production namespace

```bash
kubectl get ingress -n production
```

### 示例 2: List all ingresses with detailed info

```bash
kubectl get ingress -A -o wide
```

### 示例 3: Describe specific ingress configuration

```bash
kubectl describe ingress myapp-ingress -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows routing rules

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
