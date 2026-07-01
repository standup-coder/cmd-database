---
{
  "cmd_name": "kubeadm reset",
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
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# kubeadm reset

> Reset node state and undo kubeadm init or join

## 安装

```bash
apt-get install kubeadm (Ubuntu) or yum install kubeadm (CentOS)
```

## 用法

```
kubeadm reset [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Force reset without prompting for confirmation |
| `--cleanup-tmp-dir` | Cleanup the /etc/kubernetes/tmp directory |

## 示例

### 示例 1: Reset node with confirmation prompt

```bash
kubeadm reset
```

### 示例 2: Force reset without confirmation

```bash
kubeadm reset -f
```

## 风险提示

> ⚠️ **CRITICAL**: Removes all Kubernetes components and data from node

## 所属维度

[[Kubernetes Cluster Management-MOC|Kubernetes Cluster Management]]
