---
cmd_name: clip
cmd_category: AI基础设施/多模态
cmd_dimension: 多模态
cmd_install: pip install git+https://github.com/openai/CLIP.git
cmd_platforms:
- linux
- darwin
- windows
summary: "OpenAI CLIP图文对齐模型，零样本图像分类、图文相似度计算、图像检索"
cmd_level: intermediate
cmd_related:
- llava
- transformers-pipeline
cmd_tags:
- multimodal
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/multimodal.yaml
---


# clip

> OpenAI CLIP图文对齐模型，零样本图像分类、图文相似度计算、图像检索

## 安装

```bash
pip install git+https://github.com/openai/CLIP.git
```

## 用法

```
python app.py (使用clip库)
```

## 参数

| Flag | Description |
|------|-------------|
| `clip.load()` | 加载模型 |
| `encode_text()` | 编码文本 |
| `encode_image()` | 编码图像 |

## 示例

### 示例 1: 计算图文相似度

```bash
python -c "import clip, torch; m, p = clip.load('ViT-B/32'); i = p(torch.randn(1,3,224,224)); t = clip.tokenize(['a dog']); logits = m(i, t)"
```

### 示例 2: 零样本图像分类

```bash
python zero_shot.py --model ViT-L/14 --classes 'cat,dog,bird,car' --image folder/
```

## 关联命令

- [[llava]]
- [[transformers-pipeline]]

## 风险提示

> ⚠️ **LOW**: 推理安全

## 参考链接

- [https://github.com/openai/CLIP](https://github.com/openai/CLIP)

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]
