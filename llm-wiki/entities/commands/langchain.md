---
cmd_name: langchain
cmd_category: AI基础设施/Agent工程
cmd_dimension: Agent工程
cmd_install: pip install langchain
cmd_platforms:
- linux
- darwin
- windows
summary: "LangChain LLM应用开发框架，支持Chains、Agents、RAG、工具调用"
cmd_level: intermediate
cmd_related:
- langgraph
- llama-index
cmd_tags:
- agent
- application
- rag
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/agent-engineering.yaml
---


# langchain

> LangChain LLM应用开发框架，支持Chains、Agents、RAG、工具调用

## 安装

```bash
pip install langchain
```

## 用法

```
python app.py (使用langchain库)
```

## 参数

| Flag | Description |
|------|-------------|
| `ChatOpenAI` | 聊天模型封装 |
| `create_react_agent` | 创建ReAct Agent |
| `RunnableParallel` | 并行执行多个Runnable |
| `Chroma` | 向量存储集成 |

## 示例

### 示例 1: 基础LLM调用

```bash
python -c "from langchain import OpenAI; llm = OpenAI(); print(llm.predict('hello'))"
```

### 示例 2: 构建RAG应用

```bash
python rag_app.py --model gpt-4 --vectorstore chroma --documents ./docs
```

### 示例 3: 多工具ReAct Agent

```bash
python agent.py --tools search,calculator --model claude-3
```

## 关联命令

- [[langgraph]]
- [[llama-index]]

## 风险提示

> ⚠️ **MEDIUM**: Agent可能执行不可预期操作，需限制工具权限

## 参考链接

- [https://python.langchain.com/](https://python.langchain.com/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
