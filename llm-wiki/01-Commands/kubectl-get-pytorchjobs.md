---
{
  "cmd_name": "kubectl get pytorchjobs",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires Kubeflow Training Operator",
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

# kubectl get pytorchjobs

> List Kubeflow PyTorch training jobs

## 安装

```bash
Requires Kubeflow Training Operator
```

## 用法

```
kubectl get pytorchjobs [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-o wide` | Show additional details |

## 示例

### 示例 1: List PyTorch training jobs

```bash
kubectl get pytorchjobs
```

### 示例 2: List PyTorchJobs in ml-training namespace

```bash
kubectl get pytorchjobs -n ml-training
```

### 示例 3: Get details of specific PyTorchJob

```bash
kubectl describe pytorchjob bert-finetune
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
