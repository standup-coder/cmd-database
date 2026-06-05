---
cmd_name: kubectl get resourcequota
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "检查资源配额限制"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl get resourcequota

> 检查资源配额限制

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl get resourcequota [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 指定命名空间 |
| `-A` | 所有命名空间 |

## 示例

### 示例 1: 查看生产环境资源配额

```bash
kubectl get quota -n production
```

### 示例 2: 详细查看配额使用情况

```bash
kubectl describe resourcequota default -n production
```

## 风险提示

> ⚠️ **LOW**: 只读配额信息；帮助识别资源限制问题

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
