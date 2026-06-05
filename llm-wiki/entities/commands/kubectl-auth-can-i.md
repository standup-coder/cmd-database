---
cmd_name: kubectl auth can-i
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "检查用户权限"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl auth can-i

> 检查用户权限

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl auth can-i [verb] [resource]
```

## 示例

### 示例 1: 检查是否有获取 Pod 的权限

```bash
kubectl auth can-i get pods
```

### 示例 2: 检查是否具有管理员权限

```bash
kubectl auth can-i '*' '*'
```

### 示例 3: 检查在生产环境创建 Deployment 的权限

```bash
kubectl auth can-i create deployments --namespace production
```

## 风险提示

> ⚠️ **LOW**: 权限检查；帮助诊断 RBAC 问题

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
