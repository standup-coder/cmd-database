---
cmd_name: attention-rollout
cmd_category: AI基础设施/模型可解释性
cmd_dimension: 模型可解释性
cmd_install: pip install attention-rollout
cmd_platforms:
- linux
- darwin
- windows
summary: "Attention Rollout跨层注意力传播追踪，识别输入token到输出token的完整注意力路径"
cmd_level: intermediate
cmd_related:
- bertviz
- token-heatmap
cmd_tags:
- interpretability
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-interpretability.yaml
---


# attention-rollout

> Attention Rollout跨层注意力传播追踪，识别输入token到输出token的完整注意力路径

## 安装

```bash
pip install attention-rollout
```

## 用法

```
python visualize.py (使用attention_rollout库)
```

## 参数

| Flag | Description |
|------|-------------|
| `AttentionRollout` | Rollout分析器 |
| `discard_ratio` | 低注意力阈值过滤 |

## 示例

### 示例 1: 生成注意力rollout掩码

```bash
python -c "from attention_rollout import AttentionRollout; rollout = AttentionRollout(model, discard_ratio=0.9); mask = rollout(input_ids)"
```

### 示例 2: ViT第11层注意力rollout可视化

```bash
python rollout_viz.py --model vit-base --image cat.jpg --layer 11
```

## 关联命令

- [[bertviz]]
- [[token-heatmap]]

## 风险提示

> ⚠️ **LOW**: 可视化工具安全

## 参考链接

- [https://github.com/jacobgil/vit-explain](https://github.com/jacobgil/vit-explain)

## 所属维度

[[模型可解释性-MOC|AI基础设施/模型可解释性]]
