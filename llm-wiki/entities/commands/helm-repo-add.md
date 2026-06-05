---
cmd_name: helm repo add
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Add Helm chart repository"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm repo add

> Add Helm chart repository

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm repo add [repo-name] [repo-url] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--username` | Username for repository authentication |
| `--password` | Password for repository authentication |
| `--ca-file` | CA bundle file for repository verification |
| `--cert-file` | Client certificate file |
| `--key-file` | Client key file |

## 示例

### 示例 1: Add official stable chart repository

```bash
helm repo add stable https://charts.helm.sh/stable
```

### 示例 2: Add Bitnami chart repository

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```

### 示例 3: Add private repository with authentication

```bash
helm repo add private-repo https://charts.example.com --username user --password pass
```

### 示例 4: Add repository with custom CA certificate

```bash
helm repo add secure-repo https://secure.example.com --ca-file ca.crt
```

## 风险提示

> ⚠️ **LOW**: Adds repository reference only; verify repository trustworthiness

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
