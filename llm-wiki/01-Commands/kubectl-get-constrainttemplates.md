---
{
  "cmd_name": "kubectl get constrainttemplates",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "kubectl with OPA Gatekeeper installed",
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

# kubectl get constrainttemplates

> List ConstraintTemplate resources for OPA Gatekeeper

## 安装

```bash
kubectl with OPA Gatekeeper installed
```

## 用法

```
kubectl get constrainttemplates [name] [flags]
```

## 示例

### 示例 1: List all constraint templates

```bash
kubectl get constrainttemplates
```

### 示例 2: Describe required labels constraint template

```bash
kubectl describe constrainttemplate k8srequiredlabels
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows policy templates

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
