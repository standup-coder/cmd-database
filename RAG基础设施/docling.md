---
{
  "cmd_name": "docling",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install docling",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "unstructured",
    "marker"
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

# docling

> IBM Docling开源文档解析，支持PDF/HTML/图片/PPT，保留文档结构生成Markdown

## 安装

```bash
pip install docling
```

## 用法

```
python extract.py (使用docling库)
```

## 参数

| Flag | Description |
|------|-------------|
| `DocumentConverter` | 文档转换器 |
| `export_to_markdown` | 导出Markdown |

## 示例

### 示例 1: PDF转结构化Markdown

```bash
python -c "from docling.document_converter import DocumentConverter; c = DocumentConverter(); r = c.convert('paper.pdf'); print(r.document.export_to_markdown())"
```

### 示例 2: 查看文档转换 API

```bash
python -c "from docling.document_converter import DocumentConverter; help(DocumentConverter.convert)"
```

## 关联命令

- [[unstructured]]
- [[marker]]

## 风险提示

> ⚠️ **LOW**: 本地解析安全

## 参考链接

- [https://github.com/DS4SD/docling](https://github.com/DS4SD/docling)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
