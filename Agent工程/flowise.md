---
{
  "cmd_name": "flowise",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "npx flowise start",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dify",
    "langchain"
  ],
  "cmd_tags": [
    "agent",
    "application",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# flowise

> Flowise可视化LangChain工作流构建器，拖拽式创建LLM应用

## 安装

```bash
npx flowise start
```

## 用法

```
npx flowise [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 启动Flowise |
| `--PORT` | 端口号 |
| `--FLOWISE_USERNAME` | 用户名 |

## 示例

### 示例 1: 启动Flowise

```bash
npx flowise start
```

### 示例 2: 指定端口和认证启动

```bash
npx flowise start --PORT=3000 --FLOWISE_USERNAME=admin --FLOWISE_PASSWORD=admin
```

## 关联命令

- [[dify]]
- [[langchain]]

## 风险提示

> ⚠️ **MEDIUM**: 生产环境需配置认证

## 参考链接

- [https://flowiseai.com/](https://flowiseai.com/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
