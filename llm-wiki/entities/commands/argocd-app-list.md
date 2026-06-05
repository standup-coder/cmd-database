---
cmd_name: argocd app list
cmd_category: "容器编排/K8s持续集成"
cmd_dimension: CD
cmd_install: Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/
cmd_platforms:
- linux
- darwin
- windows
summary: "List ArgoCD applications"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-cicd.yaml
---


# argocd app list

> List ArgoCD applications

## 安装

```bash
Download from https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 用法

```
argocd app list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | Output format: wide, json, yaml |

## 示例

### 示例 1: List all applications

```bash
argocd app list
```

### 示例 2: List with detailed information

```bash
argocd app list -o wide
```

### 示例 3: List in JSON format

```bash
argocd app list -o json
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists applications only

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
