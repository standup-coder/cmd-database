---
{
  "cmd_name": "cleanlab",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install cleanlab",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "label-studio",
    "snorkel"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/data-labeling.yaml"
}
---

# cleanlab

> Cleanlab数据清洗与噪声检测，自动发现标注错误、异常样本和数据冲突

## 安装

```bash
pip install cleanlab
```

## 用法

```
python clean.py (使用cleanlab库)
```

## 参数

| Flag | Description |
|------|-------------|
| `find_label_issues` | 发现标注错误 |
| `find_outliers` | 发现异常样本 |
| `Datalab` | 综合数据质量分析 |

## 示例

### 示例 1: 检测数据集中的标注错误

```bash
python -c "from cleanlab import find_label_issues; issues = find_label_issues(labels, pred_probs)"
```

### 示例 2: 全面数据质量审计

```bash
python data_audit.py --dataset train.csv --model resnet50 --find_issues label outlier near_duplicate
```

## 关联命令

- [[label-studio]]
- [[snorkel]]

## 风险提示

> ⚠️ **LOW**: 只读分析操作，不改数据

## 参考链接

- [https://cleanlab.ai/](https://cleanlab.ai/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
