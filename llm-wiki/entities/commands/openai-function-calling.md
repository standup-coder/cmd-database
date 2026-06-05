---
cmd_name: openai-function-calling
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install openai
cmd_platforms:
- linux
- darwin
- windows
summary: "OpenAI Function Calling工具调用，让LLM自主决定调用外部API获取实时数据或执行操作"
cmd_level: intermediate
cmd_related:
- instructor
- langchain
cmd_tags:
- inference
- data
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# openai-function-calling

> OpenAI Function Calling工具调用，让LLM自主决定调用外部API获取实时数据或执行操作

## 安装

```bash
pip install openai
```

## 用法

```
python app.py (使用openai库)
```

## 参数

| Flag | Description |
|------|-------------|
| `tools` | 工具定义列表 |
| `tool_choice` | 工具选择策略 (auto, required, none) |
| `function` | 具体函数定义 |

## 示例

### 示例 1: 配置Function Calling

```bash
python -c "import openai; r = client.chat.completions.create(model='gpt-4', messages=[...], tools=[{'type':'function','function':{'name':'get_weather'}}], tool_choice='auto')"
```

### 示例 2: 交互式工具调用对话

```bash
python function_calling.py --tools tools.json --conversation
```

## 关联命令

- [[instructor]]
- [[langchain]]

## 风险提示

> ⚠️ **MEDIUM**: 工具调用可能执行副作用操作，需严格权限控制

## 参考链接

- [https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
