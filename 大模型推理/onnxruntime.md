---
{
  "cmd_name": "onnxruntime",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install onnxruntime-gpu",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "optimum-cli",
    "openvino"
  ],
  "cmd_tags": [
    "inference",
    "edge",
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

# onnxruntime

> ONNX Runtime跨平台推理加速引擎，支持CPU/GPU/边缘设备

## 安装

```bash
pip install onnxruntime-gpu
```

## 用法

```
python inference.py (使用onnxruntime库)
```

## 参数

| Flag | Description |
|------|-------------|
| `InferenceSession` | 创建推理会话 |
| `run` | 执行推理 |

## 示例

### 示例 1: 加载ONNX模型并推理

```bash
python -c "import onnxruntime as ort; sess = ort.InferenceSession('model.onnx'); outputs = sess.run(None, inputs)"
```

### 示例 2: 将HuggingFace模型导出为ONNX格式

```bash
python export_onnx.py --model meta-llama/Llama-2-7b --output model.onnx
```

## 关联命令

- [[optimum-cli]]
- [[openvino]]

## 风险提示

> ⚠️ **LOW**: 推理操作无副作用

## 参考链接

- [https://onnxruntime.ai/](https://onnxruntime.ai/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
