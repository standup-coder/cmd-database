---
cmd_name: gcloud container clusters delete
cmd_category: "容器编排/K8s云平台工具"
cmd_dimension: Kubernetes Cloud Platforms
cmd_install: Part of Google Cloud SDK; install from https://cloud.google.com/sdk/install
cmd_platforms:
- linux
- darwin
- windows
summary: "Delete Google GKE cluster"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/k8s-cloud.yaml
---


# gcloud container clusters delete

> Delete Google GKE cluster

## 安装

```bash
Part of Google Cloud SDK; install from https://cloud.google.com/sdk/install
```

## 用法

```
gcloud container clusters delete [cluster-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--zone` | Cluster zone |
| `--quiet` | Skip confirmation prompt |

## 示例

### 示例 1: Delete GKE cluster with confirmation

```bash
gcloud container clusters delete my-cluster --zone us-central1-a
```

### 示例 2: Delete without confirmation

```bash
gcloud container clusters delete my-cluster --zone us-central1-a --quiet
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes cluster and all resources

## 所属维度

[[K8s云平台工具-MOC|Kubernetes Cloud Platforms]]
