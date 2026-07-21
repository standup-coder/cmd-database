---
{
  "cmd_name": "pydantic-ai",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install pydantic-ai",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "instructor",
    "langchain"
  ],
  "cmd_tags": [
    "safety",
    "agent",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# pydantic-ai

> PydanticAI类型安全Agent框架，Samuel Colvin(Pydantic作者)出品，强类型验证

## 安装

```bash
pip install pydantic-ai
```

## 用法

```
python app.py (使用pydantic_ai库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Agent` | 创建类型安全Agent |
| `RunContext` | 运行上下文 |
| `result_type` | 结果类型约束 |

## 示例

### 示例 1: 类型安全Agent调用

```bash
python -c "from pydantic_ai import Agent; agent = Agent('openai:gpt-4', result_type=CityInfo); result = agent.run_sync('Tell me about Paris')"
```

### 示例 2: 查看同步运行 API

```bash
python -c "from pydantic_ai import Agent; help(Agent.run_sync)"
```

## 关联命令

- [[instructor]]
- [[langchain]]

## 风险提示

> ⚠️ **LOW**: 强类型约束降低风险

## 参考链接

- [https://ai.pydantic.dev/](https://ai.pydantic.dev/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
