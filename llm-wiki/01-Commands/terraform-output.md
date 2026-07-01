---
{
  "cmd_name": "terraform output",
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

# terraform output

> Display Terraform output values

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform output [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-json` | Output in JSON format |
| `-raw` | Output raw value without quotes |

## 示例

### 示例 1: Display all output values

```bash
terraform output
```

### 示例 2: Display specific output value

```bash
terraform output cluster_endpoint
```

### 示例 3: Display outputs in JSON format

```bash
terraform output -json
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; displays values only

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]
