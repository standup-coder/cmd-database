---
cmd_name: dify
cmd_category: AI基础设施/Agent工程
cmd_dimension: Agent工程
cmd_install: docker pull langgenius/dify-api
cmd_platforms:
- linux
- darwin
- windows
summary: "Dify开源LLM应用开发平台，可视化编排Agent、RAG、工作流，支持自托管"
cmd_level: intermediate
cmd_related:
- flowise
- langchain
cmd_tags:
- agent
- application
- rag
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/agent-engineering.yaml
---


# dify

> Dify开源LLM应用开发平台，可视化编排Agent、RAG、工作流，支持自托管

## 安装

```bash
docker pull langgenius/dify-api
```

## 用法

```
docker compose up (自托管)
```

## 参数

| Flag | Description |
|------|-------------|
| `--env-file` | 环境变量文件 |

## 示例

### 示例 1: Docker Compose自托管Dify

```bash
git clone https://github.com/langgenius/dify.git && cd dify/docker && docker compose up -d
```

### 示例 2: 含中间件完整部署

```bash
docker compose -f docker-compose.yaml -f docker-compose.middleware.yaml up -d
```

## 关联命令

- [[flowise]]
- [[langchain]]

## 风险提示

> ⚠️ **MEDIUM**: 自托管需配置安全认证

## 参考链接

- [https://dify.ai/](https://dify.ai/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
