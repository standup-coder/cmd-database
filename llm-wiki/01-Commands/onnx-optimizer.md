---
{
  "cmd_name": "onnx-optimizer",
  "cmd_category": "AI基础设施/AI编译器",
  "cmd_dimension": "AI编译器",
  "cmd_install": "pip install onnxoptimizer",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "trtexec",
    "iree-compile"
  ],
  "cmd_tags": [
    "inference",
    "compiler",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-compiler.yaml"
}
---

# onnx-optimizer

> ONNX模型图优化器，常量折叠、算子融合、死代码消除，跨平台推理前必备优化

## 安装

```bash
pip install onnxoptimizer
```

## 用法

```
python optimize.py (使用onnxoptimizer库)
```

## 参数

| Flag | Description |
|------|-------------|
| `optimize` | 执行优化 |
| `--passes` | 优化pass列表 |

## 示例

### 示例 1: 默认优化pass优化ONNX模型

```bash
python -c "import onnx, onnxoptimizer; model = onnx.load('model.onnx'); model_opt = onnxoptimizer.optimize(model); onnx.save(model_opt, 'model_opt.onnx')"
```

### 示例 2: 指定融合和常量提取优化

```bash
python -c "import onnxoptimizer; passes = ['fuse_bn_into_conv', 'fuse_pad_into_conv', 'extract_constant_to_initializer']; model_opt = onnxoptimizer.optimize(model, passes)"
```

## 关联命令

- [[trtexec]]
- [[iree-compile]]

## 风险提示

> ⚠️ **LOW**: 优化后需验证输出一致性

## 参考链接

- [https://github.com/onnx/optimizer](https://github.com/onnx/optimizer)

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
