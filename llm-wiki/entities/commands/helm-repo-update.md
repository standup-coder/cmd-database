---
cmd_name: helm repo update
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Update local Helm chart repository cache"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm repo update

> Update local Helm chart repository cache

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm repo update [repo-name]
```

## 示例

### 示例 1: Update all repository indexes

```bash
helm repo update
```

### 示例 2: Update specific repository

```bash
helm repo update bitnami
```

### 示例 3: List configured repositories

```bash
helm repo list
```

## 风险提示

> ⚠️ **LOW**: Updates local cache only; no cluster impact

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
