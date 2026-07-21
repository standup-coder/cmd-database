---
{
  "cmd_name": "kube-hunter",
  "cmd_category": "容器编排/K8s安全扩展",
  "cmd_dimension": "K8s安全扩展",
  "cmd_install": "pip install kube-hunter 或参考 https://github.com/aquasecurity/kube-hunter",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubescape",
    "trivy"
  ],
  "cmd_tags": [
    "safety",
    "kubernetes",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security-extra.yaml"
}
---

# kube-hunter

> Kubernetes 集群渗透测试工具

## 安装

```bash
pip install kube-hunter 或参考 https://github.com/aquasecurity/kube-hunter
```

## 用法

```
kube-hunter [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--remote` | 指定远程节点地址 |
| `--pod` | 以 Pod 内方式运行 |

## 示例

### 示例 1: 远程扫描 K8s 节点

```bash
kube-hunter --remote 192.168.1.10
```

### 示例 2: 在集群内部以 Pod 方式运行

```bash
kube-hunter --pod
```

## 关联命令

- [[kubescape]]

## 风险提示

> ⚠️ **HIGH**: 渗透测试会产生攻击行为，请仅在授权和隔离环境中执行

## 所属维度

[[K8s安全扩展-MOC|容器编排/K8s安全扩展]]
