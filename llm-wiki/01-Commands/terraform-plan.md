---
{
  "cmd_name": "terraform plan",
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

# terraform plan

> Generate and show Terraform execution plan

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform plan [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-out` | Save plan to file |
| `-var-file` | Variable file path |
| `-target` | Target specific resource |

## 示例

### 示例 1: Show execution plan

```bash
terraform plan
```

### 示例 2: Save plan to file

```bash
terraform plan -out=tfplan
```

### 示例 3: Plan with variable file

```bash
terraform plan -var-file=production.tfvars
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; previews changes only

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
