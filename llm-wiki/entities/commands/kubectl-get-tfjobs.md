---
cmd_name: kubectl get tfjobs
cmd_category: "容器编排/K8s机器学习运维"
cmd_dimension: Kubernetes MLOps
cmd_install: Requires Kubeflow Training Operator
cmd_platforms:
- linux
- darwin
- windows
summary: "List Kubeflow TensorFlow training jobs"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-mlops.yaml
---


# kubectl get tfjobs

> List Kubeflow TensorFlow training jobs

## 安装

```bash
Requires Kubeflow Training Operator
```

## 用法

```
kubectl get tfjobs [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-o wide` | Show additional details |

## 示例

### 示例 1: List TensorFlow training jobs

```bash
kubectl get tfjobs
```

### 示例 2: List TFJobs in training namespace

```bash
kubectl get tfjobs -n training
```

### 示例 3: Get details of specific TFJob

```bash
kubectl describe tfjob mnist-training
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
