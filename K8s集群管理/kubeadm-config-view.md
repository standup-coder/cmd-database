---
{
  "cmd_name": "kubeadm config view",
  "cmd_category": "Kubernetes Cluster Management",
  "cmd_dimension": "Kubernetes Cluster Management",
  "cmd_install": "apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# kubeadm config view

> View the kubeadm configuration

## 安装

```bash
apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)
```

## 用法

```
kubeadm config view
```

## 示例

### 示例 1: Display current cluster configuration

```bash
kubeadm config view
```

### 示例 2: Print default init configuration

```bash
kubeadm config print init-defaults
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; displays configuration only

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
