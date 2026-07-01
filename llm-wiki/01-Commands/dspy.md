---
{
  "cmd_name": "dspy",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install dspy",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langchain",
    "instructor"
  ],
  "cmd_tags": [
    "agent",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# dspy

> DSPy声明式LLM编程框架，优化提示和权重而非手工工程

## 安装

```bash
pip install dspy
```

## 用法

```
python app.py (使用dspy库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Signature` | 定义输入输出签名 |
| `Module` | 构建可组合模块 |
| `BootstrapFewShot` | 少样本示例引导 |
| `MIPRO` | 自动提示优化 |

## 示例

### 示例 1: 基础DSPy预测

```bash
python -c "import dspy; lm = dspy.LM('openai/gpt-4'); dspy.configure(lm=lm); pred = dspy.Predict('question -> answer'); print(pred(question='Why is the sky blue?'))"
```

### 示例 2: MIPRO自动优化提示

```bash
python optimize.py --optimizer MIPRO --metric accuracy --trainset train.json
```

## 关联命令

- [[langchain]]
- [[instructor]]

## 风险提示

> ⚠️ **LOW**: 框架抽象降低风险

## 参考链接

- [https://dspy.ai/](https://dspy.ai/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
