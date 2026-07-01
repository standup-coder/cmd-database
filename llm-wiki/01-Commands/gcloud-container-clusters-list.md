---
{
  "cmd_name": "gcloud container clusters list",
  "cmd_category": "Kubernetes Cloud Platforms",
  "cmd_dimension": "Kubernetes Cloud Platforms",
  "cmd_install": "Part of Google Cloud SDK; install from https://cloud.google.com/sdk/install",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cloud.yaml"
}
---

# gcloud container clusters list

> List Google GKE clusters

## 安装

```bash
Part of Google Cloud SDK; install from https://cloud.google.com/sdk/install
```

## 用法

```
gcloud container clusters list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--zone` | Filter by zone |
| `--format` | Output format: table, json, yaml |

## 示例

### 示例 1: List all GKE clusters

```bash
gcloud container clusters list
```

### 示例 2: List clusters in specific zone

```bash
gcloud container clusters list --zone us-central1-a
```

### 示例 3: List clusters in JSON format

```bash
gcloud container clusters list --format json
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists clusters only

## 所属维度

[[Kubernetes Cloud Platforms-MOC|Kubernetes Cloud Platforms]]
