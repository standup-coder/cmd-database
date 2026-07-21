---
{
  "cmd_name": "argocd app delete",
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
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cicd.yaml"
}
---

# argocd app delete

> Delete ArgoCD application

## 安装

```bash
Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 用法

```
argocd app delete [app-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--cascade` | Delete application resources from cluster |
| `-y` | Skip confirmation prompt |

## 示例

### 示例 1: Delete application with confirmation

```bash
argocd app delete myapp
```

### 示例 2: Delete without confirmation

```bash
argocd app delete myapp -y
```

### 示例 3: Delete application and all its resources

```bash
argocd app delete myapp --cascade
```

## 风险提示

> ⚠️ **CRITICAL**: Cascade deletion removes all application resources from cluster

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
