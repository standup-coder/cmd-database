---
cmd_name: kubectl logs
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "查看容器日志用于问题诊断"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl logs

> 查看容器日志用于问题诊断

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl logs [pod-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 实时跟踪日志 |
| `-p` | 查看前一个容器实例日志 |
| `--since` | 显示最近时间段的日志 |
| `--tail` | 显示最后 N 行日志 |

## 示例

### 示例 1: 实时跟踪 Pod 日志

```bash
kubectl logs mypod -f
```

### 示例 2: 查看最近1小时的日志

```bash
kubectl logs mypod --since=1h
```

### 示例 3: 查看最后100行日志

```bash
kubectl logs mypod --tail=100
```

### 示例 4: 查看崩溃容器的前一个实例日志

```bash
kubectl logs mypod -p
```

## 风险提示

> ⚠️ **LOW**: 只读日志信息；敏感信息需注意

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
