---
cmd_name: gcloud container clusters create
cmd_category: "容器编排/K8s云平台工具"
cmd_dimension: Kubernetes Cloud Platforms
cmd_install: Part of Google Cloud SDK; install from https://cloud.google.com/sdk/install
cmd_platforms:
- linux
- darwin
- windows
summary: "Create Google GKE Kubernetes cluster"
cmd_level: advanced
cmd_related: []
cmd_tags:
- kubernetes
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/k8s-cloud.yaml
---


# gcloud container clusters create

> Create Google GKE Kubernetes cluster

## 安装

```bash
Part of Google Cloud SDK; install from https://cloud.google.com/sdk/install
```

## 用法

```
gcloud container clusters create [cluster-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--zone` | Compute zone |
| `--num-nodes` | Number of nodes |
| `--machine-type` | Machine type for nodes |

## 示例

### 示例 1: Create GKE cluster in us-central1-a

```bash
gcloud container clusters create my-cluster --zone us-central1-a
```

### 示例 2: Create cluster with 5 n1-standard-4 nodes

```bash
gcloud container clusters create prod-cluster --num-nodes 5 --machine-type n1-standard-4
```

### 示例 3: Create cluster with auto-scaling

```bash
gcloud container clusters create dev-cluster --zone us-west1-b --enable-autoscaling --min-nodes 1 --max-nodes 10
```

## 风险提示

> ⚠️ **CRITICAL**: Creates billable GCP resources; incurs costs

## 所属维度

[[K8s云平台工具-MOC|Kubernetes Cloud Platforms]]
