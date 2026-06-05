---
cmd_name: speculative-decoding
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install transformers
cmd_platforms:
- linux
- darwin
summary: "推测解码(Speculative Decoding)加速推理，用小草稿模型预测大目标模型输出，2-3倍加速"
cmd_level: intermediate
cmd_related:
- vllm
- sglang
cmd_tags:
- inference
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# speculative-decoding

> 推测解码(Speculative Decoding)加速推理，用小草稿模型预测大目标模型输出，2-3倍加速

## 安装

```bash
pip install transformers
```

## 用法

```
python infer.py (使用transformers的 assisted_generation)
```

## 参数

| Flag | Description |
|------|-------------|
| `assistant_model` | 草稿模型 |
| `num_assistant_tokens` | 每次推测token数 |

## 示例

### 示例 1: TinyLlama草稿加速LLaMA-70B

```bash
python -c "from transformers import pipeline; gen = pipeline('text-generation', model='meta-llama/Llama-2-70b', assistant_model='TinyLlama/TinyLlama-1.1B'); gen('Hello', num_assistant_tokens=5)"
```

### 示例 2: 配置推测解码参数

```bash
python speculative.py --target llama-70b --draft tinyllama --speedup 2.5
```

## 关联命令

- [[vllm]]
- [[sglang]]

## 风险提示

> ⚠️ **LOW**: 推理加速技术

## 参考链接

- [https://huggingface.co/blog/assisted-generation](https://huggingface.co/blog/assisted-generation)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
