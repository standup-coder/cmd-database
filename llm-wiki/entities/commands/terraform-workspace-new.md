---
cmd_name: terraform workspace new
cmd_category: "容器编排/K8s配置管理"
cmd_dimension: Kubernetes Config Management
cmd_install: Download from https://www.terraform.io/downloads
cmd_platforms:
- linux
- darwin
- windows
summary: "Create new Terraform workspace"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-config.yaml
---


# terraform workspace new

> Create new Terraform workspace

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform workspace new [name]
```

## 示例

### 示例 1: Create production workspace

```bash
terraform workspace new production
```

### 示例 2: Create staging workspace

```bash
terraform workspace new staging
```

### 示例 3: Create workspace with state path

```bash
terraform workspace new -state=path/to/state dev
```

## 风险提示

> ⚠️ **MEDIUM**: Creates new isolated state

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]
