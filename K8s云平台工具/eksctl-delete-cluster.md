---
{
  "cmd_name": "eksctl delete cluster",
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
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cloud.yaml"
}
---

# eksctl delete cluster

> Delete AWS EKS cluster

## 安装

```bash
Download from https://eksctl.io/introduction/#installation
```

## 用法

```
eksctl delete cluster [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | Cluster name |
| `--region` | AWS region |
| `--wait` | Wait for deletion to complete |

## 示例

### 示例 1: Delete EKS cluster

```bash
eksctl delete cluster --name my-cluster
```

### 示例 2: Delete cluster in specific region

```bash
eksctl delete cluster --name my-cluster --region us-west-2
```

### 示例 3: Delete and wait for completion

```bash
eksctl delete cluster --name my-cluster --wait
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes cluster and all resources

## 所属维度

[[K8s云平台工具-MOC|Kubernetes Cloud Platforms]]
