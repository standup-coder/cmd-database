---
cmd_name: neuronx-cc
cmd_category: AI基础设施/模型生态
cmd_dimension: 模型生态
cmd_install: pip install neuronx-cc
cmd_platforms:
- linux
summary: "AWS Neuron编译器，将PyTorch/TensorFlow模型编译为Trainium/Inferentia高效执行格式"
cmd_level: intermediate
cmd_related:
- optimum-cli
- onnxruntime
cmd_tags:
- compiler
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/model-hub.yaml
---


# neuronx-cc

> AWS Neuron编译器，将PyTorch/TensorFlow模型编译为Trainium/Inferentia高效执行格式

## 安装

```bash
pip install neuronx-cc
```

## 用法

```
neuronx-cc [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `compile` | 编译模型 |
| `--target` | 目标设备 (trn1, inf2) |

## 示例

### 示例 1: 编译模型为Neuron格式

```bash
neuronx-cc compile model.pt --target trn1 --output model_neff
```

## 关联命令

- [[optimum-cli]]
- [[onnxruntime]]

## 风险提示

> ⚠️ **MEDIUM**: AWS专用硬件编译

## 参考链接

- [https://aws.amazon.com/machine-learning/neuron/](https://aws.amazon.com/machine-learning/neuron/)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
