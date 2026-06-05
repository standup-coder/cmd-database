---
cmd_name: kubectl get volumesnapshotcontent
cmd_category: "容器编排/K8s存储增强"
cmd_dimension: Kubernetes Storage Management
cmd_install: kubectl with CSI snapshot controller
cmd_platforms:
- linux
- darwin
- windows
summary: "List VolumeSnapshotContent resources representing actual snapshots"
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


# kubectl get volumesnapshotcontent

> List VolumeSnapshotContent resources representing actual snapshots

## 安装

```bash
kubectl with CSI snapshot controller
```

## 用法

```
kubectl get volumesnapshotcontent [name] [flags]
```

## 示例

### 示例 1: List all volume snapshot contents

```bash
kubectl get volumesnapshotcontent
```

### 示例 2: Describe specific snapshot content

```bash
kubectl describe volumesnapshotcontent snapcontent-12345
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows actual snapshots

## 所属维度

[[K8s存储增强-MOC|Kubernetes Storage Management]]
