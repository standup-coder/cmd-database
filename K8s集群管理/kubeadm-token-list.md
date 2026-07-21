---
{
  "cmd_name": "kubeadm token list",
  "cmd_category": "Kubernetes Cluster Management",
  "cmd_dimension": "Kubernetes Cluster Management",
  "cmd_install": "apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# kubeadm token list

> List bootstrap tokens on the cluster

## 安装

```bash
apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)
```

## 用法

```
kubeadm token list
```

## 示例

### 示例 1: List all cluster join tokens

```bash
kubeadm token list
```

### 示例 2: Generate new token and print join command

```bash
kubeadm token create --print-join-command
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists existing tokens

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
