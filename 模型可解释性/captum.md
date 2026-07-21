---
{
  "cmd_name": "captum",
  "cmd_category": "AI基础设施/模型可解释性",
  "cmd_dimension": "模型可解释性",
  "cmd_install": "pip install captum",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "shap",
    "lime"
  ],
  "cmd_tags": [
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

# captum

> Captum PyTorch模型可解释性库，集成梯度、DeepLIFT、集成梯度、特征消融等多种归因方法

## 安装

```bash
pip install captum
```

## 用法

```
python explain.py (使用captum库)
```

## 参数

| Flag | Description |
|------|-------------|
| `IntegratedGradients` | 集成梯度归因 |
| `DeepLift` | DeepLIFT归因 |
| `GradientShap` | 梯度SHAP |
| `LayerConductance` | 层导电性分析 |
| `FeatureAblation` | 特征消融测试 |

## 示例

### 示例 1: 集成梯度特征归因

```bash
python -c "from captum.attr import IntegratedGradients; ig = IntegratedGradients(model); attrs = ig.attribute(input, target=0)"
```

### 示例 2: 中间层神经元贡献分析

```bash
python -c "from captum.attr import LayerConductance; lc = LayerConductance(model, model.layer); attrs = lc.attribute(input, target=0)"
```

## 关联命令

- [[shap]]
- [[lime]]

## 风险提示

> ⚠️ **LOW**: 归因方法选择影响结论

## 参考链接

- [https://captum.ai/](https://captum.ai/)

## 所属维度

[[模型可解释性-MOC|AI基础设施/模型可解释性]]
