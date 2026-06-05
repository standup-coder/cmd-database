---
cmd_name: kubectl get limitranges
cmd_category: "容器编排/K8s安全工具"
cmd_dimension: Kubernetes Security
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "List LimitRange resources for resource constraints"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-security.yaml
---


# kubectl get limitranges

> List LimitRange resources for resource constraints

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get limitranges [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |

## 示例

### 示例 1: List resource limits in production namespace

```bash
kubectl get limits -n production
```

### 示例 2: Describe memory limit configuration

```bash
kubectl describe limitrange mem-limit-range -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows resource constraints

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
