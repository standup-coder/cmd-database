---
{
  "cmd_name": "praisonai",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install praisonai",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "crewai",
    "autogen"
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

# praisonai

> PraisonAI低代码多Agent框架，基于CrewAI，支持AutoGen集成和UI界面

## 安装

```bash
pip install praisonai
```

## 用法

```
praisonai [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化项目 |
| `agents` | 生成Agent配置 |
| `chain` | 链式调用 |
| `chat` | 交互式对话 |

## 示例

### 示例 1: 初始化PraisonAI项目

```bash
praisonai init
```

### 示例 2: 生成3个研究Agent配置

```bash
praisonai agents --topic 'AI Research' --agents 3
```

### 示例 3: 交互式多Agent对话

```bash
praisonai chat --agents agents.yaml
```

## 关联命令

- [[crewai]]
- [[autogen]]

## 风险提示

> ⚠️ **MEDIUM**: 多Agent交互风险

## 参考链接

- [https://docs.praison.ai/](https://docs.praison.ai/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
