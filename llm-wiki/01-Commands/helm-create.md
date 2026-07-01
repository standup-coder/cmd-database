---
{
  "cmd_name": "helm create",
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

# helm create

> Create new Helm chart

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm create [chart-name]
```

## 示例

### 示例 1: Create new chart named myapp

```bash
helm create myapp
```

### 示例 2: Create chart using default starter

```bash
helm create myapp --starter default
```

## 风险提示

> ⚠️ **LOW**: Creates local chart files only

## 所属维度

[[Kubernetes Helm Package Management-MOC|Kubernetes Helm Package Management]]
