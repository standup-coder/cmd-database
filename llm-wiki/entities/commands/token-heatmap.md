---
cmd_name: token-heatmap
cmd_category: AI基础设施/模型可解释性
cmd_dimension: 模型可解释性
cmd_install: pip install transformers-interpret
cmd_platforms:
- linux
- darwin
- windows
summary: "Token级别归因热图，可视化每个输入token对模型输出的贡献度，定位幻觉和错误关注"
cmd_level: intermediate
cmd_related:
- bertviz
- captum
cmd_tags:
- interpretability
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-interpretability.yaml
---


# token-heatmap

> Token级别归因热图，可视化每个输入token对模型输出的贡献度，定位幻觉和错误关注

## 安装

```bash
pip install transformers-interpret
```

## 用法

```
python visualize.py (使用transformers_interpret库)
```

## 参数

| Flag | Description |
|------|-------------|
| `SequenceClassificationExplainer` | 序列分类解释器 |
| `explainer` | 调用解释方法 |

## 示例

### 示例 1: 生成分类token归因

```bash
python -c "from transformers_interpret import SequenceClassificationExplainer; explainer = SequenceClassificationExplainer(model, tokenizer); word_attributions = explainer(text)"
```

### 示例 2: 负面分类的token贡献热图

```bash
python token_heatmap.py --model bert-base-uncased --text 'This movie is terrible' --class 0
```

## 关联命令

- [[bertviz]]
- [[captum]]

## 风险提示

> ⚠️ **LOW**: 可视化工具安全

## 参考链接

- [https://github.com/cdpierse/transformers-interpret](https://github.com/cdpierse/transformers-interpret)

## 所属维度

[[模型可解释性-MOC|AI基础设施/模型可解释性]]
