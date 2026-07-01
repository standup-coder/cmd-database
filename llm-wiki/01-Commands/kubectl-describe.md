---
{
  "cmd_name": "kubectl describe",
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

# kubectl describe

> Show detailed information about a resource

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl describe [resource] [name]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Namespace to query |

## 示例

### 示例 1: Show details about a specific pod

```bash
kubectl describe pod mypod
```

### 示例 2: Show details about a node

```bash
kubectl describe node node-1
```

### 示例 3: Describe service in production namespace

```bash
kubectl describe service myservice -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Container Orchestration-MOC|Container Orchestration]]
