---
{
  "cmd_name": "tilt up",
  "cmd_category": "Kubernetes Development",
  "cmd_dimension": "Kubernetes Development",
  "cmd_install": "Download from https://docs.tilt.dev/install.html",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-dev.yaml"
}
---

# tilt up

> Start Tilt development environment

## 安装

```bash
Download from https://docs.tilt.dev/install.html
```

## 用法

```
tilt up [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--port` | Web UI port |
| `--context` | Kubernetes context |

## 示例

### 示例 1: Start Tilt with web UI

```bash
tilt up
```

### 示例 2: Start with custom UI port

```bash
tilt up --port 8080
```

### 示例 3: Start with specific context

```bash
tilt up --context minikube
```

## 风险提示

> ⚠️ **MEDIUM**: Deploys to cluster with live updates

## 所属维度

[[K8s开发调试-MOC|Kubernetes Development]]
