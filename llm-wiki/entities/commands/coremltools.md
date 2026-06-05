---
cmd_name: coremltools
cmd_category: AI基础设施/模型生态
cmd_dimension: 模型生态
cmd_install: pip install coremltools
cmd_platforms:
- darwin
- linux
summary: "Apple CoreML模型转换工具，将PyTorch/TensorFlow转换为iOS/macOS原生格式"
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


# coremltools

> Apple CoreML模型转换工具，将PyTorch/TensorFlow转换为iOS/macOS原生格式

## 安装

```bash
pip install coremltools
```

## 用法

```
python convert.py (使用coremltools库)
```

## 参数

| Flag | Description |
|------|-------------|
| `ct.convert` | 转换模型 |
| `compute_units` | 计算单元 (cpu_only, cpu_and_gpu, all) |

## 示例

### 示例 1: 转换PyTorch模型为CoreML

```bash
python -c "import coremltools as ct; mlmodel = ct.convert(traced_model, inputs=[ct.ImageType()]); mlmodel.save('model.mlpackage')"
```

## 关联命令

- [[onnxruntime]]
- [[optimum-cli]]

## 风险提示

> ⚠️ **LOW**: 转换操作安全

## 参考链接

- [https://coremltools.readme.io/](https://coremltools.readme.io/)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
