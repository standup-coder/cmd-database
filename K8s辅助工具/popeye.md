---
{
  "cmd_name": "popeye",
  "cmd_category": "Kubernetes Utilities",
  "cmd_dimension": "Kubernetes Utilities",
  "cmd_install": "Download from https://github.com/derailed/popeye",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-utilities.yaml"
}
---

# popeye

> Kubernetes cluster resource sanitizer and health checker

## 安装

```bash
Download from https://github.com/derailed/popeye
```

## 用法

```
popeye [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Check specific namespace |
| `-o` | Output format: standard, json, yaml, html |
| `-s` | Specify spinach config file |

## 示例

### 示例 1: Scan entire cluster for issues

```bash
popeye
```

### 示例 2: Scan production namespace

```bash
popeye -n production
```

### 示例 3: Output results in JSON format

```bash
popeye -o json
```

### 示例 4: Run with custom configuration

```bash
popeye -s spinach.yaml
```

## 风险提示

> ⚠️ **LOW**: Read-only health check; no cluster modifications

## 所属维度

[[K8s辅助工具-MOC|Kubernetes Utilities]]
