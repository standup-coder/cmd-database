---
{
  "cmd_name": "embedchain",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install embedchain",
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
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# embedchain

> EmbedChain RAG框架，简化数据加载、分块、嵌入、查询全流程

## 安装

```bash
pip install embedchain
```

## 用法

```
python app.py (使用embedchain库)
```

## 参数

| Flag | Description |
|------|-------------|
| `App` | 创建RAG应用 |
| `add` | 添加数据源 |
| `query` | 查询 |

## 示例

### 示例 1: 从URL构建RAG

```bash
python -c "from embedchain import App; app = App(); app.add('https://example.com'); print(app.query('What is this?'))"
```

### 示例 2: 多源RAG应用

```bash
python app.py --add youtube,notion,slack --query 'Summarize'
```

## 关联命令

- [[langchain]]
- [[llama-index]]

## 风险提示

> ⚠️ **LOW**: RAG应用风险较低

## 参考链接

- [https://docs.embedchain.ai/](https://docs.embedchain.ai/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
