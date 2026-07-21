---
{
  "cmd_name": "kubectl get notebooks",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires Kubeflow Notebooks component",
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
  "source_file": "data/container/k8s/k8s-mlops.yaml"
}
---

# kubectl get notebooks

> List Kubeflow Notebooks

## 安装

```bash
Requires Kubeflow Notebooks component
```

## 用法

```
kubectl get notebooks [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-o wide` | Show additional details |

## 示例

### 示例 1: List notebooks in user namespace

```bash
kubectl get notebooks -n kubeflow-user
```

### 示例 2: List all notebooks across namespaces

```bash
kubectl get notebooks -A
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
