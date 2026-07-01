---
{
  "cmd_name": "eksctl get cluster",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cloud.yaml"
}
---

# eksctl get cluster

> List AWS EKS clusters

## 安装

```bash
Download from https://eksctl.io/introduction/#installation
```

## 用法

```
eksctl get cluster [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--region` | AWS region |
| `-o` | Output format: table, json, yaml |

## 示例

### 示例 1: List all EKS clusters

```bash
eksctl get cluster
```

### 示例 2: List clusters in specific region

```bash
eksctl get cluster --region us-west-2
```

### 示例 3: List clusters in JSON format

```bash
eksctl get cluster -o json
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists clusters only

## 所属维度

[[Kubernetes Cloud Platforms-MOC|Kubernetes Cloud Platforms]]
