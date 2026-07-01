---
{
  "cmd_name": "phidata",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install phidata",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "agno",
    "langchain"
  ],
  "cmd_tags": [
    "agent",
    "multimodal",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# phidata

> Phidata构建AI助手的框架，支持知识库、结构化输出、多模态(已合并为Agno)

## 安装

```bash
pip install phidata
```

## 用法

```
python app.py (使用phidata库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Assistant` | 创建AI助手 |
| `KnowledgeBase` | 知识库 |

## 示例

### 示例 1: 带知识库的AI助手

```bash
python assistant.py --model gpt-4 --knowledge ./docs --storage postgres
```

### 示例 2: 使用 PostgreSQL 存储和 Claude 模型

```bash
python assistant.py --storage postgres --model claude-3-sonnet
```

## 关联命令

- [[agno]]
- [[langchain]]

## 风险提示

> ⚠️ **LOW**: 框架抽象降低风险

## 参考链接

- [https://docs.phidata.com/](https://docs.phidata.com/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
