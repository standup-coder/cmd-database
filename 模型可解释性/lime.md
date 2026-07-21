---
{
  "cmd_name": "lime",
  "cmd_category": "AI基础设施/模型可解释性",
  "cmd_dimension": "模型可解释性",
  "cmd_install": "pip install lime",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "shap",
    "captum"
  ],
  "cmd_tags": [
    "training",
    "interpretability",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-interpretability.yaml"
}
---

# lime

> LIME (Local Interpretable Model-agnostic Explanations) 局部代理模型解释，扰动样本训练可解释模型

## 安装

```bash
pip install lime
```

## 用法

```
python explain.py (使用lime库)
```

## 参数

| Flag | Description |
|------|-------------|
| `LimeTabularExplainer` | 表格数据解释器 |
| `LimeTextExplainer` | 文本数据解释器 |
| `LimeImageExplainer` | 图像数据解释器 |

## 示例

### 示例 1: 表格数据局部解释

```bash
python -c "from lime.lime_tabular import LimeTabularExplainer; explainer = LimeTabularExplainer(X, feature_names=names); exp = explainer.explain_instance(x, model.predict_proba)"
```

### 示例 2: 文本分类局部解释

```bash
python -c "from lime.lime_text import LimeTextExplainer; explainer = LimeTextExplainer(); exp = explainer.explain_instance(text, classifier)"
```

## 关联命令

- [[shap]]
- [[captum]]

## 风险提示

> ⚠️ **LOW**: 局部解释不代表全局行为

## 参考链接

- [https://github.com/marcotcr/lime](https://github.com/marcotcr/lime)

## 所属维度

[[模型可解释性-MOC|AI基础设施/模型可解释性]]
