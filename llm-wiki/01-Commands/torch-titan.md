---
{
  "cmd_name": "torch-titan",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "git clone https://github.com/pytorch/torchtitan.git",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "torchrun",
    "deepspeed"
  ],
  "cmd_tags": [
    "training",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# torch-titan

> PyTorch官方原生大模型训练参考实现，支持FSDP2、TP、PP、CP

## 安装

```bash
git clone https://github.com/pytorch/torchtitan.git
```

## 用法

```
torchrun [OPTIONS] train.py
```

## 参数

| Flag | Description |
|------|-------------|
| `--job.config_file` | 配置文件路径 |
| `--training.steps` | 训练步数 |
| `--model.flavor` | 模型规模 (debug, 7B, 13B, 70B) |

## 示例

### 示例 1: 8卡训练LLaMA-3-8B

```bash
torchrun --nproc_per_node=8 train.py --job.config_file train_configs/llama3_8b.toml
```

### 示例 2: 70B模型分布式训练

```bash
torchrun --nproc_per_node=8 train.py --job.config_file train_configs/llama3_70b.toml --model.flavor 70B
```

## 关联命令

- [[torchrun]]
- [[deepspeed]]

## 风险提示

> ⚠️ **MEDIUM**: 官方参考实现，配置需仔细

## 参考链接

- [https://github.com/pytorch/torchtitan](https://github.com/pytorch/torchtitan)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
