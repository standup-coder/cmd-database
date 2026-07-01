---
{
  "cmd_name": "marker",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install marker-pdf",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pymupdf",
    "unstructured"
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

# marker

> Marker高性能PDF转Markdown工具，基于布局模型，准确提取表格、公式、代码块

## 安装

```bash
pip install marker-pdf
```

## 用法

```
marker [OPTIONS] INPUT_DIR OUTPUT_DIR
```

## 参数

| Flag | Description |
|------|-------------|
| `--workers` | 并行工作进程数 |
| `--max_pages` | 最大处理页数 |
| `--langs` | 语言列表 |

## 示例

### 示例 1: 4进程批量转换PDF

```bash
marker ./pdfs ./markdown --workers 4
```

### 示例 2: 指定语言转换

```bash
marker single paper.pdf ./output --langs English,Chinese
```

## 关联命令

- [[pymupdf]]
- [[unstructured]]

## 风险提示

> ⚠️ **LOW**: 本地处理安全

## 参考链接

- [https://github.com/VikParuchuri/marker](https://github.com/VikParuchuri/marker)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
