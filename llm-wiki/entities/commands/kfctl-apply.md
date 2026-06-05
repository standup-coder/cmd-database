---
cmd_name: kfctl apply
cmd_category: "容器编排/K8s机器学习运维"
cmd_dimension: Kubernetes MLOps
cmd_install: Download from https://github.com/kubeflow/kfctl/releases
cmd_platforms:
- linux
- darwin
- windows
summary: "Deploy Kubeflow to Kubernetes cluster"
cmd_level: advanced
cmd_related: []
cmd_tags:
- kubernetes
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/k8s-mlops.yaml
---


# kfctl apply

> Deploy Kubeflow to Kubernetes cluster

## 安装

```bash
Download from https://github.com/kubeflow/kfctl/releases
```

## 用法

```
kfctl apply -f <config-file> [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Path to Kubeflow config file |
| `-V` | Verbose output |

## 示例

### 示例 1: Deploy Kubeflow with Istio

```bash
kfctl apply -f kfctl_k8s_istio.yaml
```

### 示例 2: Deploy Kubeflow on AWS with verbose output

```bash
kfctl apply -f kfctl_aws.yaml -V
```

## 风险提示

> ⚠️ **CRITICAL**: Deploys full Kubeflow stack; resource-intensive operation

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
