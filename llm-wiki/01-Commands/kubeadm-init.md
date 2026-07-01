---
{
  "cmd_name": "kubeadm init",
  "cmd_category": "Kubernetes Cluster Management",
  "cmd_dimension": "Kubernetes Cluster Management",
  "cmd_install": "apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# kubeadm init

> Initialize Kubernetes control plane node

## 安装

```bash
apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)
```

## 用法

```
kubeadm init [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--pod-network-cidr` | Specify range of IP addresses for the pod network |
| `--apiserver-advertise-address` | The IP address the API Server will advertise |
| `--control-plane-endpoint` | Specify a stable IP address or DNS name for the control plane |
| `--kubernetes-version` | Choose a specific Kubernetes version for the control plane |

## 示例

### 示例 1: Initialize control plane with pod network CIDR

```bash
kubeadm init --pod-network-cidr=10.244.0.0/16
```

### 示例 2: Initialize with specific API server address

```bash
kubeadm init --apiserver-advertise-address=192.168.1.100
```

### 示例 3: Initialize with high availability endpoint

```bash
kubeadm init --control-plane-endpoint=cluster-endpoint:6443
```

## 风险提示

> ⚠️ **CRITICAL**: Initializes new cluster; existing cluster data may be affected

## 所属维度

[[Kubernetes Cluster Management-MOC|Kubernetes Cluster Management]]
