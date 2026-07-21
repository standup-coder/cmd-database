---
{
  "cmd_name": "systemctl status kubelet",
  "cmd_category": "Kubernetes Cluster Management",
  "cmd_dimension": "Kubernetes Cluster Management",
  "cmd_install": "Installed with kubeadm",
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

# systemctl status kubelet

> Check kubelet service status

## 安装

```bash
Installed with kubeadm
```

## 用法

```
systemctl status kubelet
```

## 示例

### 示例 1: View kubelet service status

```bash
systemctl status kubelet
```

### 示例 2: Start kubelet service

```bash
systemctl start kubelet
```

### 示例 3: Enable kubelet to start on boot

```bash
systemctl enable kubelet
```

### 示例 4: Restart kubelet service

```bash
systemctl restart kubelet
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
