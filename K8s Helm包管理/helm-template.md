---
{
  "cmd_name": "helm template",
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

# helm template

> Render chart templates locally

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm template [release-name] [chart] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--values` | Values file path |
| `--set` | Set values on command line |
| `--output-dir` | Write rendered templates to directory |
| `--show-only` | Show only specific templates |

## 示例

### 示例 1: Render nginx chart templates

```bash
helm template nginx bitnami/nginx
```

### 示例 2: Render with custom values

```bash
helm template nginx bitnami/nginx --values values.yaml
```

### 示例 3: Write rendered templates to directory

```bash
helm template nginx bitnami/nginx --output-dir rendered
```

### 示例 4: Show only deployment template

```bash
helm template nginx bitnami/nginx --show-only templates/deployment.yaml
```

## 风险提示

> ⚠️ **LOW**: Local rendering only; no cluster changes

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
