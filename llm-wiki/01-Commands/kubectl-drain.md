---
{
  "cmd_name": "kubectl drain",
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
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/kubernetes.yaml"
}
---

# kubectl drain

> Drain node in preparation for maintenance

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl drain [node-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--ignore-daemonsets` | Ignore DaemonSet-managed pods |
| `--delete-emptydir-data` | Delete pods with emptyDir volumes |
| `--force` | Force drain even if pods not managed by controller |
| `--grace-period` | Grace period for pod termination |

## 示例

### 示例 1: Drain node for maintenance

```bash
kubectl drain node-1 --ignore-daemonsets
```

### 示例 2: Drain node including emptyDir data

```bash
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data
```

## 风险提示

> ⚠️ **CRITICAL**: Evicts all pods from node; can cause service disruption if not properly planned

## 所属维度

[[Container Orchestration-MOC|Container Orchestration]]
