---
cmd_name: crewai
cmd_category: AI基础设施/Agent工程
cmd_dimension: Agent工程
cmd_install: pip install crewai
cmd_platforms:
- linux
- darwin
- windows
summary: "CrewAI多Agent协作框架，角色扮演、任务委派、团队协作执行复杂工作流"
cmd_level: intermediate
cmd_related:
- autogen
- langgraph
cmd_tags:
- agent
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/agent-engineering.yaml
---


# crewai

> CrewAI多Agent协作框架，角色扮演、任务委派、团队协作执行复杂工作流

## 安装

```bash
pip install crewai
```

## 用法

```
python crew.py (使用crewai库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Agent` | 定义Agent角色 |
| `Task` | 定义任务 |
| `Crew` | 组建Agent团队 |
| `Process` | 执行流程 (sequential, hierarchical) |

## 示例

### 示例 1: 多Agent协作撰写博客

```bash
python crew.py --agents researcher,writer,editor --process sequential --goal 'Write a blog post'
```

### 示例 2: 层级管理式Agent团队协作

```bash
python crew.py --process hierarchical --manager gpt-4
```

## 关联命令

- [[autogen]]
- [[langgraph]]

## 风险提示

> ⚠️ **MEDIUM**: 多Agent交互可能产生意外行为

## 参考链接

- [https://www.crewai.com/](https://www.crewai.com/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
