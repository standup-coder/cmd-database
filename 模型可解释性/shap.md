---
{
  "cmd_name": "shap",
  "cmd_category": "AI基础设施/模型可解释性",
  "cmd_dimension": "模型可解释性",
  "cmd_install": "pip install shap",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lime",
    "captum"
  ],
  "cmd_tags": [
    "interpretability",
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-interpretability.yaml"
}
---

# shap

> SHAP (SHapley Additive exPlanations) 博弈论特征归因，精确量化每个特征对预测的贡献

## 安装

```bash
pip install shap
```

## 用法

```
python explain.py (使用shap库)
```

## 参数

| Flag | Description |
|------|-------------|
| `shap.TreeExplainer` | 树模型解释器 |
| `shap.DeepExplainer` | 深度学习解释器 |
| `shap.KernelExplainer` | 通用模型解释器 |
| `shap.summary_plot` | 特征重要性汇总图 |
| `shap.waterfall_plot` | 单样本瀑布图 |

## 示例

### 示例 1: 树模型全局特征重要性

```bash
python -c "import shap; explainer = shap.TreeExplainer(model); shap_values = explainer.shap_values(X); shap.summary_plot(shap_values, X)"
```

### 示例 2: 深度模型单样本归因

```bash
python -c "import shap; explainer = shap.DeepExplainer(model, background); shap_values = explainer.shap_values(X); shap.waterfall_plot(shap.Explanation(shap_values[0]))"
```

## 关联命令

- [[lime]]
- [[captum]]

## 风险提示

> ⚠️ **LOW**: 解释计算可能较慢，大样本需采样

## 参考链接

- [https://shap.readthedocs.io/](https://shap.readthedocs.io/)

## 所属维度

[[模型可解释性-MOC|AI基础设施/模型可解释性]]
