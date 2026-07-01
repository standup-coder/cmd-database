---
{
  "cmd_name": "terraform import",
  "cmd_category": "Kubernetes Config Management",
  "cmd_dimension": "Kubernetes Config Management",
  "cmd_install": "Download from https://www.terraform.io/downloads",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# terraform import

> Import existing infrastructure into Terraform state

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform import [address] [id]
```

## 示例

### 示例 1: Import namespace into state

```bash
terraform import kubernetes_namespace.example default
```

### 示例 2: Import EKS cluster

```bash
terraform import aws_eks_cluster.main my-cluster
```

### 示例 3: Import with variables

```bash
terraform import -var-file=production.tfvars kubernetes_deployment.app app-deployment
```

## 风险提示

> ⚠️ **MEDIUM**: Adds existing resource to state

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
