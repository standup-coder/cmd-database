---
cmd_name: transformers-pipeline
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install transformers
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace Transformers Pipeline快速推理接口，一行代码完成文本生成/分类/问答"
cmd_level: intermediate
cmd_related:
- vllm
- onnxruntime
cmd_tags:
- inference
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# transformers-pipeline

> HuggingFace Transformers Pipeline快速推理接口，一行代码完成文本生成/分类/问答

## 安装

```bash
pip install transformers
```

## 用法

```
python inference.py (使用transformers库)
```

## 参数

| Flag | Description |
|------|-------------|
| `pipeline` | 创建推理管道(task, model, device) |
| `AutoModelForCausalLM` | 加载因果语言模型 |
| `AutoTokenizer` | 加载分词器 |

## 示例

### 示例 1: 一行代码创建文本生成管道

```bash
python -c "from transformers import pipeline; pipe = pipeline('text-generation', model='gpt2'); print(pipe('Hello')[0]['generated_text'])"
```

### 示例 2: 情感分析管道

```bash
python -c "from transformers import pipeline; pipe = pipeline('sentiment-analysis'); print(pipe('I love this product!'))"
```

## 关联命令

- [[vllm]]
- [[onnxruntime]]

## 风险提示

> ⚠️ **LOW**: 推理操作无副作用

## 参考链接

- [https://huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
