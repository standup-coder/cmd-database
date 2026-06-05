---
cmd_name: mt-bench
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: pip install fastchat
cmd_platforms:
- linux
- darwin
- windows
summary: "MT-Bench多轮对话评测基准，80个高质量多轮问题，GPT-4作为裁判评分"
cmd_level: intermediate
cmd_related:
- arena
- alpaca-eval
cmd_tags:
- evaluation
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# mt-bench

> MT-Bench多轮对话评测基准，80个高质量多轮问题，GPT-4作为裁判评分

## 安装

```bash
pip install fastchat
```

## 用法

```
python gen_judgment.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bench-name` | 评测名称 (mt_bench, mt_bench_category) |
| `--model-list` | 评测模型列表 |
| `--judge-model` | 裁判模型 (默认gpt-4) |

## 示例

### 示例 1: 多模型MT-Bench评测

```bash
python gen_judgment.py --bench-name mt_bench --model-list llama-3-70b gpt-4 qwen-72b
```

### 示例 2: 使用GPT-4-Turbo裁判

```bash
python gen_judgment.py --bench-name mt_bench --judge-model gpt-4-turbo
```

## 关联命令

- [[arena]]
- [[alpaca-eval]]

## 风险提示

> ⚠️ **LOW**: 调用GPT-4 API需消耗token

## 参考链接

- [https://github.com/lm-sys/FastChat](https://github.com/lm-sys/FastChat)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
