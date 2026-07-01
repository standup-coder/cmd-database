---
{
  "cmd_name": "agno",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install agno",
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
    "multimodal",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# agno

> Agno (原Phidata) 轻量级Agent框架，支持记忆、知识库、工具、多模态

## 安装

```bash
pip install agno
```

## 用法

```
python app.py (使用agno库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Agent` | 创建Agent |
| `KnowledgeBase` | 知识库 |
| `Storage` | 持久化存储 |

## 示例

### 示例 1: 创建简单Agent

```bash
python -c "from agno.agent import Agent; agent = Agent(model=OpenAIChat('gpt-4')); agent.print_response('Hello')"
```

### 示例 2: 带知识库和记忆的Agent

```bash
python agent.py --knowledge ./docs --memory sqlite --tools search,calculator
```

## 关联命令

- [[langchain]]
- [[crewai]]

## 风险提示

> ⚠️ **MEDIUM**: Agent工具调用需谨慎

## 参考链接

- [https://docs.agno.com/](https://docs.agno.com/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
