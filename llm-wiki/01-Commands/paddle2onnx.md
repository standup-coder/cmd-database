---
{
  "cmd_name": "paddle2onnx",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install paddle2onnx",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tf2onnx",
    "onnxruntime"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# paddle2onnx

> PaddlePaddle到ONNX转换工具，支持Paddle模型导出为ONNX格式

## 安装

```bash
pip install paddle2onnx
```

## 用法

```
paddle2onnx [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model_dir` | Paddle模型目录 |
| `--model_filename` | 模型文件名 |
| `--save_file` | 输出ONNX文件 |

## 示例

### 示例 1: 转换Paddle模型为ONNX

```bash
paddle2onnx --model_dir ./inference_model --model_filename model.pdmodel --params_filename model.pdiparams --save_file model.onnx
```

### 示例 2: 查看 ONNX 转换帮助

```bash
paddle2onnx --help
```

## 关联命令

- [[tf2onnx]]
- [[onnxruntime]]

## 风险提示

> ⚠️ **LOW**: 格式转换安全

## 参考链接

- [https://github.com/PaddlePaddle/Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
