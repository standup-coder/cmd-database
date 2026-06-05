---
cmd_name: xformers
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install xformers
cmd_platforms:
- linux
- darwin
- windows
summary: "Meta开源的高效Transformer组件库，提供memory_efficient_attention等优化算子"
cmd_level: intermediate
cmd_related:
- flash-attn
- lightning
cmd_tags:
- training
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# xformers

> Meta开源的高效Transformer组件库，提供memory_efficient_attention等优化算子

## 安装

```bash
pip install xformers
```

## 用法

```
python train.py (导入xformers库使用)
```

## 参数

| Flag | Description |
|------|-------------|
| `memory_efficient_attention` | 内存高效注意力实现 |
| `xFormersConfig` | 配置Transformer优化策略 |

## 示例

### 示例 1: 使用xFormers内存高效注意力训练

```bash
python train.py --use_xformers --attention_op=memory_efficient
```

### 示例 2: 直接使用xFormers注意力算子

```bash
python -c "from xformers.ops import memory_efficient_attention; y = memory_efficient_attention(q, k, v)"
```

## 关联命令

- [[flash-attn]]
- [[lightning]]

## 风险提示

> ⚠️ **LOW**: 纯性能优化组件，不改变训练逻辑

## 参考链接

- [https://github.com/facebookresearch/xformers](https://github.com/facebookresearch/xformers)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
