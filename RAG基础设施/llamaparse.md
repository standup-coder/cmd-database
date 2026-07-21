---
{
  "cmd_name": "llamaparse",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install llama-parse",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "unstructured",
    "docling"
  ],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/rag-infra.yaml"
}
---

# llamaparse

> LlamaParse LlamaIndex高级PDF解析服务，GenAI原生解析，支持表格、图表、数学公式

## 安装

```bash
pip install llama-parse
```

## 用法

```
python extract.py (使用llama_parse库)
```

## 参数

| Flag | Description |
|------|-------------|
| `LlamaParse` | 解析器类 |
| `result_type` | 输出格式 (markdown, text) |
| `verbose` | 详细输出 |

## 示例

### 示例 1: PDF转Markdown

```bash
python -c "from llama_parse import LlamaParse; parser = LlamaParse(result_type='markdown'); docs = parser.load_data('paper.pdf')"
```

### 示例 2: 查看 PDF 加载 API

```bash
python -c "from llama_parse import LlamaParse; help(LlamaParse.load_data)"
```

## 关联命令

- [[unstructured]]
- [[docling]]

## 风险提示

> ⚠️ **LOW**: 云端API解析注意隐私

## 参考链接

- [https://docs.cloud.llamaindex.ai/](https://docs.cloud.llamaindex.ai/)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
