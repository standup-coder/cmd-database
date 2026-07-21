---
{
  "cmd_name": "llm-factory",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "git clone https://github.com/hiyouga/LLaMA-Factory.git && cd LLaMA-Factory && pip install -e '.[torch,metrics]'",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "axolotl",
    "unsloth"
  ],
  "cmd_tags": [
    "training",
    "inference",
    "quantization",
    "rlhf",
    "fine-tuning",
    "pre-training",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# llm-factory

> 一站式LLM训练平台，支持100+模型预训练、微调、RLHF、DPO、量化、推理

## 安装

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git && cd LLaMA-Factory && pip install -e '.[torch,metrics]'
```

## 用法

```
llamafactory-cli [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `train` | 启动训练 |
| `export` | 导出/合并模型 |
| `api` | 启动API服务 |
| `--stage` | 训练阶段 (sft, rm, ppo, dpo, kto) |

## 示例

### 示例 1: 使用Alpaca数据集进行SFT微调

```bash
llamafactory-cli train --stage sft --model_name_or_path meta-llama/Llama-2-7b --dataset alpaca_gpt4_en
```

### 示例 2: 导出模型并分片为2GB每个文件

```bash
llamafactory-cli export --model_name_or_path merged_model --export_dir ./export --export_size 2
```

### 示例 3: 启动OpenAI兼容API服务

```bash
llamafactory-cli api --model_name_or_path merged_model --template llama2
```

## 关联命令

- [[axolotl]]
- [[unsloth]]

## 风险提示

> ⚠️ **MEDIUM**: 训练消耗大量计算资源，量化可能损失精度

## 参考链接

- [https://github.com/hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
