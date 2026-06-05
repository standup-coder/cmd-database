---
cmd_name: kubectl get componentstatuses
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "检查 Kubernetes 控制平面组件健康状态"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- kubernetes
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl get componentstatuses

> 检查 Kubernetes 控制平面组件健康状态

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl get componentstatuses
```

## 示例

### 示例 1: 检查控制平面组件状态

```bash
kubectl get cs
```

### 示例 2: 详细显示组件状态信息

```bash
kubectl get componentstatuses -o wide
```

## 风险提示

> ⚠️ **LOW**: 只读健康检查；无修改风险

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
