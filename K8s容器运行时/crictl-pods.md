---
{
  "cmd_name": "crictl pods",
  "cmd_category": "Kubernetes Container Runtime",
  "cmd_dimension": "Kubernetes Container Runtime",
  "cmd_install": "Download from https://github.com/kubernetes-sigs/cri-tools/releases",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-runtime.yaml"
}
---

# crictl pods

> List all pods

## 安装

```bash
Download from https://github.com/kubernetes-sigs/cri-tools/releases
```

## 用法

```
crictl pods [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-q` | Only display pod IDs |
| `--namespace` | Filter by namespace |
| `--name` | Filter by pod name |

## 示例

### 示例 1: List all pods

```bash
crictl pods
```

### 示例 2: List pods in kube-system namespace

```bash
crictl pods --namespace kube-system
```

### 示例 3: List only pod IDs

```bash
crictl pods -q
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists pods only

## 所属维度

[[K8s容器运行时-MOC|Kubernetes Container Runtime]]
