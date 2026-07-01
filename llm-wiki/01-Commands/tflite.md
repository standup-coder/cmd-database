---
{
  "cmd_name": "tflite",
  "cmd_category": "AI基础设施/边缘AI",
  "cmd_dimension": "边缘AI",
  "cmd_install": "pip install tensorflow",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "executorch",
    "coremltools"
  ],
  "cmd_tags": [
    "inference",
    "edge",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/edge-ai.yaml"
}
---

# tflite

> TensorFlow Lite移动端和嵌入式推理框架，支持Android/iOS/ARM/Raspberry Pi

## 安装

```bash
pip install tensorflow
```

## 用法

```
tflite_convert [OPTIONS]
```

```
python inference.py (使用tflite_runtime)
```

## 参数

| Flag | Description |
|------|-------------|
| `--saved_model_dir` | SavedModel路径 |
| `--output_file` | 输出TFLite文件 |
| `--optimizations` | 优化选项 (DEFAULT, OPTIMIZE_FOR_SIZE, OPTIMIZE_FOR_LATENCY) |

## 示例

### 示例 1: 转换SavedModel为TFLite

```bash
tflite_convert --saved_model_dir ./saved_model --output_file model.tflite
```

### 示例 2: TFLite推理

```bash
python -c "import tflite_runtime.interpreter as tflite; interpreter = tflite.Interpreter(model_path='model.tflite'); interpreter.allocate_tensors()"
```

## 关联命令

- [[executorch]]
- [[coremltools]]

## 风险提示

> ⚠️ **LOW**: 转换操作安全

## 参考链接

- [https://www.tensorflow.org/lite](https://www.tensorflow.org/lite)

## 所属维度

[[边缘AI-MOC|AI基础设施/边缘AI]]
