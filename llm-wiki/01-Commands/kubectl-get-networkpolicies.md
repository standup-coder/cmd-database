---
{
  "cmd_name": "kubectl get networkpolicies",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
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
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# kubectl get networkpolicies

> List NetworkPolicy resources for traffic control

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get networkpolicies [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List network policies in production namespace

```bash
kubectl get netpol -n production
```

### 示例 2: List policies across all namespaces

```bash
kubectl get netpol -A
```

### 示例 3: Describe specific network policy

```bash
kubectl describe netpol allow-frontend -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows network restrictions

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
