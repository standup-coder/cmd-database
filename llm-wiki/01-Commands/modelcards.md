---
{
  "cmd_name": "modelcards",
  "cmd_category": "AI基础设施/模型架构",
  "cmd_dimension": "模型架构",
  "cmd_install": "pip install modelcards",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "huggingface-cli",
    "transformers-cli"
  ],
  "cmd_tags": [
    "architecture",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-architecture.yaml"
}
---

# modelcards

> HuggingFace Model Card工具，生成和管理模型文档，确保模型可追溯和合规

## 安装

```bash
pip install modelcards
```

## 用法

```
python card.py (使用modelcards库)
```

## 参数

| Flag | Description |
|------|-------------|
| `ModelCard` | 模型卡对象 |
| `save` | 保存模型卡 |
| `validate` | 验证模型卡格式 |

## 示例

### 示例 1: 加载并查看模型卡

```bash
python -c "from modelcards import ModelCard; card = ModelCard.load('meta-llama/Llama-2-7b'); print(card.data)"
```

### 示例 2: 从模板创建模型卡

```bash
python -c "from modelcards import ModelCard; card = ModelCard.from_template(); card.save('README.md')"
```

## 关联命令

- [[huggingface-cli]]
- [[transformers-cli]]

## 风险提示

> ⚠️ **LOW**: 文档工具安全

## 参考链接

- [https://github.com/huggingface/modelcards](https://github.com/huggingface/modelcards)

## 所属维度

[[模型架构-MOC|AI基础设施/模型架构]]
