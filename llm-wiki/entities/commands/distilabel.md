---
cmd_name: distilabel
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install distilabel
cmd_platforms:
- linux
- darwin
- windows
summary: "Distilabel合成数据生成与模型蒸馏框架，用LLM生成高质量训练数据，支持自对弈和批评"
cmd_level: intermediate
cmd_related:
- dpo
- grpo
cmd_tags:
- training
- data
- distillation
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# distilabel

> Distilabel合成数据生成与模型蒸馏框架，用LLM生成高质量训练数据，支持自对弈和批评

## 安装

```bash
pip install distilabel
```

## 用法

```
python pipeline.py (使用distilabel库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Pipeline` | 数据生成流水线 |
| `Task` | 生成任务定义 |
| ` UltraFeedback` | 偏好数据生成 |

## 示例

### 示例 1: 构建数据生成流水线

```bash
python -c "from distilabel.pipeline import Pipeline; p = Pipeline(name='sft-data'); p.load(...)"
```

### 示例 2: 合成指令数据

```bash
python generate_synthetic.py --task instruction_following --model gpt-4 --num_samples 10000
```

## 关联命令

- [[dpo]]
- [[grpo]]

## 风险提示

> ⚠️ **LOW**: 合成数据需质量验证

## 参考链接

- [https://github.com/argilla-io/distilabel](https://github.com/argilla-io/distilabel)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
