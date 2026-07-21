---
{
  "cmd_name": "peft",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install peft",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "bitsandbytes",
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

# peft

> 参数高效微调库，支持LoRA、QLoRA、IA3、Prompt Tuning等方法

## 安装

```bash
pip install peft
```

## 用法

```
python train.py (导入peft库使用)
```

## 参数

| Flag | Description |
|------|-------------|
| `LoraConfig` | 配置LoRA微调参数(rank, alpha, target_modules) |
| `get_peft_model` | 将PEFT配置应用到基础模型 |
| `PeftModel.from_pretrained` | 加载已保存的PEFT模型 |

## 示例

### 示例 1: 使用rank=16的LoRA微调注意力层

```bash
python lora_train.py --r=16 --lora_alpha=32 --target_modules=q_proj,v_proj
```

### 示例 2: 加载LoRA权重到基础模型

```bash
python -c "from peft import PeftModel; model = PeftModel.from_pretrained(base_model, './lora-weights')"
```

## 关联命令

- [[bitsandbytes]]
- [[trl]]

## 风险提示

> ⚠️ **LOW**: 只微调少量参数，风险较低

## 参考链接

- [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
