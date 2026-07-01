---
{
  "cmd_name": "terraform fmt",
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

# terraform fmt

> Format Terraform configuration files

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform fmt [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-recursive` | Format files in subdirectories |
| `-check` | Check if files are formatted |
| `-diff` | Display formatting changes |

## 示例

### 示例 1: Format files in current directory

```bash
terraform fmt
```

### 示例 2: Format all files recursively

```bash
terraform fmt -recursive
```

### 示例 3: Check if formatting needed

```bash
terraform fmt -check
```

## 风险提示

> ⚠️ **LOW**: Only formats code; no functional changes

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
