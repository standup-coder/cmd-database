---
{
  "cmd_name": "openvino",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install openvino",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "onnxruntime",
    "optimum-cli"
  ],
  "cmd_tags": [
    "inference",
    "gpu",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# openvino

> Intel OpenVINO工具包，针对Intel CPU/GPU/NPU优化的推理框架

## 安装

```bash
pip install openvino
```

## 用法

```
ovc [OPTIONS]
```

```
benchmark_app [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--input_model` | 输入模型路径 |
| `--output_model` | 输出IR模型路径 |
| `--compress_to_fp16` | 压缩为FP16 |

## 示例

### 示例 1: 将ONNX模型转换为OpenVINO IR并压缩为FP16

```bash
ovc model.onnx --compress_to_fp16
```

### 示例 2: 在Intel CPU上基准测试模型性能

```bash
benchmark_app -m model.xml -d CPU
```

## 关联命令

- [[onnxruntime]]
- [[optimum-cli]]

## 风险提示

> ⚠️ **LOW**: 推理操作无副作用

## 参考链接

- [https://docs.openvino.ai/](https://docs.openvino.ai/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
