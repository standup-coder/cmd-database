---
cmd_name: tritonserver
cmd_category: AI基础设施/模型服务
cmd_dimension: 模型服务
cmd_install: docker pull nvcr.io/nvidia/tritonserver:24.01-py3
cmd_platforms:
- linux
summary: "NVIDIA Triton推理服务器，支持TensorRT、ONNX、PyTorch、Python后端，多模型并行服务"
cmd_level: advanced
cmd_related:
- bentoml
- torchserve
cmd_tags:
- inference
- advanced
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/model-serving.yaml
---


# tritonserver

> NVIDIA Triton推理服务器，支持TensorRT、ONNX、PyTorch、Python后端，多模型并行服务

## 安装

```bash
docker pull nvcr.io/nvidia/tritonserver:24.01-py3
```

## 用法

```
tritonserver [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model-repository` | 模型仓库路径 |
| `--http-port` | HTTP服务端口号 |
| `--grpc-port` | gRPC服务端口号 |
| `--strict-model-config` | 严格模型配置检查 |
| `--load-model` | 指定加载的模型 |

## 示例

### 示例 1: 启动Triton服务加载/models目录下所有模型

```bash
tritonserver --model-repository=/models --http-port=8000 --grpc-port=8001
```

### 示例 2: Docker GPU部署Triton推理服务

```bash
docker run --gpus all --rm -p 8000:8000 -p 8001:8001 -v $(pwd)/models:/models nvcr.io/nvidia/tritonserver:24.01-py3 tritonserver --model-repository=/models
```

## 关联命令

- [[bentoml]]
- [[torchserve]]

## 风险提示

> ⚠️ **MEDIUM**: 生产部署需配置认证和资源限制

## 参考链接

- [https://github.com/triton-inference-server/server](https://github.com/triton-inference-server/server)

## 所属维度

[[模型服务-MOC|AI基础设施/模型服务]]
