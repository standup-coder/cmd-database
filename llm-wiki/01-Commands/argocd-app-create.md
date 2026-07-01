---
{
  "cmd_name": "argocd app create",
  "cmd_category": "Kubernetes CI/CD",
  "cmd_dimension": "CD",
  "cmd_install": "Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/",
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
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cicd.yaml"
}
---

# argocd app create

> Create ArgoCD application

## 安装

```bash
Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 用法

```
argocd app create [app-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--repo` | Git repository URL |
| `--path` | Path to manifests in repository |
| `--dest-server` | Destination Kubernetes server |
| `--dest-namespace` | Destination namespace |

## 示例

### 示例 1: Create application from Git repository

```bash
argocd app create myapp --repo https://github.com/example/repo --path manifests --dest-server https://kubernetes.default.svc --dest-namespace default
```

### 示例 2: Create application with Helm charts

```bash
argocd app create myapp --repo https://github.com/example/repo --path helm --dest-namespace production
```

## 风险提示

> ⚠️ **HIGH**: Creates application that will deploy resources to cluster

## 所属维度

[[CD-MOC|Kubernetes CI/CD]]
