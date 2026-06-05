---
cmd_name: alpaca-eval
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install alpaca-eval
cmd_platforms:
- linux
- darwin
- windows
summary: "指令跟随能力评估工具，使用GPT-4作为裁判对模型输出进行排序"
cmd_level: intermediate
cmd_related:
- lm-eval
- opencompass
cmd_tags:
- training
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# alpaca-eval

> 指令跟随能力评估工具，使用GPT-4作为裁判对模型输出进行排序

## 安装

```bash
pip install alpaca-eval
```

## 用法

```
alpaca_eval [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model_outputs` | 模型输出JSON文件路径 |
| `--reference_outputs` | 参考模型输出(默认Davinci-003) |
| `--annotators_config` | 裁判模型配置(默认GPT-4) |

## 示例

### 示例 1: 评估模型在AlpacaEval基准上的表现

```bash
alpaca_eval --model_outputs outputs.json
```

### 示例 2: 使用Weighted AlpacaEval更准确地评估

```bash
alpaca_eval --model_outputs my_model.json --annotators_config=weighted_alpaca_eval_gpt4_turbo
```

## 关联命令

- [[lm-eval]]
- [[opencompass]]

## 风险提示

> ⚠️ **LOW**: 调用OpenAI API需消耗token，注意成本

## 参考链接

- [https://github.com/tatsu-lab/alpaca_eval](https://github.com/tatsu-lab/alpaca_eval)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
