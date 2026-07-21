---
{
  "cmd_name": "skaffold dev",
  "cmd_category": "Kubernetes Development",
  "cmd_dimension": "Kubernetes Development",
  "cmd_install": "Download from https://skaffold.dev/docs/install/",
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

# skaffold dev

> Start Skaffold continuous development mode

## 安装

```bash
Download from https://skaffold.dev/docs/install/
```

## 用法

```
skaffold dev [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--port-forward` | Enable port forwarding |
| `--namespace` | Deploy to specific namespace |
| `--cleanup` | Cleanup deployments on exit |

## 示例

### 示例 1: Start development with auto-reload

```bash
skaffold dev
```

### 示例 2: Start with automatic port forwarding

```bash
skaffold dev --port-forward
```

### 示例 3: Deploy to dev namespace

```bash
skaffold dev --namespace dev
```

## 风险提示

> ⚠️ **MEDIUM**: Deploys to cluster; automatically rebuilds on code changes

## 所属维度

[[K8s开发调试-MOC|Kubernetes Development]]
