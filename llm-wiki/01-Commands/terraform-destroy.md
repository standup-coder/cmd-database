---
{
  "cmd_name": "terraform destroy",
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

# terraform destroy

> Destroy Terraform-managed infrastructure

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform destroy [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-auto-approve` | Skip approval prompt |
| `-target` | Destroy specific resource |

## 示例

### 示例 1: Destroy all resources with confirmation

```bash
terraform destroy
```

### 示例 2: Destroy without confirmation

```bash
terraform destroy -auto-approve
```

### 示例 3: Destroy specific resource only

```bash
terraform destroy -target=kubernetes_namespace.example
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes all managed infrastructure

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
