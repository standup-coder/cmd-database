---
cmd_name: calicoctl apply
cmd_category: "容器编排/K8s网络插件"
cmd_dimension: Kubernetes Networking
cmd_install: Download from https://github.com/projectcalico/calico/releases
cmd_platforms:
- linux
- darwin
- windows
summary: "Apply Calico network policy configuration"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/k8s-network.yaml
---


# calicoctl apply

> Apply Calico network policy configuration

## 安装

```bash
Download from https://github.com/projectcalico/calico/releases
```

## 用法

```
calicoctl apply -f [policy-file]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Policy configuration file path |

## 示例

### 示例 1: Apply network policy from file

```bash
calicoctl apply -f network-policy.yaml
```

### 示例 2: Apply all policies in directory

```bash
calicoctl apply -f policies/
```

## 风险提示

> ⚠️ **HIGH**: Modifies network policies; can affect pod connectivity

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
