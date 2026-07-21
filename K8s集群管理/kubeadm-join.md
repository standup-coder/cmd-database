---
{
  "cmd_name": "kubeadm join",
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
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# kubeadm join

> Join worker node to Kubernetes cluster

## 安装

```bash
apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)
```

## 用法

```
kubeadm join [api-server-endpoint] --token [token] --discovery-token-ca-cert-hash [hash]
```

## 参数

| Flag | Description |
|------|-------------|
| `--token` | Use this token for mutual authentication |
| `--discovery-token-ca-cert-hash` | Validate the root CA public key with this hash |
| `--control-plane` | Create a new control plane instance on this node |

## 示例

### 示例 1: Join node to cluster with token

```bash
kubeadm join 192.168.1.100:6443 --token abcdef.0123456789abcdef --discovery-token-ca-cert-hash sha256:hash...
```

### 示例 2: Join as control plane node for HA

```bash
kubeadm join 192.168.1.100:6443 --token abcdef.0123456789abcdef --discovery-token-ca-cert-hash sha256:hash... --control-plane
```

## 风险提示

> ⚠️ **HIGH**: Adds node to production cluster; verify token and endpoint carefully

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
