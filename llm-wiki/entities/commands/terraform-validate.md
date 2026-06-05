---
cmd_name: terraform validate
cmd_category: "容器编排/K8s配置管理"
cmd_dimension: Kubernetes Config Management
cmd_install: Download from https://www.terraform.io/downloads
cmd_platforms:
- linux
- darwin
- windows
summary: "Validate Terraform configuration syntax"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-config.yaml
---


# terraform validate

> Validate Terraform configuration syntax

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform validate [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-json` | Output validation result in JSON |

## 示例

### 示例 1: Validate current directory configuration

```bash
terraform validate
```

### 示例 2: Validate and output JSON result

```bash
terraform validate -json
```

### 示例 3: Validate without color output

```bash
terraform validate -no-color
```

## 风险提示

> ⚠️ **LOW**: Read-only validation; no infrastructure changes

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]
