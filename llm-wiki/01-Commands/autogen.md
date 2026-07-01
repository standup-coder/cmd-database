---
{
  "cmd_name": "autogen",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install pyautogen",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "crewai",
    "langgraph"
  ],
  "cmd_tags": [
    "agent",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# autogen

> Microsoft AutoGen多Agent对话框架，支持代码生成、工具调用、人机协同

## 安装

```bash
pip install pyautogen
```

## 用法

```
python app.py (使用autogen库)
```

## 参数

| Flag | Description |
|------|-------------|
| `ConversableAgent` | 可对话Agent |
| `UserProxyAgent` | 用户代理Agent |
| `GroupChat` | 群聊管理 |
| `register_function` | 注册工具函数 |

## 示例

### 示例 1: 代码生成与执行Agent

```bash
python coding_agent.py --agents coder,executor --task 'Build a web scraper'
```

### 示例 2: 创建基础对话Agent

```bash
python -c "from autogen import ConversableAgent; assistant = ConversableAgent('assistant', llm_config={'model':'gpt-4'})"
```

## 关联命令

- [[crewai]]
- [[langgraph]]

## 风险提示

> ⚠️ **HIGH**: 代码执行Agent可能执行危险代码，需沙箱隔离

## 参考链接

- [https://microsoft.github.io/autogen/](https://microsoft.github.io/autogen/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
