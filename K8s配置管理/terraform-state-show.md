---
{
  "cmd_name": "terraform state show",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# terraform state show

> Show detailed resource state

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform state show [address]
```

## 示例

### 示例 1: Show deployment resource state

```bash
terraform state show kubernetes_deployment.app
```

### 示例 2: Show module resource state

```bash
terraform state show 'module.eks.aws_eks_cluster.main'
```

### 示例 3: Show service state without colors

```bash
terraform state show -no-color kubernetes_service.api
```

## 风险提示

> ⚠️ **LOW**: Read-only; displays resource details

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]
