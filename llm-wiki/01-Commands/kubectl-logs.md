---
{
  "cmd_name": "kubectl logs",
  "cmd_category": "Container Orchestration",
  "cmd_dimension": "Container Orchestration",
  "cmd_install": "Download from https://kubernetes.io/docs/tasks/tools/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/kubernetes.yaml"
}
---

# kubectl logs

> Print the logs for a container in a pod

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl logs [pod-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Follow log output (stream logs) |
| `-c` | Container name (for multi-container pods) |
| `--tail` | Lines of recent log to display |
| `--previous` | Print logs from previous container instance |
| `-n` | Namespace |

## 示例

### 示例 1: Print logs from pod

```bash
kubectl logs mypod
```

### 示例 2: Stream logs from pod

```bash
kubectl logs mypod -f
```

### 示例 3: Print logs from specific container

```bash
kubectl logs mypod -c mycontainer
```

### 示例 4: Print last 100 lines of logs

```bash
kubectl logs mypod --tail=100
```

### 示例 5: Print logs from crashed container

```bash
kubectl logs mypod --previous
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Container Orchestration-MOC|Container Orchestration]]
