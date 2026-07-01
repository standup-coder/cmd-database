---
{
  "cmd_name": "kfp run submit",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-mlops.yaml"
}
---

# kfp run submit

> Submit a Kubeflow Pipeline run

## 安装

```bash
pip install kfp
```

## 用法

```
kfp run submit [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e, --experiment-name` | Name of experiment |
| `-r, --run-name` | Name for this run |
| `-f, --package-file` | Path to pipeline package file |
| `-p, --pipeline-name` | Name of existing pipeline |

## 示例

### 示例 1: Submit pipeline run from file

```bash
kfp run submit -e my-experiment -r run-001 -f pipeline.yaml
```

### 示例 2: Submit run using existing pipeline

```bash
kfp run submit -e prod -p training-pipeline -r daily-train
```

## 风险提示

> ⚠️ **MEDIUM**: Creates pipeline run; consumes cluster resources

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
