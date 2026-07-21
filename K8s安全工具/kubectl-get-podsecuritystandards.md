---
{
  "cmd_name": "kubectl get podsecuritystandards",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "kubectl built-in command (v1.23+)",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# kubectl get podsecuritystandards

> Check PodSecurity admission labels on namespaces (v1.23+)

## 安装

```bash
kubectl built-in command (v1.23+)
```

## 用法

```
kubectl get ns -o custom-columns=NAME:.metadata.name,PSA-LABEL:.metadata.labels.pod-security\.enforce
```

## 示例

### 示例 1: Check PodSecurity enforce level on all namespaces

```bash
kubectl get ns -o custom-columns=NAME:.metadata.name,PSA-LABEL:.metadata.labels.pod-security\.enforce
```

### 示例 2: Set namespace PodSecurity level to restricted

```bash
kubectl label namespace my-ns pod-security.kubernetes.io/enforce=restricted
```

## 风险提示

> ⚠️ **MEDIUM**: Changing enforce level may prevent pods from starting

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
