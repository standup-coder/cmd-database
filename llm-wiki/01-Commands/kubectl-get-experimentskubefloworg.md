---
{
  "cmd_name": "kubectl get experiments.kubeflow.org",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires Kubeflow Katib component",
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

# kubectl get experiments.kubeflow.org

> List Kubeflow Katib experiments

## 安装

```bash
Requires Kubeflow Katib component
```

## 用法

```
kubectl get experiments.kubeflow.org [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-o wide` | Show additional details |

## 示例

### 示例 1: List Katib experiments

```bash
kubectl get experiments.kubeflow.org
```

### 示例 2: Get experiment details in YAML

```bash
kubectl get experiments.kubeflow.org -n kubeflow -o yaml
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
