---
cmd_name: kubectl cluster-info
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "显示集群基本信息"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl cluster-info

> 显示集群基本信息

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl cluster-info [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `dump` | 转储集群详细信息 |

## 示例

### 示例 1: 显示集群核心服务地址

```bash
kubectl cluster-info
```

### 示例 2: 转储完整集群信息用于诊断

```bash
kubectl cluster-info dump
```

### 示例 3: 将集群信息转储到指定目录

```bash
kubectl cluster-info dump --output-directory=/tmp/cluster-dump
```

## 风险提示

> ⚠️ **LOW**: 只读集群信息；dump 可能包含敏感数据

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
