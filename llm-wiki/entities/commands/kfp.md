---
cmd_name: kfp
cmd_category: AI基础设施/MLOps平台
cmd_dimension: MLOps平台
cmd_install: pip install kfp
cmd_platforms:
- linux
- darwin
- windows
summary: "Kubeflow Pipelines (KFP) 命令行客户端"
cmd_level: intermediate
cmd_related:
- mlflow
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/mlops.yaml
---


# kfp

> Kubeflow Pipelines (KFP) 命令行客户端

## 安装

```bash
pip install kfp
```

## 用法

```
kfp [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `pipeline` | 管理Pipeline (upload, delete, get) |
| `run` | 管理Run (submit, list, get) |
| `experiment` | 管理Experiment (create, list, get) |

## 示例

### 示例 1: 上传一个pipeline

```bash
kfp pipeline upload -p my_pipeline.yaml my-pipeline
```

### 示例 2: 基于pipeline提交一个运行

```bash
kfp run submit -e my-experiment -p my-pipeline
```

## 关联命令

- [[mlflow]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 参考链接

- [https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/)

## 所属维度

[[MLOps平台-MOC|AI基础设施/MLOps平台]]
