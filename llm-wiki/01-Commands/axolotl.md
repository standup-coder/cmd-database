---
{
  "cmd_name": "axolotl",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install axolotl[flash-attn]",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "unsloth",
    "llm-factory"
  ],
  "cmd_tags": [
    "training",
    "peft",
    "fine-tuning",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# axolotl

> YAML配置式LLM微调工具，支持LoRA、QLoRA、全参数微调

## 安装

```bash
pip install axolotl[flash-attn]
```

## 用法

```
axolotl [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `train` | 启动训练 |
| `merge-lora` | 合并LoRA权重到基础模型 |
| `--config` | 指定YAML配置文件路径 |

## 示例

### 示例 1: 使用LoRA配置微调LLaMA-3

```bash
axolotl train examples/llama-3/lora.yml
```

### 示例 2: 合并训练好的LoRA权重

```bash
axolotl merge-lora --config=config.yml
```

### 示例 3: 仅准备数据集不开始训练

```bash
axolotl train config.yml --prepare-dataset
```

## 关联命令

- [[unsloth]]
- [[llm-factory]]

## 风险提示

> ⚠️ **MEDIUM**: 微调会修改模型权重，需备份基础模型

## 参考链接

- [https://github.com/axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
