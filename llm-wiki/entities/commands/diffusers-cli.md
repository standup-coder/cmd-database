---
cmd_name: diffusers-cli
cmd_category: AI基础设施/模型架构
cmd_dimension: 模型架构
cmd_install: pip install diffusers
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace Diffusers扩散模型工具，管理文生图/视频模型管线、调度器配置"
cmd_level: intermediate
cmd_related:
- transformers-cli
- comfyui
cmd_tags:
- architecture
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-architecture.yaml
---


# diffusers-cli

> HuggingFace Diffusers扩散模型工具，管理文生图/视频模型管线、调度器配置

## 安装

```bash
pip install diffusers
```

## 用法

```
diffusers-cli [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `env` | 环境信息 |
| `convert` | 模型转换 |

## 示例

### 示例 1: 查看Diffusers环境

```bash
diffusers-cli env
```

### 示例 2: 加载扩散模型管线

```bash
python -c "from diffusers import StableDiffusionPipeline; pipe = StableDiffusionPipeline.from_pretrained('runwayml/stable-diffusion-v1-5')"
```

## 关联命令

- [[transformers-cli]]
- [[comfyui]]

## 风险提示

> ⚠️ **LOW**: 模型下载占用存储

## 参考链接

- [https://huggingface.co/docs/diffusers](https://huggingface.co/docs/diffusers)

## 所属维度

[[模型架构-MOC|AI基础设施/模型架构]]
