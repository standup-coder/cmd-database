---
{
  "cmd_name": "kubectl apply -f inferenceservice.yaml",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve.yaml",
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
  "source_file": "data/container/k8s/k8s-mlops.yaml"
}
---

# kubectl apply -f inferenceservice.yaml

> Deploy a KServe InferenceService

## 安装

```bash
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve.yaml
```

## 用法

```
kubectl apply -f inferenceservice.yaml
```

## 示例

### 示例 1: Deploy sklearn model inference service

```bash
kubectl apply -f sklearn-iris.yaml
```

### 示例 2: Deploy PyTorch model to specific namespace

```bash
kubectl apply -n kserve-test -f pytorch-model.yaml
```

## 风险提示

> ⚠️ **MEDIUM**: Deploys model serving resources to cluster

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
