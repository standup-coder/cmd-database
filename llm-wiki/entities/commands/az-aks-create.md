---
cmd_name: az aks create
cmd_category: "容器编排/K8s云平台工具"
cmd_dimension: Kubernetes Cloud Platforms
cmd_install: Part of Azure CLI; install from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
cmd_platforms:
- linux
- darwin
- windows
summary: "Create Azure AKS Kubernetes cluster"
cmd_level: advanced
cmd_related: []
cmd_tags:
- kubernetes
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/k8s-cloud.yaml
---


# az aks create

> Create Azure AKS Kubernetes cluster

## 安装

```bash
Part of Azure CLI; install from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
```

## 用法

```
az aks create [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--resource-group` | Resource group name |
| `--name` | Cluster name |
| `--node-count` | Number of nodes |
| `--node-vm-size` | VM size for nodes |

## 示例

### 示例 1: Create AKS cluster with 3 nodes

```bash
az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 3
```

### 示例 2: Create cluster with specific VM size

```bash
az aks create --resource-group prod-rg --name prod-cluster --node-vm-size Standard_D4s_v3
```

### 示例 3: Create cluster with monitoring enabled

```bash
az aks create --resource-group dev-rg --name dev-cluster --enable-addons monitoring
```

## 风险提示

> ⚠️ **CRITICAL**: Creates billable Azure resources; incurs costs

## 所属维度

[[K8s云平台工具-MOC|Kubernetes Cloud Platforms]]
