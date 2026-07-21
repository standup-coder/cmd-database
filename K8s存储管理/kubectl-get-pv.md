---
{
  "cmd_name": "kubectl get pv",
  "cmd_category": "Kubernetes Storage Management",
  "cmd_dimension": "Kubernetes Storage Management",
  "cmd_install": "kubectl built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-storage-management.yaml"
}
---

# kubectl get pv

> List PersistentVolume resources

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get pv [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | Output format: wide, yaml, json |
| `--show-labels` | Show labels in output |

## 示例

### 示例 1: List all persistent volumes

```bash
kubectl get pv
```

### 示例 2: List PVs with detailed information

```bash
kubectl get pv -o wide
```

### 示例 3: Get detailed YAML configuration

```bash
kubectl get pv -o yaml
```

### 示例 4: Describe specific persistent volume

```bash
kubectl describe pv my-pv
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows storage volumes

## 所属维度

[[K8s存储管理-MOC|Kubernetes Storage Management]]
