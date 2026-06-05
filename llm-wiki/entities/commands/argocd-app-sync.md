---
cmd_name: argocd app sync
cmd_category: "容器编排/K8s持续集成"
cmd_dimension: CD
cmd_install: Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/
cmd_platforms:
- linux
- darwin
- windows
summary: "Sync application state with Git repository"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/k8s-cicd.yaml
---


# argocd app sync

> Sync application state with Git repository

## 安装

```bash
Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 用法

```
argocd app sync [app-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--prune` | Delete resources not in Git |
| `--dry-run` | Preview sync without applying |
| `--force` | Force sync even if no changes detected |

## 示例

### 示例 1: Sync application with Git repository

```bash
argocd app sync myapp
```

### 示例 2: Sync and delete orphaned resources

```bash
argocd app sync myapp --prune
```

### 示例 3: Preview sync changes

```bash
argocd app sync myapp --dry-run
```

## 风险提示

> ⚠️ **HIGH**: Applies changes to cluster; may affect running services

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
