---
{
  "cmd_name": "kubectl cp",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "rag",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-storage-management.yaml"
}
---

# kubectl cp

> Copy files between local filesystem and pod

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl cp [source] [destination] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | Container name if pod has multiple containers |
| `-n` | Namespace |

## 示例

### 示例 1: Copy local file to pod

```bash
kubectl cp /local/data.txt mypod:/data/data.txt -n production
```

### 示例 2: Copy file from pod to local

```bash
kubectl cp mypod:/data/logs.txt /local/logs.txt -n production
```

### 示例 3: Copy entire directory to pod

```bash
kubectl cp /backup/ mypod:/restore/ -n production
```

## 风险提示

> ⚠️ **MEDIUM**: Transfers data between environments

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
