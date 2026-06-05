---
cmd_name: vllm
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install vllm
cmd_platforms:
- linux
- darwin
summary: "vLLM高性能大模型推理引擎，采用PagedAttention实现最高24倍吞吐提升"
cmd_level: intermediate
cmd_related:
- sglang
- lmdeploy
cmd_tags:
- inference
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# vllm

> vLLM高性能大模型推理引擎，采用PagedAttention实现最高24倍吞吐提升

## 安装

```bash
pip install vllm
```

## 用法

```
vllm serve [OPTIONS]
```

```
python -m vllm.entrypoints.openai.api_server [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | 模型路径或HuggingFace模型ID |
| `--tensor-parallel-size` | 张量并行GPU数量 |
| `--max-model-len` | 最大序列长度 |
| `--gpu-memory-utilization` | GPU内存利用率上限(0.0-1.0) |
| `--quantization` | 量化方式 (awq, gptq, fp8) |

## 示例

### 示例 1: 2卡张量并行部署LLaMA-3.1-8B

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 2
```

### 示例 2: 8卡部署Qwen2-72B，支持32K上下文

```bash
vllm serve Qwen/Qwen2-72B --tensor-parallel-size 8 --max-model-len 32768
```

### 示例 3: AWQ量化部署，节省显存

```bash
vllm serve TheBloke/Llama-2-70B-AWQ --quantization awq --gpu-memory-utilization 0.9
```

## 关联命令

- [[sglang]]
- [[lmdeploy]]

## 风险提示

> ⚠️ **MEDIUM**: 高并发推理可能耗尽GPU资源

## 参考链接

- [https://docs.vllm.ai/](https://docs.vllm.ai/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
