---
cmd_name: k9s
cmd_category: "容器编排/K8s辅助工具"
cmd_dimension: Kubernetes Utilities
cmd_install: Download from https://k9scli.io/topics/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Interactive terminal UI for Kubernetes"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- kubernetes
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-utilities.yaml
---


# k9s

> Interactive terminal UI for Kubernetes

## 安装

```bash
Download from https://k9scli.io/topics/install/
```

## 用法

```
k9s [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Start in specific namespace |
| `-c` | Start with specific view (pods, services, etc.) |
| `--readonly` | Launch in read-only mode |

## 示例

### 示例 1: Launch k9s terminal UI

```bash
k9s
```

### 示例 2: Launch in production namespace

```bash
k9s -n production
```

### 示例 3: Launch directly to pods view

```bash
k9s -c pods
```

### 示例 4: Launch in read-only mode

```bash
k9s --readonly
```

## 风险提示

> ⚠️ **LOW**: Interactive UI; risk depends on user actions

## 所属维度

[[K8s辅助工具-MOC|Kubernetes Utilities]]
