---
{
  "cmd_name": "mergekit",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install mergekit",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "safetensors-convert",
    "huggingface-cli"
  ],
  "cmd_tags": [
    "training",
    "gpu",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# mergekit

> MergeKit模型合并工具，支持SLERP、TIES、DARE、Model Stock等多种合并算法，无需GPU

## 安装

```bash
pip install mergekit
```

## 用法

```
mergekit-yaml [CONFIG] [OUTPUT_PATH]
```

## 参数

| Flag | Description |
|------|-------------|
| `--lazy-unpickle` | 懒加载模型权重 |
| `--low-cpu-memory` | 低内存模式 |
| `--copy-tokenizer` | 复制tokenizer |

## 示例

### 示例 1: 按配置合并模型

```bash
mergekit-yaml merge_config.yaml ./merged_model --lazy-unpickle
```

### 示例 2: 从标准输入读取配置

```bash
cat merge_config.yaml | mergekit-yaml - ./output
```

## 关联命令

- [[safetensors-convert]]
- [[huggingface-cli]]

## 风险提示

> ⚠️ **LOW**: 合并操作只读加载模型

## 参考链接

- [https://github.com/arcee-ai/mergekit](https://github.com/arcee-ai/mergekit)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
