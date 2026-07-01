---
{
  "cmd_name": "terraform workspace list",
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

# terraform workspace list

> List Terraform workspaces

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform workspace list
```

## 示例

### 示例 1: List all workspaces

```bash
terraform workspace list
```

### 示例 2: Filter production workspaces

```bash
terraform workspace list | grep production
```

### 示例 3: Show current workspace

```bash
terraform workspace show
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists workspaces

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
