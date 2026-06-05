---
cmd_name: lm-eval
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install lm-eval
cmd_platforms:
- linux
- darwin
- windows
summary: "EleutherAI语言模型评估框架，支持HellaSwag、MMLU、ARC等100+基准测试"
cmd_level: intermediate
cmd_related:
- opencompass
- alpaca-eval
cmd_tags:
- training
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# lm-eval

> EleutherAI语言模型评估框架，支持HellaSwag、MMLU、ARC等100+基准测试

## 安装

```bash
pip install lm-eval
```

## 用法

```
lm_eval [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | 模型类型 (hf, vllm, gguf) |
| `--tasks` | 评估任务列表，逗号分隔 |
| `--batch_size` | 推理批次大小 |
| `--output_path` | 结果输出目录 |

## 示例

### 示例 1: 在多个基准上评估LLaMA-2-7B

```bash
lm_eval --model hf --model_args pretrained=meta-llama/Llama-2-7b --tasks hellaswag,arc_challenge,mmlu --batch_size=8
```

### 示例 2: 使用vLLM加速评估

```bash
lm_eval --model vllm --model_args pretrained=Qwen/Qwen2-7B --tasks mmlu --batch_size=auto
```

## 关联命令

- [[opencompass]]
- [[alpaca-eval]]

## 风险提示

> ⚠️ **LOW**: 只读评估操作，无风险

## 参考链接

- [https://github.com/EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
