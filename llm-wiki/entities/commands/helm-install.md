---
cmd_name: helm install
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Install Helm chart to Kubernetes cluster"
cmd_level: advanced
cmd_related: []
cmd_tags:
- kubernetes
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm install

> Install Helm chart to Kubernetes cluster

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm install [release-name] [chart] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Target namespace |
| `--create-namespace` | Create namespace if not exists |
| `--values` | Values file path |
| `--set` | Set values on command line |
| `--set-string` | Set string values on command line |
| `--set-file` | Set values from file |
| `--dry-run` | Simulate installation |
| `--debug` | Enable verbose output |
| `--timeout` | Timeout for installation |
| `--wait` | Wait for resources to be ready |

## 示例

### 示例 1: Install nginx chart with release name nginx

```bash
helm install nginx bitnami/nginx
```

### 示例 2: Install to production namespace

```bash
helm install nginx bitnami/nginx -n production --create-namespace
```

### 示例 3: Install with custom values file

```bash
helm install nginx bitnami/nginx --values values.yaml
```

### 示例 4: Install with inline values

```bash
helm install nginx bitnami/nginx --set replicaCount=3 --set service.port=8080
```

### 示例 5: Preview installation without applying

```bash
helm install nginx bitnami/nginx --dry-run --debug
```

### 示例 6: Install and wait for readiness

```bash
helm install nginx bitnami/nginx --wait --timeout 10m
```

## 风险提示

> ⚠️ **HIGH**: Deploys resources to cluster; may affect existing workloads

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
