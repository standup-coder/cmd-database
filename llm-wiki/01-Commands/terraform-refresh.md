---
{
  "cmd_name": "terraform refresh",
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

# terraform refresh

> Update Terraform state with real infrastructure

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform refresh [flags]
```

## 示例

### 示例 1: Refresh state from infrastructure

```bash
terraform refresh
```

### 示例 2: Refresh with variables

```bash
terraform refresh -var-file=production.tfvars
```

### 示例 3: Refresh specific resource

```bash
terraform refresh -target=kubernetes_deployment.app
```

## 风险提示

> ⚠️ **MEDIUM**: Updates state file with current infrastructure

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
