---
cmd_name: ctr images list
cmd_category: "容器编排/K8s容器运行时"
cmd_dimension: Kubernetes Container Runtime
cmd_install: Installed with containerd
cmd_platforms:
- linux
summary: "List images in containerd"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-runtime.yaml
---


# ctr images list

> List images in containerd

## 安装

```bash
Installed with containerd
```

## 用法

```
ctr images list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-q` | Print only the image refs |

## 示例

### 示例 1: List all containerd images

```bash
ctr images list
```

### 示例 2: List only image references

```bash
ctr images list -q
```

### 示例 3: List images in k8s.io namespace

```bash
ctr -n k8s.io images list
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists images only

## 所属维度

[[K8s容器运行时-MOC|Kubernetes Container Runtime]]
