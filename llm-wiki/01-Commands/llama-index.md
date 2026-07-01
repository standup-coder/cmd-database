---
{
  "cmd_name": "llama-index",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install llama-index",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langchain",
    "haystack"
  ],
  "cmd_tags": [
    "agent",
    "rag",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# llama-index

> LlamaIndex数据框架，连接LLM与私有数据，支持RAG、Agent、工作流

## 安装

```bash
pip install llama-index
```

## 用法

```
python app.py (使用llama_index库)
```

## 参数

| Flag | Description |
|------|-------------|
| `VectorStoreIndex` | 向量存储索引 |
| `QueryEngine` | 查询引擎 |
| `AgentRunner` | Agent运行器 |
| `Workflow` | 事件驱动工作流 |

## 示例

### 示例 1: 从文档构建索引

```bash
python -c "from llama_index import VectorStoreIndex, SimpleDirectoryReader; docs = SimpleDirectoryReader('data').load_data(); index = VectorStoreIndex.from_documents(docs)"
```

### 示例 2: 事件驱动Agent工作流

```bash
python agent.py --index ./index --tools slack,notion --workflow event_driven
```

## 关联命令

- [[langchain]]
- [[haystack]]

## 风险提示

> ⚠️ **MEDIUM**: 外部工具集成注意权限

## 参考链接

- [https://www.llamaindex.ai/](https://www.llamaindex.ai/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
