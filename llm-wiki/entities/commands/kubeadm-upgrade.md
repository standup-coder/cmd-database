---
cmd_name: kubeadm upgrade
cmd_category: "容器编排/K8s集群管理"
cmd_dimension: Kubernetes Cluster Management
cmd_install: apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)
cmd_platforms:
- linux
summary: "Upgrade Kubernetes cluster to specified version"
cmd_level: advanced
cmd_related: []
cmd_tags:
- kubernetes
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/k8s-cluster.yaml
---


# kubeadm upgrade

> Upgrade Kubernetes cluster to specified version

## 安装

```bash
apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)
```

## 用法

```
kubeadm upgrade [subcommand]
```

## 参数

| Flag | Description |
|------|-------------|
| `plan` | Check which versions are available to upgrade to |
| `apply` | Upgrade cluster to specified version |
| `node` | Upgrade commands for worker nodes |

## 示例

### 示例 1: Check available upgrade versions

```bash
kubeadm upgrade plan
```

### 示例 2: Upgrade control plane to v1.28.0

```bash
kubeadm upgrade apply v1.28.0
```

### 示例 3: Upgrade worker node components

```bash
kubeadm upgrade node
```

## 风险提示

> ⚠️ **CRITICAL**: Cluster upgrade may cause downtime; backup before upgrading

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
