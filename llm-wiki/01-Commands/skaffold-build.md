---
{
  "cmd_name": "skaffold build",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-dev.yaml"
}
---

# skaffold build

> Build container images only (no deployment)

## 安装

```bash
Download from https://skaffold.dev/docs/install/
```

## 用法

```
skaffold build [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--file-output` | Save built images to file |
| `--push` | Push images to registry |

## 示例

### 示例 1: Build images locally

```bash
skaffold build
```

### 示例 2: Build and push to registry

```bash
skaffold build --push
```

### 示例 3: Build and save image tags to file

```bash
skaffold build --file-output=images.json
```

## 风险提示

> ⚠️ **LOW**: Local build operation; no cluster deployment

## 所属维度

[[Kubernetes Development-MOC|Kubernetes Development]]
