---
cmd_name: kubectl config
cmd_category: "容器编排/Kubernetes命令"
cmd_dimension: Container Orchestration
cmd_install: Download from https://kubernetes.io/docs/tasks/tools/
cmd_platforms:
- linux
- darwin
- windows
summary: "Modify kubeconfig files"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/kubernetes.yaml
---


# kubectl config

> Modify kubeconfig files

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl config [subcommand]
```

## 参数

| Flag | Description |
|------|-------------|
| `view` | Display merged kubeconfig settings |
| `get-contexts` | Display available contexts |
| `use-context` | Set the current context |
| `set-context` | Set a context entry |

## 示例

### 示例 1: View current configuration

```bash
kubectl config view
```

### 示例 2: List available contexts

```bash
kubectl config get-contexts
```

### 示例 3: Switch to production context

```bash
kubectl config use-context production
```

### 示例 4: Display current context

```bash
kubectl config current-context
```

## 风险提示

> ⚠️ **HIGH**: Switching contexts can direct commands to different clusters (production/staging)

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
