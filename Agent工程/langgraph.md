---
{
  "cmd_name": "langgraph",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install langgraph",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langchain",
    "crewai"
  ],
  "cmd_tags": [
    "agent",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# langgraph

> LangGraph状态机Agent框架，支持循环、条件分支、持久化、人机协同

## 安装

```bash
pip install langgraph
```

## 用法

```
python app.py (使用langgraph库)
```

## 参数

| Flag | Description |
|------|-------------|
| `StateGraph` | 定义状态图 |
| `add_node` | 添加节点 |
| `add_edge` | 添加边 |
| `compile` | 编译为可运行应用 |

## 示例

### 示例 1: 定义简单Agent状态图

```bash
python -c "from langgraph.graph import StateGraph; builder = StateGraph(State); builder.add_node('agent', call_model); builder.add_edge('agent', END); graph = builder.compile()"
```

### 示例 2: 带检查点和人机协同的Agent

```bash
python agent_loop.py --checkpoint --interrupt human_approval
```

## 关联命令

- [[langchain]]
- [[crewai]]

## 风险提示

> ⚠️ **MEDIUM**: 循环Agent可能陷入无限循环，需设置最大迭代

## 参考链接

- [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
