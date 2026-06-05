---
cmd_name: grpo
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install trl
cmd_platforms:
- linux
- darwin
summary: "GRPO (Group Relative Policy Optimization) 强化学习训练，DeepSeek-R1核心训练方法，无需价值模型"
cmd_level: intermediate
cmd_related:
- trl
- dpo
cmd_tags:
- training
- rlhf
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# grpo

> GRPO (Group Relative Policy Optimization) 强化学习训练，DeepSeek-R1核心训练方法，无需价值模型

## 安装

```bash
pip install trl
```

## 用法

```
python grpo_train.py (使用trl库)
```

## 参数

| Flag | Description |
|------|-------------|
| `--model_name` | 基础模型 |
| `--reward_funcs` | 奖励函数列表 |
| `--num_generations` | 每组生成样本数 |
| `--beta` | KL散度惩罚系数 |

## 示例

### 示例 1: GRPO训练配置

```bash
python -c "from trl import GRPOTrainer; trainer = GRPOTrainer(model='Qwen/Qwen2.5-7B', reward_funcs=[accuracy_reward, format_reward])"
```

### 示例 2: 完整GRPO训练流程

```bash
python grpo_train.py --model_name Qwen2.5-7B --num_generations 8 --beta 0.04 --output_dir ./grpo_output
```

## 关联命令

- [[trl]]
- [[dpo]]

## 风险提示

> ⚠️ **MEDIUM**: RL训练不稳定，需监控奖励曲线

## 参考链接

- [https://huggingface.co/docs/trl/grpo_trainer](https://huggingface.co/docs/trl/grpo_trainer)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
