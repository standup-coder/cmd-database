---
{
  "cmd_name": "opencompass",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install -U opencompass",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lm-eval",
    "alpaca-eval"
  ],
  "cmd_tags": [
    "training",
    "evaluation",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# opencompass

> 上海AI Lab开源的模型评测平台，支持50+数据集和多种评测范式

## 安装

```bash
pip install -U opencompass
```

## 用法

```
opencompass [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行评测 |
| `--models` | 待评测模型列表 |
| `--datasets` | 评测数据集配置 |
| `--work-dir` | 工作目录 |

## 示例

### 示例 1: 评测InternLM2.5在MMLU和CMMLU上的表现

```bash
opencompass run --models hf_internlm2_5_7b_chat --datasets mmlu_ppl cmmlu_ppl
```

### 示例 2: 多模型全数据集评测对比

```bash
opencompass run --models llama3_8b qwen2_7b --datasets all
```

## 关联命令

- [[lm-eval]]
- [[alpaca-eval]]

## 风险提示

> ⚠️ **LOW**: 评估操作无副作用

## 参考链接

- [https://github.com/open-compass/opencompass](https://github.com/open-compass/opencompass)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
