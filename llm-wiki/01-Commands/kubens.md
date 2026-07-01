---
{
  "cmd_name": "kubens",
  "cmd_category": "Kubernetes Utilities",
  "cmd_dimension": "Kubernetes Utilities",
  "cmd_install": "Download from https://github.com/ahmetb/kubectx",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-utilities.yaml"
}
---

# kubens

> Switch between Kubernetes namespaces

## 安装

```bash
Download from https://github.com/ahmetb/kubectx
```

## 用法

```
kubens [namespace-name]
```

## 示例

### 示例 1: List all namespaces

```bash
kubens
```

### 示例 2: Switch to production namespace

```bash
kubens production
```

### 示例 3: Switch to previous namespace

```bash
kubens -
```

### 示例 4: Switch to default namespace

```bash
kubens default
```

## 风险提示

> ⚠️ **MEDIUM**: Changes default namespace for subsequent commands

## 所属维度

[[Kubernetes Utilities-MOC|Kubernetes Utilities]]
