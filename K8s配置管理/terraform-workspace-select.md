---
{
  "cmd_name": "terraform workspace select",
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

# terraform workspace select

> Switch to different Terraform workspace

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform workspace select [name]
```

## 示例

### 示例 1: Switch to production workspace

```bash
terraform workspace select production
```

### 示例 2: Switch to default workspace

```bash
terraform workspace select default
```

### 示例 3: Switch to staging workspace

```bash
terraform workspace select staging
```

## 风险提示

> ⚠️ **MEDIUM**: Changes active workspace; affects state

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]
