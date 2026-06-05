---
cmd_name: trtexec
cmd_category: AI基础设施/AI编译器
cmd_dimension: AI编译器
cmd_install: docker pull nvcr.io/nvidia/tensorrt
cmd_platforms:
- linux
summary: "TensorRT引擎构建与性能测试工具，将ONNX/UFF转为TensorRT序列化引擎，极致NVIDIA GPU优化"
cmd_level: intermediate
cmd_related:
- tensorrt-llm
- onnx-optimizer
cmd_tags:
- compiler
- gpu
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/ai-compiler.yaml
---


# trtexec

> TensorRT引擎构建与性能测试工具，将ONNX/UFF转为TensorRT序列化引擎，极致NVIDIA GPU优化

## 安装

```bash
docker pull nvcr.io/nvidia/tensorrt
```

## 用法

```
trtexec [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--onnx` | 输入ONNX模型路径 |
| `--saveEngine` | 输出引擎文件路径 |
| `--fp16` | 启用FP16混合精度 |
| `--int8` | 启用INT8量化 |
| `--workspace` | 工作区大小(MB) |
| `--maxBatch` | 最大批处理大小 |

## 示例

### 示例 1: ONNX转TensorRT FP16引擎

```bash
trtexec --onnx=model.onnx --saveEngine=model.trt --fp16 --workspace=4096
```

### 示例 2: TensorRT引擎性能基准测试

```bash
trtexec --loadEngine=model.trt --batch=8 --iterations=100 --avgRuns=10
```

### 示例 3: INT8量化引擎构建

```bash
trtexec --onnx=model.onnx --saveEngine=model_int8.trt --int8 --calib=calibration.cache
```

## 关联命令

- [[tensorrt-llm]]
- [[onnx-optimizer]]

## 风险提示

> ⚠️ **MEDIUM**: 量化可能损失精度，需验证

## 参考链接

- [https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html)

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
