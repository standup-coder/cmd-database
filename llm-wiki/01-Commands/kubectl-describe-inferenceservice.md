---
{
  "cmd_name": "kubectl describe inferenceservice",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires KServe CRDs installed",
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

# kubectl describe inferenceservice

> Show detailed information about KServe InferenceService

## 安装

```bash
Requires KServe CRDs installed
```

## 用法

```
kubectl describe inferenceservice <name> [flags]
```

```
kubectl describe isvc <name> [flags]
```

## 示例

### 示例 1: Show details of sklearn-iris inference service

```bash
kubectl describe isvc sklearn-iris
```

### 示例 2: Describe inference service in production namespace

```bash
kubectl describe isvc -n production my-model
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
