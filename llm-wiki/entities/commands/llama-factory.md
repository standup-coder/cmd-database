---
cmd_name: llama-factory
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: git clone https://github.com/hiyouga/LLaMA-Factory.git && pip install
  -e .
cmd_platforms:
- linux
- darwin
- windows
summary: "LLaMA-Factory一站式大模型微调框架，支持100+模型，预训练/微调/DPO/RLHF全流程"
cmd_level: intermediate
cmd_related:
- unsloth
- axolotl
cmd_tags:
- training
- rlhf
- fine-tuning
- pre-training
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# llama-factory

> LLaMA-Factory一站式大模型微调框架，支持100+模型，预训练/微调/DPO/RLHF全流程

## 安装

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git && pip install -e .
```

## 用法

```
llamafactory-cli [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `train` | 训练模型 |
| `export` | 导出模型 |
| `api` | 启动API服务 |
| `webui` | 启动Web界面 |

## 示例

### 示例 1: LoRA监督微调LLaMA-3

```bash
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```

### 示例 2: 合并LoRA权重并导出

```bash
llamafactory-cli export --model_dir ./sft_model --export_dir ./merged --export_size 2
```

### 示例 3: 启动OpenAI兼容API

```bash
llamafactory-cli api --model_dir ./merged --template llama3
```

## 关联命令

- [[unsloth]]
- [[axolotl]]

## 风险提示

> ⚠️ **LOW**: 注意模型和数据路径配置

## 参考链接

- [https://github.com/hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
