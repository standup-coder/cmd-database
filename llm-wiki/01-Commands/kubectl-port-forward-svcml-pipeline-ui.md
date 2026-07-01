---
{
  "cmd_name": "kubectl port-forward svc/ml-pipeline-ui",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires Kubeflow Pipelines deployed",
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

# kubectl port-forward svc/ml-pipeline-ui

> Access Kubeflow Pipelines UI locally

## 安装

```bash
Requires Kubeflow Pipelines deployed
```

## 用法

```
kubectl port-forward svc/ml-pipeline-ui <local-port>:80 -n kubeflow
```

## 示例

### 示例 1: Forward Pipelines UI to localhost:8080

```bash
kubectl port-forward svc/ml-pipeline-ui 8080:80 -n kubeflow
```

### 示例 2: Run port-forward in background

```bash
kubectl port-forward svc/ml-pipeline-ui 3000:80 -n kubeflow &
```

## 风险提示

> ⚠️ **LOW**: Local port forwarding only

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
