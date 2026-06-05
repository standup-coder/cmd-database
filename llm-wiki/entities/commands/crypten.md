---
cmd_name: crypten
cmd_category: AI基础设施/联邦学习
cmd_dimension: 联邦学习
cmd_install: pip install crypten
cmd_platforms:
- linux
- darwin
cmd_level: intermediate
cmd_related:
- flower
- opacus
cmd_tags:
- linux
- darwin
- intermediate
cmd_risk_level: low
summary: CrypTen Facebook隐私计算库，基于MPC(安全多方计算)的加密机器学习，支持加密推理和训练
created: '2026-06-04'
source_file: data/ai/federated-learning.yaml
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

### 加密张量基本操作

```bash
python -c "import crypten; crypten.init(); x_enc = crypten.cryptensor([1.0, 2.0]); print(x_enc.get_plain_text())"
```

### 两方加密推理

```bash
python secure_inference.py --model model.pth --input data.csv --world_size 2
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接

- https://github.com/facebookresearch/CrypTen

## 所属维度

[[联邦学习-MOC|AI基础设施/联邦学习]]
