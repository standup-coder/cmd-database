---
{
  "cmd_name": "helm history",
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

# helm history

> View release history

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm history [release-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Release namespace |
| `-o` | Output format: table, json, yaml |
| `--max` | Maximum number of revisions to fetch |

## 示例

### 示例 1: View nginx release history

```bash
helm history nginx
```

### 示例 2: View history in production namespace

```bash
helm history nginx -n production
```

### 示例 3: Show last 10 revisions

```bash
helm history nginx --max 10
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows revision history

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
