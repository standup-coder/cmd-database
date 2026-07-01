---
{
  "cmd_name": "terraform apply",
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
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# terraform apply

> Apply Terraform configuration changes

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform apply [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-auto-approve` | Skip approval prompt |
| `-var-file` | Variable file path |
| `-target` | Target specific resource |

## 示例

### 示例 1: Apply changes with confirmation

```bash
terraform apply
```

### 示例 2: Apply without confirmation prompt

```bash
terraform apply -auto-approve
```

### 示例 3: Apply with variable file

```bash
terraform apply -var-file=production.tfvars
```

### 示例 4: Apply saved plan file

```bash
terraform apply tfplan
```

## 风险提示

> ⚠️ **CRITICAL**: Creates, modifies, or deletes infrastructure resources

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
