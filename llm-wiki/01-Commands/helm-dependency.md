---
{
  "cmd_name": "helm dependency",
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

# helm dependency

> Manage chart dependencies

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm dependency [subcommand] [flags]
```

## 示例

### 示例 1: List chart dependencies

```bash
helm dependency list mychart
```

### 示例 2: Update chart dependencies

```bash
helm dependency update mychart
```

### 示例 3: Rebuild dependency lock file

```bash
helm dependency build mychart
```

## 风险提示

> ⚠️ **LOW**: Manages local dependencies only

## 所属维度

[[Kubernetes Helm Package Management-MOC|Kubernetes Helm Package Management]]
