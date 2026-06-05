---
cmd_name: crictl stats
cmd_category: "容器编排/K8s容器运行时"
cmd_dimension: Kubernetes Container Runtime
cmd_install: Download from https://github.com/kubernetes-sigs/cri-tools/releases
cmd_platforms:
- linux
summary: "Display container resource usage statistics"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-runtime.yaml
---


# crictl stats

> Display container resource usage statistics

## 安装

```bash
Download from https://github.com/kubernetes-sigs/cri-tools/releases
```

## 用法

```
crictl stats [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | Show all containers (default shows just running) |
| `--no-stream` | Disable streaming stats and only pull the first result |

## 示例

### 示例 1: Show real-time resource usage for running containers

```bash
crictl stats
```

### 示例 2: Show stats for all containers

```bash
crictl stats -a
```

### 示例 3: Show current stats snapshot

```bash
crictl stats --no-stream
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; displays resource metrics only

## 所属维度

[[K8s容器运行时-MOC|Kubernetes Container Runtime]]
