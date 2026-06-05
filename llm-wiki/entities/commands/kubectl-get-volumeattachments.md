---
cmd_name: kubectl get volumeattachments
cmd_category: "容器编排/K8s存储增强"
cmd_dimension: Kubernetes Storage Management
cmd_install: kubectl built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "List VolumeAttachment resources showing volume-node associations"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- rag
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-storage-management.yaml
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

[[K8s存储增强-MOC|Kubernetes Storage Management]]
