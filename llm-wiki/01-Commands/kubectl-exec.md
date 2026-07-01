---
{
  "cmd_name": "kubectl exec",
  "cmd_category": "Container Orchestration",
  "cmd_dimension": "Container Orchestration",
  "cmd_install": "Download from https://kubernetes.io/docs/tasks/tools/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/kubernetes.yaml"
}
---

# kubectl exec

> Execute a command in a container

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl exec [pod-name] -- [command]
```

## 参数

| Flag | Description |
|------|-------------|
| `-it` | Interactive terminal |
| `-c` | Container name (for multi-container pods) |
| `-n` | Namespace |

## 示例

### 示例 1: Execute command in pod

```bash
kubectl exec mypod -- ls /
```

### 示例 2: Open interactive shell in pod

```bash
kubectl exec -it mypod -- /bin/bash
```

### 示例 3: Show environment variables in container

```bash
kubectl exec mypod -c mycontainer -- env
```

## 风险提示

> ⚠️ **HIGH**: Can execute arbitrary commands in production containers

## 所属维度

[[Container Orchestration-MOC|Container Orchestration]]
