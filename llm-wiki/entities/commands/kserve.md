---
cmd_name: kserve
cmd_category: AI基础设施/模型服务
cmd_dimension: 模型服务
cmd_install: kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve.yaml
cmd_platforms:
- linux
- darwin
- windows
summary: "KServe Kubernetes原生模型服务平台，支持自动扩缩容、金丝雀发布、多框架运行时"
cmd_level: intermediate
cmd_related:
- bentoml
- tritonserver
cmd_tags:
- kubernetes
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/model-serving.yaml
---


# kserve

> KServe Kubernetes原生模型服务平台，支持自动扩缩容、金丝雀发布、多框架运行时

## 安装

```bash
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve.yaml
```

## 用法

```
kubectl apply -f [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `apiVersion: serving.kserve.io/v1beta1` | KServe API版本 |
| `kind: InferenceService` | 推理服务资源类型 |
| `predictor` | 预测器配置(sklearn, xgboost, tensorflow, pytorch, triton) |

## 示例

### 示例 1: 部署sklearn模型推理服务

```bash
kubectl apply -f sklearn-iris.yaml
```

### 示例 2: 部署PyTorch模型到指定命名空间

```bash
kubectl apply -n kserve-test -f pytorch-model.yaml
```

### 示例 3: 查看所有推理服务状态

```bash
kubectl get inferenceservices
```

## 关联命令

- [[bentoml]]
- [[tritonserver]]

## 风险提示

> ⚠️ **MEDIUM**: 部署到K8s集群，需谨慎操作

## 参考链接

- [https://kserve.github.io/website/](https://kserve.github.io/website/)

## 所属维度

[[模型服务-MOC|AI基础设施/模型服务]]
