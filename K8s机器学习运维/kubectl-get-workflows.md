---
{
  "cmd_name": "kubectl get workflows",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires Kubeflow Pipelines",
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

# kubectl get workflows

> List Kubeflow Pipelines workflows

## 安装

```bash
Requires Kubeflow Pipelines
```

## 用法

```
kubectl get workflows [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-o wide` | Show additional details |

## 示例

### 示例 1: List pipeline workflows

```bash
kubectl get workflows -n kubeflow
```

### 示例 2: List workflows for specific pipeline run

```bash
kubectl get workflows -l pipeline/runid=abc123
```

### 示例 3: Get workflow details

```bash
kubectl describe workflow my-pipeline-run
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
