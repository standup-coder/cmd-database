---
cmd_name: openai-agents
cmd_category: AI基础设施/Agent工程
cmd_dimension: Agent工程
cmd_install: pip install openai-agents
cmd_platforms:
- linux
- darwin
- windows
summary: "OpenAI官方Agents SDK，支持Responses API、工具调用、网络搜索、文件搜索"
cmd_level: intermediate
cmd_related:
- langchain
- autogen
cmd_tags:
- agent
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/agent-engineering.yaml
---


# openai-agents

> OpenAI官方Agents SDK，支持Responses API、工具调用、网络搜索、文件搜索

## 安装

```bash
pip install openai-agents
```

## 用法

```
python app.py (使用openai-agents库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Agent` | 创建Agent |
| `function_tool` | 注册函数工具 |
| `Runner.run` | 运行Agent |

## 示例

### 示例 1: 运行OpenAI Agent

```bash
python -c "from agents import Agent, Runner; agent = Agent(name='Assistant', instructions='Helpful'); result = Runner.run_sync(agent, 'Hello')"
```

### 示例 2: 带搜索工具的Agent

```bash
python agent.py --tools web_search,file_search --model gpt-4o
```

## 关联命令

- [[langchain]]
- [[autogen]]

## 风险提示

> ⚠️ **MEDIUM**: 网络搜索可能返回不可信信息

## 参考链接

- [https://github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
