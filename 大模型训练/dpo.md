---
{
  "cmd_name": "dpo",
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
    "grpo",
    "trl"
  ],
  "cmd_tags": [
    "training",
    "data",
    "rlhf",
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

# dpo

> DPO (Direct Preference Optimization) 直接偏好优化，无需奖励模型直接从偏好数据微调

## 安装

```bash
pip install trl
```

## 用法

```
python dpo_train.py (使用trl库)
```

## 参数

| Flag | Description |
|------|-------------|
| `--beta` | 温度参数，控制与参考模型的偏离程度 |
| `--loss_type` | 损失类型 (sigmoid, hinge, ipo, exppo) |
| `--label_smoothing` | 标签平滑系数 |

## 示例

### 示例 1: DPO训练配置

```bash
python -c "from trl import DPOTrainer; trainer = DPOTrainer(model, ref_model, beta=0.1, train_dataset=dataset)"
```

### 示例 2: 完整DPO偏好微调

```bash
python dpo_train.py --model_name llama-3-8b --beta 0.1 --loss_type sigmoid --dataset preference_data.json
```

## 关联命令

- [[grpo]]
- [[trl]]

## 风险提示

> ⚠️ **MEDIUM**: 偏好数据质量直接影响效果

## 参考链接

- [https://huggingface.co/docs/trl/dpo_trainer](https://huggingface.co/docs/trl/dpo_trainer)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
