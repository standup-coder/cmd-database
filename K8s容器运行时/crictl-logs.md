---
{
  "cmd_name": "crictl logs",
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

# crictl logs

> Fetch logs of a container

## 安装

```bash
Download from https://github.com/kubernetes-sigs/cri-tools/releases
```

## 用法

```
crictl logs [container-id] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Follow log output |
| `--tail` | Number of lines to show from the end of the logs |
| `--since` | Show logs since timestamp |

## 示例

### 示例 1: Print container logs

```bash
crictl logs <container-id>
```

### 示例 2: Follow container logs in real-time

```bash
crictl logs -f <container-id>
```

### 示例 3: Show last 100 lines of logs

```bash
crictl logs --tail=100 <container-id>
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; views logs only

## 所属维度

[[K8s容器运行时-MOC|Kubernetes Container Runtime]]
