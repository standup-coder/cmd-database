---
{
  "cmd_name": "kubectl get inferenceservices",
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

# kubectl get inferenceservices

> List KServe InferenceServices

## 安装

```bash
Requires KServe CRDs installed
```

## 用法

```
kubectl get inferenceservices [flags]
```

```
kubectl get isvc [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n, --namespace` | Specify namespace |
| `-A, --all-namespaces` | List across all namespaces |
| `-o wide` | Show additional details |

## 示例

### 示例 1: List all inference services in current namespace

```bash
kubectl get isvc
```

### 示例 2: List all inference services across namespaces

```bash
kubectl get isvc -A
```

### 示例 3: Get detailed YAML output for specific service

```bash
kubectl get isvc sklearn-iris -o yaml
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
