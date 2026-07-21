---
{
  "cmd_name": "skaffold run",
  "cmd_category": "Kubernetes Development",
  "cmd_dimension": "Kubernetes Development",
  "cmd_install": "Download from https://skaffold.dev/docs/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-dev.yaml"
}
---

# skaffold run

> Build and deploy application once

## 安装

```bash
Download from https://skaffold.dev/docs/install/
```

## 用法

```
skaffold run [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace` | Deploy to specific namespace |
| `--tail` | Stream logs after deployment |

## 示例

### 示例 1: Build and deploy once

```bash
skaffold run
```

### 示例 2: Deploy to staging namespace

```bash
skaffold run --namespace staging
```

### 示例 3: Deploy and stream logs

```bash
skaffold run --tail
```

## 风险提示

> ⚠️ **HIGH**: Deploys application to cluster

## 所属维度

[[K8s开发调试-MOC|Kubernetes Development]]
