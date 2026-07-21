---
{
  "cmd_name": "crictl images",
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

# crictl images

> List container images

## 安装

```bash
Download from https://github.com/kubernetes-sigs/cri-tools/releases
```

## 用法

```
crictl images [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-q` | Only display image IDs |
| `--no-trunc` | Show full image ID |

## 示例

### 示例 1: List all images

```bash
crictl images
```

### 示例 2: List only image IDs

```bash
crictl images -q
```

### 示例 3: List nginx images

```bash
crictl images nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists images only

## 所属维度

[[K8s容器运行时-MOC|Kubernetes Container Runtime]]
