---
{
  "cmd_name": "kubectl get volumeattachments",
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

# kubectl get volumeattachments

> List VolumeAttachment resources showing volume-node associations

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get volumeattachments [name] [flags]
```

## 示例

### 示例 1: List all volume attachments

```bash
kubectl get volumeattachments
```

### 示例 2: Describe specific volume attachment

```bash
kubectl describe volumeattachment csi-12345678
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows volume mounting status

## 所属维度

[[Kubernetes Storage Management-MOC|Kubernetes Storage Management]]
