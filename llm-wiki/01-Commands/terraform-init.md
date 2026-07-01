---
{
  "cmd_name": "terraform init",
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

# terraform init

> Initialize Terraform working directory

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform init [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-upgrade` | Upgrade provider plugins |
| `-backend-config` | Backend configuration |

## 示例

### 示例 1: Initialize Terraform directory

```bash
terraform init
```

### 示例 2: Initialize and upgrade providers

```bash
terraform init -upgrade
```

### 示例 3: Initialize with backend configuration

```bash
terraform init -backend-config=backend.hcl
```

## 风险提示

> ⚠️ **LOW**: Local initialization only; no infrastructure changes

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
