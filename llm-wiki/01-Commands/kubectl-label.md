---
{
  "cmd_name": "kubectl label",
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

# kubectl label

> Update labels on a resource

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl label [resource] [name] [key=value]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Namespace |
| `--overwrite` | Overwrite existing label |

## 示例

### 示例 1: Add label to pod

```bash
kubectl label pods mypod env=production
```

### 示例 2: Overwrite existing label

```bash
kubectl label pods mypod env=staging --overwrite
```

### 示例 3: Remove label from pod

```bash
kubectl label pods mypod env-
```

## 风险提示

> ⚠️ **MEDIUM**: Changing labels can affect service selectors and routing

## 所属维度

[[Container Orchestration-MOC|Container Orchestration]]
