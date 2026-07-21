---
{
  "cmd_name": "terraform state list",
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

# terraform state list

> List resources in Terraform state

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform state list [options]
```

## 示例

### 示例 1: List all resources in state

```bash
terraform state list
```

### 示例 2: List resources matching pattern

```bash
terraform state list 'kubernetes_namespace.*'
```

### 示例 3: List resource by ID

```bash
terraform state list -id=eks-cluster
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists state resources

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]
