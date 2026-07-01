---
{
  "cmd_name": "megatron-lm",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "git clone https://github.com/NVIDIA/Megatron-LM.git",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "deepspeed",
    "torchrun"
  ],
  "cmd_tags": [
    "training",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# megatron-lm

> NVIDIA Megatron-LM大规模语言模型训练框架，支持张量/流水线/序列并行

## 安装

```bash
git clone https://github.com/NVIDIA/Megatron-LM.git
```

## 用法

```
python pretrain_gpt.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--tensor-model-parallel-size` | 张量并行度 |
| `--pipeline-model-parallel-size` | 流水线并行度 |
| `--sequence-parallel` | 启用序列并行 |
| `--use-distributed-optimizer` | 使用分布式优化器 |

## 示例

### 示例 1: 8x8并行训练GPT-3级别大模型

```bash
python pretrain_gpt.py --tensor-model-parallel-size 8 --pipeline-model-parallel-size 8 --num-layers 96 --hidden-size 12288
```

### 示例 2: 从检查点生成样本

```bash
python tools/generate_samples_gpt.py --load checkpoint --num-samples 100
```

## 关联命令

- [[deepspeed]]
- [[torchrun]]

## 风险提示

> ⚠️ **HIGH**: 大规模并行训练配置复杂，需专业调优

## 参考链接

- [https://github.com/NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
