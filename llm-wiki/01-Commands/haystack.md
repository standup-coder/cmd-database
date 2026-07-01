---
{
  "cmd_name": "haystack",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install haystack-ai",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langchain",
    "llama-index"
  ],
  "cmd_tags": [
    "agent",
    "rag",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# haystack

> Haystack端到端NLP框架，支持RAG、Agent、文档搜索、Pipeline编排

## 安装

```bash
pip install haystack-ai
```

## 用法

```
python app.py (使用haystack库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Pipeline` | 构建处理管道 |
| `DocumentStore` | 文档存储 |
| `Agent` | Haystack Agent |

## 示例

### 示例 1: 构建RAG Pipeline

```bash
python -c "from haystack import Pipeline; pipe = Pipeline(); pipe.add_component('retriever', retriever); pipe.add_component('generator', generator); pipe.connect('retriever', 'generator')"
```

### 示例 2: 文档问答Agent

```bash
python agent.py --tools search,qa --document_store elasticsearch
```

## 关联命令

- [[langchain]]
- [[llama-index]]

## 风险提示

> ⚠️ **MEDIUM**: Pipeline组件配置需验证

## 参考链接

- [https://haystack.deepset.ai/](https://haystack.deepset.ai/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
