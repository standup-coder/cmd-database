---
{
  "cmd_name": "kubectl top",
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

# kubectl top

> Display resource (CPU/memory) usage

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl top [nodes|pods]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Namespace |
| `-A` | All namespaces |
| `--containers` | Show container metrics |

## 示例

### 示例 1: Show node resource usage

```bash
kubectl top nodes
```

### 示例 2: Show pod resource usage

```bash
kubectl top pods
```

### 示例 3: Show resource usage for all pods

```bash
kubectl top pods -A
```

### 示例 4: Show container-level resource usage

```bash
kubectl top pods --containers
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; requires metrics-server installed

## 所属维度

[[Container Orchestration-MOC|Container Orchestration]]
