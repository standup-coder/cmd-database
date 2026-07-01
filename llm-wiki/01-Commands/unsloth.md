---
{
  "cmd_name": "unsloth",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install unsloth",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "axolotl",
    "trl"
  ],
  "cmd_tags": [
    "training",
    "peft",
    "fine-tuning",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# unsloth

> 2-5倍加速的LLM微调框架，支持LoRA和QLoRA，内存占用减少80%

## 安装

```bash
pip install unsloth
```

## 用法

```
python train.py (使用unsloth库)
```

## 参数

| Flag | Description |
|------|-------------|
| `FastLanguageModel.from_pretrained` | 加载优化后的预训练模型 |
| `FastLanguageModel.get_peft_model` | 应用PEFT微调配置 |

## 示例

### 示例 1: 快速加载Unsloth优化模型

```bash
python -c "from unsloth import FastLanguageModel; model, tokenizer = FastLanguageModel.from_pretrained('unsloth/Llama-3.2-1B')"
```

### 示例 2: 使用Unsloth加速微调

```bash
python finetune.py --use_unsloth --max_seq_length=2048
```

## 关联命令

- [[axolotl]]
- [[trl]]

## 风险提示

> ⚠️ **LOW**: 优化后的训练更稳定，内存占用更低

## 参考链接

- [https://github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
