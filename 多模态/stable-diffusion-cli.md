---
{
  "cmd_name": "stable-diffusion-cli",
  "cmd_category": "AI基础设施/多模态",
  "cmd_dimension": "多模态",
  "cmd_install": "pip install diffusers transformers accelerate",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "comfyui",
    "clip"
  ],
  "cmd_tags": [
    "multimodal",
    "peft",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/multimodal.yaml"
}
---

# stable-diffusion-cli

> Stable Diffusion文本到图像生成命令行工具，支持多种模型和LoRA

## 安装

```bash
pip install diffusers transformers accelerate
```

## 用法

```
python generate.py (使用diffusers库)
```

## 参数

| Flag | Description |
|------|-------------|
| `--prompt` | 生成提示词 |
| `--model` | 模型ID |
| `--width` | 图像宽度 |
| `--height` | 图像高度 |
| `--steps` | 采样步数 |

## 示例

### 示例 1: SDXL文本生成图像

```bash
python generate.py --prompt 'a cat wearing a hat' --model stabilityai/stable-diffusion-xl-base-1.0 --steps 30
```

### 示例 2: 使用LoRA风格生成

```bash
python generate.py --prompt 'cyberpunk city' --lora ./lora_weights --seed 42
```

## 关联命令

- [[comfyui]]
- [[clip]]

## 风险提示

> ⚠️ **MEDIUM**: 注意生成内容的合规性

## 参考链接

- [https://github.com/Stability-AI/stablediffusion](https://github.com/Stability-AI/stablediffusion)

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]
