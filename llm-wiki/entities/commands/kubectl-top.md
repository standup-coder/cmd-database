---
cmd_name: kubectl top
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "查看资源使用情况，识别性能瓶颈"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl top

> 查看资源使用情况，识别性能瓶颈

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl top [nodes|pods] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 指定命名空间 |
| `-A` | 所有命名空间 |
| `--containers` | 显示容器级别资源 |

## 示例

### 示例 1: 查看节点资源使用情况

```bash
kubectl top nodes
```

### 示例 2: 查看生产环境 Pod 资源使用

```bash
kubectl top pods -n production
```

### 示例 3: 查看容器级别资源使用

```bash
kubectl top pods --containers
```

## 风险提示

> ⚠️ **LOW**: 只读资源监控；需要 metrics-server

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
