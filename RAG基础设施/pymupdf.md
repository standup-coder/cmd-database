---
{
  "cmd_name": "pymupdf",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install PyMuPDF",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "marker",
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

# pymupdf

> PyMuPDF高性能PDF处理库，提取文本/图像/注释，支持PDF编辑和转换

## 安装

```bash
pip install PyMuPDF
```

## 用法

```
python extract.py (使用fitz库)
```

## 参数

| Flag | Description |
|------|-------------|
| `fitz.open()` | 打开PDF |
| `page.get_text()` | 提取页面文本 |
| `page.get_images()` | 提取页面图像 |

## 示例

### 示例 1: 提取首页文本

```bash
python -c "import fitz; doc = fitz.open('file.pdf'); print(doc[0].get_text())"
```

### 示例 2: PDF页面转图片

```bash
python -c "import fitz; doc = fitz.open('file.pdf'); pix = doc[0].get_pixmap(); pix.save('page1.png')"
```

## 关联命令

- [[marker]]
- [[unstructured]]

## 风险提示

> ⚠️ **LOW**: 本地处理安全

## 参考链接

- [https://github.com/pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
