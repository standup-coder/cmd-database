---
cmd_name: opacus
cmd_category: AI基础设施/联邦学习
cmd_dimension: 联邦学习
cmd_install: pip install opacus
cmd_platforms:
- linux
- darwin
- windows
summary: "Opacus PyTorch差分隐私训练库，通过梯度裁剪和噪声注入实现(ε,δ)-差分隐私保证"
cmd_level: intermediate
cmd_related:
- flower
cmd_tags:
- training
- federated
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/federated-learning.yaml
---


# opacus

> Opacus PyTorch差分隐私训练库，通过梯度裁剪和噪声注入实现(ε,δ)-差分隐私保证

## 安装

```bash
pip install opacus
```

## 用法

```
python train.py (使用opacus库)
```

## 参数

| Flag | Description |
|------|-------------|
| `PrivacyEngine` | 隐私引擎 |
| `max_grad_norm` | 梯度裁剪阈值 |
| `noise_multiplier` | 噪声乘数 |
| `target_epsilon` | 目标隐私预算 |

## 示例

### 示例 1: 模型添加差分隐私保护

```bash
python -c "from opacus import PrivacyEngine; engine = PrivacyEngine(); model, optimizer, loader = engine.make_private(model, optimizer, loader, noise_multiplier=1.0, max_grad_norm=1.0)"
```

### 示例 2: 指定隐私预算训练

```bash
python dp_train.py --epsilon 3.0 --delta 1e-5 --epochs 10
```

## 关联命令

- [[flower]]

## 风险提示

> ⚠️ **MEDIUM**: 隐私预算过小会严重影响模型精度

## 参考链接

- [https://opacus.ai/](https://opacus.ai/)

## 所属维度

[[联邦学习-MOC|AI基础设施/联邦学习]]
