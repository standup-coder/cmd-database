---
cmd_name: timm
cmd_category: AI基础设施/模型架构
cmd_dimension: 模型架构
cmd_install: pip install timm
cmd_platforms:
- linux
- darwin
- windows
summary: "PyTorch Image Models库，800+预训练视觉模型，涵盖ViT、ConvNeXt、Swin Transformer等"
cmd_level: intermediate
cmd_related:
- transformers-cli
- clip
cmd_tags:
- training
- architecture
- pre-training
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-architecture.yaml
---


# timm

> PyTorch Image Models库，800+预训练视觉模型，涵盖ViT、ConvNeXt、Swin Transformer等

## 安装

```bash
pip install timm
```

## 用法

```
python vision.py (使用timm库)
```

## 参数

| Flag | Description |
|------|-------------|
| `create_model` | 创建模型 |
| `list_models` | 列出模型 |
| `pretrained` | 加载预训练权重 |

## 示例

### 示例 1: 加载ViT-B/16预训练模型

```bash
python -c "import timm; model = timm.create_model('vit_base_patch16_224', pretrained=True)"
```

### 示例 2: 列出所有ViT变体

```bash
python -c "import timm; print(timm.list_models('*vit*'))"
```

## 关联命令

- [[transformers-cli]]
- [[clip]]

## 风险提示

> ⚠️ **LOW**: 模型下载占用存储

## 参考链接

- [https://github.com/huggingface/pytorch-image-models](https://github.com/huggingface/pytorch-image-models)

## 所属维度

[[模型架构-MOC|AI基础设施/模型架构]]
