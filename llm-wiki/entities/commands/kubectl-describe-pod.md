---
cmd_name: kubectl describe pod
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "详细查看 Pod 状态和事件信息"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl describe pod

> 详细查看 Pod 状态和事件信息

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl describe pod [pod-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 指定命名空间 |
| `--show-events` | 显示相关事件 |

## 示例

### 示例 1: 查看指定 Pod 的详细信息

```bash
kubectl describe pod myapp-pod
```

### 示例 2: 查看生产环境中的 Pod 详情

```bash
kubectl describe pod myapp-pod -n production
```

### 示例 3: 查看 Pod 信息但不显示事件

```bash
kubectl describe pod myapp-pod --show-events=false
```

## 风险提示

> ⚠️ **LOW**: 只读操作；显示详细诊断信息

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
