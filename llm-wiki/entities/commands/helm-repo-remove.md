---
cmd_name: helm repo remove
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Remove Helm chart repository"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm repo remove

> Remove Helm chart repository

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm repo remove [repo-name]
```

## 示例

### 示例 1: Remove unused repository

```bash
helm repo remove deprecated-repo
```

### 示例 2: Verify repository removal

```bash
helm repo list
```

## 风险提示

> ⚠️ **LOW**: Removes repository reference only

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
