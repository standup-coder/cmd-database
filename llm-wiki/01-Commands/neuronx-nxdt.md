---
{
  "cmd_name": "neuronx-nxdt",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install neuronx-distributed-training",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "deepspeed",
    "megatron-lm"
  ],
  "cmd_tags": [
    "training",
    "distributed",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# neuronx-nxdt

> AWS Neuron分布式训练工具，针对Trainium芯片优化的LLM训练

## 安装

```bash
pip install neuronx-distributed-training
```

## 用法

```
python train.py (使用neuronx_distributed)
```

## 参数

| Flag | Description |
|------|-------------|
| `--tensor_parallel_size` | 张量并行大小 |
| `--pipeline_parallel_size` | 流水线并行大小 |

## 示例

### 示例 1: Trainium上8路张量并行训练

```bash
python train.py --tensor_parallel_size 8 --pipeline_parallel_size 1 --model_config config.json
```

### 示例 2: 查看 Trainium 分布式训练工具帮助

```bash
neuronx-nxdt --help
```

## 关联命令

- [[deepspeed]]
- [[megatron-lm]]

## 风险提示

> ⚠️ **MEDIUM**: Trainium专用，需AWS环境

## 参考链接

- [https://aws.amazon.com/machine-learning/trainium/](https://aws.amazon.com/machine-learning/trainium/)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
