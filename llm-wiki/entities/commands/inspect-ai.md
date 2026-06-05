---
cmd_name: inspect-ai
cmd_category: AI基础设施/AI安全
cmd_dimension: AI安全
cmd_install: pip install inspect-ai
cmd_platforms:
- linux
- darwin
- windows
summary: "UK AISI Inspect AI评测框架，系统化评估模型知识、推理、安全性和能力"
cmd_level: intermediate
cmd_related:
- lm-eval
- safety-eval
cmd_tags:
- inference
- evaluation
- safety
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ai-safety.yaml
---


# inspect-ai

> UK AISI Inspect AI评测框架，系统化评估模型知识、推理、安全性和能力

## 安装

```bash
pip install inspect-ai
```

## 用法

```
inspect [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `eval` | 运行评测 |
| `view` | 查看评测结果 |
| `list` | 列出任务 |

## 示例

### 示例 1: 运行安全评测

```bash
inspect eval security_eval.py --model openai/gpt-4
```

### 示例 2: 数学能力多次评测

```bash
inspect eval math_eval.py --model anthropic/claude-3-sonnet --epochs 3
```

## 关联命令

- [[lm-eval]]
- [[safety-eval]]

## 风险提示

> ⚠️ **LOW**: 评测框架安全

## 参考链接

- [https://github.com/UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai)

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]
