---
cmd_name: kubectl annotate
cmd_category: "容器编排/Kubernetes命令"
cmd_dimension: Container Orchestration
cmd_install: Download from https://kubernetes.io/docs/tasks/tools/
cmd_platforms:
- linux
- darwin
- windows
summary: "Update annotations on a resource"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/kubernetes.yaml
---


# kubectl annotate

> Update annotations on a resource

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl annotate [resource] [name] [key=value]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Namespace |
| `--overwrite` | Overwrite existing annotation |

## 示例

### 示例 1: Add annotation to pod

```bash
kubectl annotate pods mypod description='My application pod'
```

### 示例 2: Remove annotation from pod

```bash
kubectl annotate pods mypod description-
```

## 风险提示

> ⚠️ **LOW**: Annotations are metadata only; minimal risk

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
