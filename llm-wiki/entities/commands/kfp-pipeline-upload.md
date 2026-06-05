---
cmd_name: kfp pipeline upload
cmd_category: "容器编排/K8s机器学习运维"
cmd_dimension: Kubernetes MLOps
cmd_install: pip install kfp
cmd_platforms:
- linux
- darwin
- windows
summary: "Upload a pipeline to Kubeflow Pipelines"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-mlops.yaml
---


# kfp pipeline upload

> Upload a pipeline to Kubeflow Pipelines

## 安装

```bash
pip install kfp
```

## 用法

```
kfp pipeline upload [flags] <pipeline-file>
```

## 参数

| Flag | Description |
|------|-------------|
| `-p, --pipeline-name` | Name for the pipeline |
| `-d, --description` | Pipeline description |

## 示例

### 示例 1: Upload pipeline with name

```bash
kfp pipeline upload -p my-pipeline pipeline.yaml
```

### 示例 2: Upload with description

```bash
kfp pipeline upload -p ml-training -d 'Training pipeline' train.yaml.tar.gz
```

## 风险提示

> ⚠️ **LOW**: Uploads pipeline definition only

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
