---
{
  "cmd_name": "promptflow",
  "cmd_category": "AI基础设施/AI应用",
  "cmd_dimension": "AI应用",
  "cmd_install": "pip install promptflow",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langchain",
    "dify"
  ],
  "cmd_tags": [
    "deployment",
    "application",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-applications.yaml"
}
---

# promptflow

> 微软PromptFlow Prompt工程与LLM应用开发框架，可视化编排、评估、部署一体化

## 安装

```bash
pip install promptflow
```

## 用法

```
pf [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `flow init` | 初始化工作流 |
| `flow test` | 测试工作流 |
| `run create` | 创建批量运行 |
| `connection create` | 创建连接 |

## 示例

### 示例 1: 初始化聊天机器人工作流

```bash
pf flow init --flow ./my_chatbot --type chat
```

### 示例 2: 测试工作流

```bash
pf flow test --flow ./my_chatbot --inputs question='Hello'
```

### 示例 3: 批量评测工作流

```bash
pf run create --flow ./my_chatbot --data ./data.jsonl --column-mapping question='${data.question}'
```

## 关联命令

- [[langchain]]
- [[dify]]

## 风险提示

> ⚠️ **LOW**: 注意API密钥配置安全

## 参考链接

- [https://microsoft.github.io/promptflow/](https://microsoft.github.io/promptflow/)

## 所属维度

[[AI应用-MOC|AI基础设施/AI应用]]
