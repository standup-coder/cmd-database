---
{
  "cmd_name": "crypten",
  "cmd_category": "AI基础设施/联邦学习",
  "cmd_dimension": "联邦学习",
  "cmd_install": "pip install crypten",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flower",
    "opacus"
  ],
  "cmd_tags": [
    "training",
    "inference",
    "safety",
    "federated",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/federated-learning.yaml"
}
---

# crypten

> CrypTen Facebook隐私计算库，基于MPC(安全多方计算)的加密机器学习，支持加密推理和训练

## 安装

```bash
pip install crypten
```

## 用法

```
python secure_infer.py (使用crypten库)
```

## 参数

| Flag | Description |
|------|-------------|
| `crypten.init()` | 初始化MPC环境 |
| `crypten.cryptensor` | 加密张量 |
| `crypten.nn.from_pytorch` | PyTorch模型加密 |

## 示例

### 示例 1: 加密张量基本操作

```bash
python -c "import crypten; crypten.init(); x_enc = crypten.cryptensor([1.0, 2.0]); print(x_enc.get_plain_text())"
```

### 示例 2: 两方加密推理

```bash
python secure_inference.py --model model.pth --input data.csv --world_size 2
```

## 关联命令

- [[flower]]
- [[opacus]]

## 风险提示

> ⚠️ **MEDIUM**: MPC计算开销大，通信成本高

## 参考链接

- [https://github.com/facebookresearch/CrypTen](https://github.com/facebookresearch/CrypTen)

## 所属维度

[[联邦学习-MOC|AI基础设施/联邦学习]]
