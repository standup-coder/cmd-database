---
{
  "cmd_name": "pyvertical",
  "cmd_category": "AI基础设施/联邦学习",
  "cmd_dimension": "联邦学习",
  "cmd_install": "pip install pyvertical",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "flower",
    "opacus"
  ],
  "cmd_tags": [
    "federated",
    "data",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/federated-learning.yaml"
}
---

# pyvertical

> PyVertical垂直联邦学习框架，特征分片联合建模，适用于银行+电商等跨机构数据互补场景

## 安装

```bash
pip install pyvertical
```

## 用法

```
python train.py (使用pyvertical库)
```

## 参数

| Flag | Description |
|------|-------------|
| `VerticalDataLoader` | 垂直数据加载器 |
| `splitnn` | SplitNN模型分割 |

## 示例

### 示例 1: 垂直分布式数据加载

```bash
python -c "from pyvertical import VerticalDataLoader; loader = VerticalDataLoader(dataset, batch_size=32, distributed=True)"
```

### 示例 2: 两方特征分片联合训练

```bash
python vfl_train.py --parties 2 --feature_split 10,20 --epochs 50
```

## 关联命令

- [[flower]]
- [[opacus]]

## 风险提示

> ⚠️ **HIGH**: 垂直联邦存在特征对齐泄露风险，需安全求交(PSI)

## 参考链接

- [https://github.com/Actionable-Business-Intelligence/pyvertical](https://github.com/Actionable-Business-Intelligence/pyvertical)

## 所属维度

[[联邦学习-MOC|AI基础设施/联邦学习]]
