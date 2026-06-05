---
cmd_name: bitsandbytes
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install bitsandbytes
cmd_platforms:
- linux
- darwin
- windows
summary: "8-bit/4-bit量化库，支持QLoRA在消费级GPU上训练大模型"
cmd_level: intermediate
cmd_related:
- peft
- unsloth
cmd_tags:
- training
- peft
- quantization
- gpu
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# bitsandbytes

> 8-bit/4-bit量化库，支持QLoRA在消费级GPU上训练大模型

## 安装

```bash
pip install bitsandbytes
```

## 用法

```
python train.py (导入bitsandbytes库使用)
```

## 参数

| Flag | Description |
|------|-------------|
| `BitsAndBytesConfig` | 配置量化参数(load_in_4bit, bnb_4bit_compute_dtype) |
| `load_in_8bit` | 使用8-bit量化加载模型 |
| `load_in_4bit` | 使用4-bit量化加载模型(NF4/FP4) |

## 示例

### 示例 1: 使用NF4量化进行QLoRA训练

```bash
python qlora_train.py --load_in_4bit --bnb_4bit_quant_type=nf4
```

### 示例 2: 8-bit量化推理，自动分配层到GPU/CPU

```bash
python inference.py --load_in_8bit --device_map=auto
```

## 关联命令

- [[peft]]
- [[unsloth]]

## 风险提示

> ⚠️ **MEDIUM**: 量化可能带来精度损失，需评估模型质量

## 参考链接

- [https://github.com/TimDettmers/bitsandbytes](https://github.com/TimDettmers/bitsandbytes)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
