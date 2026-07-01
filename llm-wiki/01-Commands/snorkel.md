---
{
  "cmd_name": "snorkel",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install snorkel",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cleanlab",
    "label-studio"
  ],
  "cmd_tags": [
    "training",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/data-labeling.yaml"
}
---

# snorkel

> Snorkel弱监督标注框架，通过编程方式生成训练标签，减少人工标注成本

## 安装

```bash
pip install snorkel
```

## 用法

```
python label.py (使用snorkel库)
```

## 参数

| Flag | Description |
|------|-------------|
| `@labeling_function` | 定义标注函数 |
| `LabelModel` | 训练标签模型聚合弱标签 |
| `PandasLFApplier` | 应用标注函数到DataFrame |

## 示例

### 示例 1: 使用标注函数自动标注数据

```bash
python snorkel_label.py --data train.csv --lf_file labeling_functions.py
```

### 示例 2: 训练标签模型聚合多个弱监督源

```bash
python -c "from snorkel.labeling import LabelModel; label_model = LabelModel(cardinality=2); label_model.fit(L_train)"
```

## 关联命令

- [[cleanlab]]
- [[label-studio]]

## 风险提示

> ⚠️ **MEDIUM**: 弱监督标签质量依赖标注函数设计，需验证

## 参考链接

- [https://www.snorkel.org/](https://www.snorkel.org/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
