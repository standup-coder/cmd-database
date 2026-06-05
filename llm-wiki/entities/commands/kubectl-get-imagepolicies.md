---
cmd_name: kubectl get imagepolicies
cmd_category: "容器编排/K8s安全工具"
cmd_dimension: Kubernetes Security
cmd_install: kubectl with OPA/Gatekeeper or similar tools
cmd_platforms:
- linux
- darwin
- windows
summary: "List ImagePolicy resources for image validation"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-security.yaml
---


# kubectl get imagepolicies

> List ImagePolicy resources for image validation

## 安装

```bash
kubectl with OPA/Gatekeeper or similar tools
```

## 用法

```
kubectl get imagepolicies [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |

## 示例

### 示例 1: List image policies in production namespace

```bash
kubectl get imagepolicies -n production
```

### 示例 2: Describe trusted image policy

```bash
kubectl describe imagepolicy allow-trusted-images -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows image validation rules

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
