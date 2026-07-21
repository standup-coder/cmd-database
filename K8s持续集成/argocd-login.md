---
{
  "cmd_name": "argocd login",
  "cmd_category": "Kubernetes CI/CD",
  "cmd_dimension": "CD",
  "cmd_install": "Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/",
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
  "source_file": "data/container/k8s/k8s-cicd.yaml"
}
---

# argocd login

> Login to ArgoCD server

## 安装

```bash
Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 用法

```
argocd login [server-address] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--username` | Username for authentication |
| `--password` | Password for authentication |
| `--insecure` | Skip server certificate verification |

## 示例

### 示例 1: Login to ArgoCD server

```bash
argocd login argocd.example.com
```

### 示例 2: Login with credentials

```bash
argocd login argocd.example.com --username admin --password admin123
```

### 示例 3: Login to local server without TLS verification

```bash
argocd login localhost:8080 --insecure
```

## 风险提示

> ⚠️ **LOW**: Authentication only; no cluster modifications

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
