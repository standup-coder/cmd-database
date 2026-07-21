---
{
  "cmd_name": "terraform state rm",
  "cmd_category": "Kubernetes Config Management",
  "cmd_dimension": "Kubernetes Config Management",
  "cmd_install": "Download from https://www.terraform.io/downloads",
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
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# terraform state rm

> Remove resource from Terraform state

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform state rm [address]
```

## 示例

### 示例 1: Remove namespace from state

```bash
terraform state rm kubernetes_namespace.test
```

### 示例 2: Remove module resource from state

```bash
terraform state rm 'module.eks.aws_eks_cluster.main'
```

### 示例 3: Preview removal without executing

```bash
terraform state rm -dry-run kubernetes_deployment.app
```

## 风险提示

> ⚠️ **HIGH**: Removes from state; resource remains in infrastructure

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]
