---
{
  "cmd_name": "az aks delete",
  "cmd_category": "Kubernetes Cloud Platforms",
  "cmd_dimension": "Kubernetes Cloud Platforms",
  "cmd_install": "Part of Azure CLI; install from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli",
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
  "source_file": "data/container/k8s/k8s-cloud.yaml"
}
---

# az aks delete

> Delete Azure AKS cluster

## 安装

```bash
Part of Azure CLI; install from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
```

## 用法

```
az aks delete [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--resource-group` | Resource group name |
| `--name` | Cluster name |
| `--yes` | Skip confirmation prompt |

## 示例

### 示例 1: Delete AKS cluster with confirmation

```bash
az aks delete --resource-group myResourceGroup --name myAKSCluster
```

### 示例 2: Delete without confirmation

```bash
az aks delete --resource-group myRG --name myCluster --yes
```

## 风险提示

> ⚠️ **CRITICAL**: Permanently deletes cluster and all resources

## 所属维度

[[Kubernetes Cloud Platforms-MOC|Kubernetes Cloud Platforms]]
