---
{
  "cmd_name": "kubectl rollout",
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

# kubectl rollout

> Manage the rollout of a resource

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl rollout [subcommand] [resource]
```

## 参数

| Flag | Description |
|------|-------------|
| `status` | Show rollout status |
| `history` | View rollout history |
| `undo` | Rollback to previous revision |
| `restart` | Restart a resource |

## 示例

### 示例 1: Check deployment rollout status

```bash
kubectl rollout status deployment/nginx
```

### 示例 2: View deployment history

```bash
kubectl rollout history deployment/nginx
```

### 示例 3: Rollback to previous version

```bash
kubectl rollout undo deployment/nginx
```

### 示例 4: Restart deployment (recreate pods)

```bash
kubectl rollout restart deployment/nginx
```

## 风险提示

> ⚠️ **HIGH**: Rollback may cause temporary service disruption

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
