---
{
  "cmd_name": "eksctl create cluster",
  "cmd_category": "Kubernetes Cloud Platforms",
  "cmd_dimension": "Kubernetes Cloud Platforms",
  "cmd_install": "Download from https://eksctl.io/introduction/#installation",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cloud.yaml"
}
---

# eksctl create cluster

> Create AWS EKS Kubernetes cluster

## 安装

```bash
Download from https://eksctl.io/introduction/#installation
```

## 用法

```
eksctl create cluster [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | Cluster name |
| `--region` | AWS region |
| `--nodes` | Number of nodes |
| `--node-type` | EC2 instance type for nodes |

## 示例

### 示例 1: Create EKS cluster in us-west-2

```bash
eksctl create cluster --name my-cluster --region us-west-2
```

### 示例 2: Create cluster with 3 t3.large nodes

```bash
eksctl create cluster --name production --nodes 3 --node-type t3.large
```

### 示例 3: Create cluster with auto-scaling

```bash
eksctl create cluster --name dev --region us-east-1 --nodes-min 1 --nodes-max 5
```

## 风险提示

> ⚠️ **CRITICAL**: Creates billable AWS resources; incurs costs

## 所属维度

[[Kubernetes Cloud Platforms-MOC|Kubernetes Cloud Platforms]]
