---
{
  "cmd_name": "kfp experiment create",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "pip install kfp",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-mlops.yaml"
}
---

# kfp experiment create

> Create a Kubeflow Pipelines experiment

## 安装

```bash
pip install kfp
```

## 用法

```
kfp experiment create <name> [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d, --description` | Experiment description |

## 示例

### 示例 1: Create new experiment

```bash
kfp experiment create my-experiment
```

### 示例 2: Create experiment with description

```bash
kfp experiment create prod-training -d 'Production training experiments'
```

## 风险提示

> ⚠️ **LOW**: Creates metadata only

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
