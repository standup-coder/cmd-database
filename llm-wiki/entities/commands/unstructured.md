---
cmd_name: unstructured
cmd_category: AI基础设施/RAG基础设施
cmd_dimension: RAG基础设施
cmd_install: pip install unstructured[all-docs]
cmd_platforms:
- linux
- darwin
- windows
summary: "Unstructured通用文档解析库，支持PDF/Word/PPT/HTML/图片等50+格式提取文本"
cmd_level: intermediate
cmd_related:
- llamaparse
- marker
cmd_tags:
- rag
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/rag-infra.yaml
---


# unstructured

> Unstructured通用文档解析库，支持PDF/Word/PPT/HTML/图片等50+格式提取文本

## 安装

```bash
pip install unstructured[all-docs]
```

## 用法

```
python extract.py (使用unstructured库)
```

## 参数

| Flag | Description |
|------|-------------|
| `partition` | 智能文档分块 |
| `partition_pdf` | PDF专用解析 |
| `partition_html` | HTML解析 |

## 示例

### 示例 1: 提取PDF文本和表格

```bash
python -c "from unstructured.partition.pdf import partition_pdf; elements = partition_pdf('doc.pdf')"
```

### 示例 2: 自动识别格式并解析

```bash
python -c "from unstructured.partition.auto import partition; elements = partition('report.docx')"
```

## 关联命令

- [[llamaparse]]
- [[marker]]

## 风险提示

> ⚠️ **LOW**: 只读解析

## 参考链接

- [https://unstructured.io/](https://unstructured.io/)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
