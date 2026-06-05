---
cmd_name: smolagents
cmd_category: AI基础设施/Agent工程
cmd_dimension: Agent工程
cmd_install: pip install smolagents
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace SmolAgents极简Agent库，代码优先，最小抽象，高度透明"
cmd_level: advanced
cmd_related:
- langchain
- autogen
cmd_tags:
- agent
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/agent-engineering.yaml
---


# smolagents

> HuggingFace SmolAgents极简Agent库，代码优先，最小抽象，高度透明

## 安装

```bash
pip install smolagents
```

## 用法

```
python app.py (使用smolagents库)
```

## 参数

| Flag | Description |
|------|-------------|
| `CodeAgent` | 代码执行Agent |
| `ToolCallingAgent` | 工具调用Agent |
| `@tool` | 装饰器注册工具 |

## 示例

### 示例 1: 创建CodeAgent

```bash
python -c "from smolagents import CodeAgent; agent = CodeAgent(tools=[], model=model); agent.run('What is 2+2?')"
```

### 示例 2: 使用开源模型运行Agent

```bash
python agent.py --agent_type code --model_id Qwen/Qwen2.5-Coder-32B-Instruct
```

## 关联命令

- [[langchain]]
- [[autogen]]

## 风险提示

> ⚠️ **HIGH**: CodeAgent执行代码需沙箱隔离

## 参考链接

- [https://github.com/huggingface/smolagents](https://github.com/huggingface/smolagents)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
