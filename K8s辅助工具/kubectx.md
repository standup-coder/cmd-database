---
{
  "cmd_name": "kubectx",
  "cmd_category": "Kubernetes Utilities",
  "cmd_dimension": "Kubernetes Utilities",
  "cmd_install": "Download from https://github.com/ahmetb/kubectx",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-utilities.yaml"
}
---

# kubectx

> Switch between Kubernetes contexts

## 安装

```bash
Download from https://github.com/ahmetb/kubectx
```

## 用法

```
kubectx [context-name]
```

## 示例

### 示例 1: List all contexts

```bash
kubectx
```

### 示例 2: Switch to production context

```bash
kubectx production
```

### 示例 3: Switch to previous context

```bash
kubectx -
```

### 示例 4: Switch to staging context

```bash
kubectx staging
```

## 风险提示

> ⚠️ **HIGH**: Switching contexts changes target cluster; verify before executing commands

## 所属维度

[[K8s辅助工具-MOC|Kubernetes Utilities]]
