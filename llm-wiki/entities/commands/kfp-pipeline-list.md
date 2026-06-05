---
cmd_name: kfp pipeline list
cmd_category: "容器编排/K8s机器学习运维"
cmd_dimension: Kubernetes MLOps
cmd_install: pip install kfp
cmd_platforms:
- linux
- darwin
- windows
summary: "List Kubeflow Pipelines"
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


# kfp pipeline list

> List Kubeflow Pipelines

## 安装

```bash
pip install kfp
```

## 用法

```
kfp pipeline list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--page-size` | Number of pipelines to return |

## 示例

### 示例 1: List all pipelines

```bash
kfp pipeline list
```

### 示例 2: List pipelines with pagination

```bash
kfp pipeline list --page-size 50
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
