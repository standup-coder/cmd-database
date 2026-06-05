---
cmd_name: text-generation-inference
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: docker pull ghcr.io/huggingface/text-generation-inference:latest
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace TGI文本生成推理服务，生产级部署方案"
cmd_level: intermediate
cmd_related:
- vllm
- sglang
cmd_tags:
- inference
- deployment
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# text-generation-inference

> HuggingFace TGI文本生成推理服务，生产级部署方案

## 安装

```bash
docker pull ghcr.io/huggingface/text-generation-inference:latest
```

## 用法

```
docker run [OPTIONS] ghcr.io/huggingface/text-generation-inference:latest
```

## 参数

| Flag | Description |
|------|-------------|
| `--model-id` | HuggingFace模型ID |
| `--sharded` | 启用模型分片 |
| `--num-shard` | 分片数量(GPU数) |
| `--quantize` | 量化方式(awq,gptq,bitsandbytes) |

## 示例

### 示例 1: Docker部署LLaMA-3.1推理服务

```bash
docker run --gpus all -p 8080:80 ghcr.io/huggingface/text-generation-inference:latest --model-id meta-llama/Llama-3.1-8B-Instruct
```

### 示例 2: 4卡分片部署70B模型

```bash
docker run --gpus all -p 8080:80 ghcr.io/huggingface/text-generation-inference:latest --model-id meta-llama/Llama-3.1-70B-Instruct --sharded true --num-shard 4
```

## 关联命令

- [[vllm]]
- [[sglang]]

## 风险提示

> ⚠️ **MEDIUM**: 生产部署需配置安全认证

## 参考链接

- [https://huggingface.co/docs/text-generation-inference](https://huggingface.co/docs/text-generation-inference)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
