---
{
  "cmd_name": "kubectl port-forward",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/kubernetes.yaml"
}
---

# kubectl port-forward

> Forward one or more local ports to a pod

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl port-forward [pod-name] [local-port]:[pod-port]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Namespace |
| `--address` | Address to listen on (default: localhost) |

## 示例

### 示例 1: Forward local port 8080 to pod port 80

```bash
kubectl port-forward mypod 8080:80
```

### 示例 2: Forward to a service

```bash
kubectl port-forward service/myservice 8080:80
```

### 示例 3: Allow external connections

```bash
kubectl port-forward mypod 8080:80 --address=0.0.0.0
```

## 风险提示

> ⚠️ **MEDIUM**: Exposes pod ports to local machine; ensure proper security

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
