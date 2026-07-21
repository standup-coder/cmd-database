---
{
  "cmd_name": "tensorrt-llm",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install tensorrt-llm",
  "cmd_platforms": [
    "linux",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "vllm",
    "onnxruntime"
  ],
  "cmd_tags": [
    "inference",
    "gpu",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# tensorrt-llm

> NVIDIA TensorRT-LLM推理优化库，针对NVIDIA GPU极致优化

## 安装

```bash
pip install tensorrt-llm
```

## 用法

```
trtllm-build [OPTIONS]
```

```
python run.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--checkpoint_dir` | 检查点目录 |
| `--output_dir` | TensorRT引擎输出目录 |
| `--dtype` | 数据类型 (float16, bfloat16, float32) |
| `--max_batch_size` | 最大批次大小 |

## 示例

### 示例 1: 构建TensorRT推理引擎

```bash
trtllm-build --checkpoint_dir ./tllm_checkpoint --output_dir ./trt_engines --gemm_plugin float16
```

### 示例 2: 使用TensorRT引擎推理

```bash
python run.py --engine_dir=./trt_engines --max_output_len=512
```

## 关联命令

- [[vllm]]
- [[onnxruntime]]

## 风险提示

> ⚠️ **MEDIUM**: 需NVIDIA GPU和CUDA环境，引擎构建耗时

## 参考链接

- [https://github.com/NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
