---
cmd_name: kubectl config current-context
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "显示当前配置上下文"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl config current-context

> 显示当前配置上下文

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl config current-context
```

## 示例

### 示例 1: 显示当前使用的集群上下文

```bash
kubectl config current-context
```

### 示例 2: 列出所有可用上下文

```bash
kubectl config get-contexts
```

### 示例 3: 切换到生产环境上下文

```bash
kubectl config use-context production
```

## 风险提示

> ⚠️ **MEDIUM**: 上下文切换影响命令目标集群

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
