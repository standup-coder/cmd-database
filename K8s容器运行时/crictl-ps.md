---
{
  "cmd_name": "crictl ps",
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

# crictl ps

> List running containers

## 安装

```bash
Download from https://github.com/kubernetes-sigs/cri-tools/releases
```

## 用法

```
crictl ps [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | Show all containers (default shows just running) |
| `-q` | Only display container IDs |
| `--pod` | Filter by pod ID |

## 示例

### 示例 1: List running containers

```bash
crictl ps
```

### 示例 2: List all containers including stopped ones

```bash
crictl ps -a
```

### 示例 3: List containers in specific pod

```bash
crictl ps --pod <pod-id>
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists containers only

## 所属维度

[[K8s容器运行时-MOC|Kubernetes Container Runtime]]
