---
cmd_name: flash-attn
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install flash-attn --no-build-isolation
cmd_platforms:
- linux
summary: "Flash Attention高效注意力实现，2-4倍加速长序列训练，显著降低内存占用"
cmd_level: intermediate
cmd_related:
- xformers
- unsloth
cmd_tags:
- training
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# flash-attn

> Flash Attention高效注意力实现，2-4倍加速长序列训练，显著降低内存占用

## 安装

```bash
pip install flash-attn --no-build-isolation
```

## 用法

```
python train.py (导入flash_attn库使用)
```

## 参数

| Flag | Description |
|------|-------------|
| `flash_attn_func` | Flash Attention核心函数 |
| `FlashAttention2` | Flash Attention 2模块 |

## 示例

### 示例 1: 使用Flash Attention 2训练32K长文本

```bash
python train.py --use_flash_attention_2 --max_seq_length=32768
```

### 示例 2: 安装Flash Attention(需要CUDA)

```bash
pip install flash-attn --no-build-isolation
```

## 关联命令

- [[xformers]]
- [[unsloth]]

## 风险提示

> ⚠️ **LOW**: 计算结果与标准Attention一致，仅优化性能

## 参考链接

- [https://github.com/Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
