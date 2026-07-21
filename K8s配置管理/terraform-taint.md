---
{
  "cmd_name": "terraform taint",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# terraform taint

> Mark resource for recreation on next apply

## 安装

```bash
Download from https://www.terraform.io/downloads
```

## 用法

```
terraform taint [address]
```

## 示例

### 示例 1: Taint deployment for recreation

```bash
terraform taint kubernetes_deployment.app
```

### 示例 2: Taint node group

```bash
terraform taint module.eks.aws_eks_node_group.main
```

### 示例 3: Taint even if resource missing

```bash
terraform taint -allow-missing kubernetes_service.api
```

## 风险提示

> ⚠️ **MEDIUM**: Forces resource recreation on next apply

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]
