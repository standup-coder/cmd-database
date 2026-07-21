---
{
  "cmd_name": "optimum-cli",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install optimum[exporters]",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "onnxruntime",
    "auto-gptq"
  ],
  "cmd_tags": [
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# optimum-cli

> HuggingFace Optimum模型优化工具，支持ONNX/TensorRT/OpenVINO导出和量化

## 安装

```bash
pip install optimum[exporters]
```

## 用法

```
optimum-cli [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `export onnx` | 导出ONNX模型 |
| `export openvino` | 导出OpenVINO模型 |
| `export tflite` | 导出TensorFlow Lite模型 |
| `gptq` | GPTQ量化 |
| `awq` | AWQ量化 |

## 示例

### 示例 1: 导出ONNX格式模型

```bash
optimum-cli export onnx --model meta-llama/Llama-2-7b-hf --task text-generation-with-past ./onnx_model
```

### 示例 2: 4-bit GPTQ量化

```bash
optimum-cli gptq --model meta-llama/Llama-2-7b-hf --dataset c4 --bits 4
```

## 关联命令

- [[onnxruntime]]
- [[auto-gptq]]

## 风险提示

> ⚠️ **MEDIUM**: 量化可能损失精度，需验证输出

## 参考链接

- [https://huggingface.co/docs/optimum](https://huggingface.co/docs/optimum)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
