---
{
  "cmd_name": "n8n",
  "cmd_category": "AI基础设施/AI应用",
  "cmd_dimension": "AI应用",
  "cmd_install": "npm install -g n8n",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dify",
    "flowise"
  ],
  "cmd_tags": [
    "application",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-applications.yaml"
}
---

# n8n

> n8n开源AI工作流自动化平台，低代码编排LLM、数据库、API、通知等节点

## 安装

```bash
npm install -g n8n
```

## 用法

```
n8n [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 启动服务 |
| `webhook` | 测试Webhook |
| `execute` | 执行工作流 |
| `--tunnel` | 启用隧道 |

## 示例

### 示例 1: 启动n8n服务

```bash
n8n start
```

### 示例 2: 测试Webhook

```bash
n8n webhook --url http://localhost:5678/webhook/xxx
```

### 示例 3: 执行工作流文件

```bash
n8n execute --file workflow.json
```

## 关联命令

- [[dify]]
- [[flowise]]

## 风险提示

> ⚠️ **MEDIUM**: 工作流执行权限需管控

## 参考链接

- [https://n8n.io/](https://n8n.io/)

## 所属维度

[[AI应用-MOC|AI基础设施/AI应用]]
