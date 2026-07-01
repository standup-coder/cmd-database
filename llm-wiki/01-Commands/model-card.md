---
{
  "cmd_name": "model-card",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "huggingface-cli",
    "modelscope"
  ],
  "cmd_tags": [
    "training",
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# model-card

> 模型卡片(model card)编写规范，记录模型用途、限制、训练数据等元信息

## 用法

```
创建 README.md 或 model_card.md 文件
```

## 参数

| Flag | Description |
|------|-------------|
| `model_details` | 模型架构、版本、训练数据 |
| `intended_use` | 预期用途和限制 |
| `ethical_considerations` | 伦理考量和风险 |
| `evaluation` | 评估指标和结果 |

## 示例

### 示例 1: 创建带模型卡片的仓库

```bash
huggingface-cli repo create my-model --type model && echo '# Model Card' > README.md
```

### 示例 2: 上传模型文件到 Hub

```bash
huggingface-cli upload my-model ./model README.md
```

## 关联命令

- [[huggingface-cli]]
- [[modelscope]]

## 风险提示

> ⚠️ **LOW**: 文档编写无技术风险

## 参考链接

- [https://huggingface.co/docs/hub/model-cards](https://huggingface.co/docs/hub/model-cards)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
