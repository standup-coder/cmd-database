---
cmd_name: az aks list
cmd_category: "容器编排/K8s云平台工具"
cmd_dimension: Kubernetes Cloud Platforms
cmd_install: Part of Azure CLI; install from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
cmd_platforms:
- linux
- darwin
- windows
summary: "List Azure AKS clusters"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-cloud.yaml
---


# az aks list

> List Azure AKS clusters

## 安装

```bash
Part of Azure CLI; install from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
```

## 用法

```
az aks list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--resource-group` | Filter by resource group |
| `-o` | Output format: table, json, yaml |

## 示例

### 示例 1: List all AKS clusters

```bash
az aks list
```

### 示例 2: List clusters in specific resource group

```bash
az aks list --resource-group myResourceGroup
```

### 示例 3: List clusters in table format

```bash
az aks list -o table
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists clusters only

## 所属维度

[[K8s云平台工具-MOC|Kubernetes Cloud Platforms]]
