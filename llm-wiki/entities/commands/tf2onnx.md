---
cmd_name: tf2onnx
cmd_category: AI基础设施/模型生态
cmd_dimension: 模型生态
cmd_install: pip install tf2onnx
cmd_platforms:
- linux
- darwin
- windows
summary: "TensorFlow到ONNX转换工具，支持SavedModel、Checkpoint、Keras模型"
cmd_level: intermediate
cmd_related:
- onnxruntime
- optimum-cli
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-hub.yaml
---


# tf2onnx

> TensorFlow到ONNX转换工具，支持SavedModel、Checkpoint、Keras模型

## 安装

```bash
pip install tf2onnx
```

## 用法

```
python -m tf2onnx.convert [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--saved-model` | SavedModel路径 |
| `--checkpoint` | Checkpoint路径 |
| `--keras` | Keras模型文件 |
| `--output` | 输出ONNX文件 |

## 示例

### 示例 1: 转换SavedModel为ONNX

```bash
python -m tf2onnx.convert --saved-model ./saved_model --output model.onnx
```

### 示例 2: 转换Keras模型为ONNX

```bash
python -m tf2onnx.convert --keras model.h5 --output model.onnx
```

## 关联命令

- [[onnxruntime]]
- [[optimum-cli]]

## 风险提示

> ⚠️ **LOW**: 格式转换安全

## 参考链接

- [https://github.com/onnx/tensorflow-onnx](https://github.com/onnx/tensorflow-onnx)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
