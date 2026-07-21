---
{
  "cmd_name": "stern",
  "cmd_category": "Kubernetes Utilities",
  "cmd_dimension": "Kubernetes Utilities",
  "cmd_install": "Download from https://github.com/stern/stern",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-utilities.yaml"
}
---

# stern

> Multi-pod and container log tailing for Kubernetes

## 安装

```bash
Download from https://github.com/stern/stern
```

## 用法

```
stern [pod-query] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Namespace to filter |
| `-c` | Container name filter (regex) |
| `--since` | Show logs since duration (e.g., 5m, 1h) |
| `-t` | Show timestamps |

## 示例

### 示例 1: Tail logs from pods matching 'nginx'

```bash
stern nginx
```

### 示例 2: Tail nginx pods in production namespace

```bash
stern nginx -n production
```

### 示例 3: Tail all pods in default namespace

```bash
stern . -n default
```

### 示例 4: Show logs from last 15 minutes

```bash
stern --since 15m nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; tails logs only

## 所属维度

[[K8s辅助工具-MOC|Kubernetes Utilities]]
