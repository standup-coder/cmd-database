---
{
  "cmd_name": "trl",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install trl",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "axolotl",
    "peft"
  ],
  "cmd_tags": [
    "training",
    "rlhf",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# trl

> Transformers Reinforcement Learning，支持SFT、DPO、PPO、ORPO训练

## 安装

```bash
pip install trl
```

## 用法

```
trl [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `sft` | 监督微调 (Supervised Fine-Tuning) |
| `dpo` | 直接偏好优化 (Direct Preference Optimization) |
| `ppo` | 近端策略优化 (Proximal Policy Optimization) |

## 示例

### 示例 1: 使用Alpaca数据集进行SFT微调

```bash
trl sft --model_name_or_path meta-llama/Llama-2-7b --dataset_name tatsu-lab/alpaca
```

### 示例 2: 使用RLHF数据进行DPO训练

```bash
trl dpo --model_name_or_path model-sft --dataset_name anthropic/hh-rlhf
```

## 关联命令

- [[axolotl]]
- [[peft]]

## 风险提示

> ⚠️ **MEDIUM**: RL训练过程不稳定，需监控训练指标

## 参考链接

- [https://huggingface.co/docs/trl](https://huggingface.co/docs/trl)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
