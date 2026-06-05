---
cmd_name: multilingual-eval
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: pip install lm-eval
cmd_platforms:
- linux
- darwin
summary: "多语言能力评测，支持C-Eval(中文)、MMLU多语言、XCOPA、XNLI等跨语言基准"
cmd_level: intermediate
cmd_related:
- lm-eval
- opencompass
cmd_tags:
- evaluation
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# multilingual-eval

> 多语言能力评测，支持C-Eval(中文)、MMLU多语言、XCOPA、XNLI等跨语言基准

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
| `--tasks` | 评测任务 (ceval, mmlu, xcopa, xnli) |
| `--num_fewshot` | few-shot数量 |
| `--batch_size` | 推理批次大小 |

## 示例

### 示例 1: 中文+英文多语言评测

```bash
lm_eval --model hf --model_args pretrained=meta-llama/Llama-3-8B --tasks ceval,mmlu --num_fewshot 5 --batch_size 8
```

### 示例 2: 跨语言推理评测

```bash
lm_eval --model hf --model_args pretrained=Qwen/Qwen2-72B --tasks xcopa,xnli --device cuda
```

## 关联命令

- [[lm-eval]]
- [[opencompass]]

## 风险提示

> ⚠️ **LOW**: 多语言评测覆盖文化差异

## 参考链接

- [https://github.com/EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
