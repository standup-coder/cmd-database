---
cmd_name: llava
cmd_category: AI基础设施/多模态
cmd_dimension: 多模态
cmd_install: git clone https://github.com/haotian-liu/LLaVA.git
cmd_platforms:
- linux
- darwin
summary: "LLaVA大语言视觉助手，视觉指令微调，支持图像问答、描述、推理"
cmd_level: intermediate
cmd_related:
- clip
- transformers-pipeline
cmd_tags:
- inference
- multimodal
- fine-tuning
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/multimodal.yaml
---


# llava

> LLaVA大语言视觉助手，视觉指令微调，支持图像问答、描述、推理

## 安装

```bash
git clone https://github.com/haotian-liu/LLaVA.git
```

## 用法

```
python -m llava.serve.cli [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model-path` | 模型路径 |
| `--image-file` | 输入图像 |
| `--load-4bit` | 4-bit量化加载 |

## 示例

### 示例 1: 图像问答交互

```bash
python -m llava.serve.cli --model-path liuhaotian/llava-v1.5-7b --image-file image.jpg
```

### 示例 2: 启动LLaVA控制器服务

```bash
python -m llava.serve.controller --host 0.0.0.0 --port 10000
```

## 关联命令

- [[clip]]
- [[transformers-pipeline]]

## 风险提示

> ⚠️ **LOW**: 本地推理安全

## 参考链接

- [https://github.com/haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA)

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]
