---
cmd_name: kubectl apply -f inferenceservice.yaml
cmd_category: "容器编排/K8s机器学习运维"
cmd_dimension: Kubernetes MLOps
cmd_install: kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve.yaml
cmd_platforms:
- linux
- darwin
- windows
summary: "Deploy a KServe InferenceService"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-mlops.yaml
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

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
