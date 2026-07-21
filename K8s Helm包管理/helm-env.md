---
{
  "cmd_name": "helm env",
  "cmd_category": "Kubernetes Helm Package Management",
  "cmd_dimension": "Kubernetes Helm Package Management",
  "cmd_install": "Download from https://helm.sh/docs/intro/install/",
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
  "source_file": "data/container/k8s/k8s-helm-enhanced.yaml"
}
---

# helm env

> Display Helm environment information

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm env
```

## 示例

### 示例 1: Show Helm environment variables and paths

```bash
helm env
```

### 示例 2: Find repository cache location

```bash
helm env | grep HELM_REPOSITORY_CACHE
```

## 风险提示

> ⚠️ **LOW**: Read-only environment information

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
