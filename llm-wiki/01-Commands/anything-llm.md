---
{
  "cmd_name": "anything-llm",
  "cmd_category": "AI基础设施/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/Mintplex-Labs/anything-llm/blob/master/BARE_METAL.md",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ollama",
    "docling"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-extra.yaml"
}
---

# anything-llm

> 本地/私有化知识库与 LLM 对话平台

## 安装

```bash
参考 https://github.com/Mintplex-Labs/anything-llm/blob/master/BARE_METAL.md
```

## 用法

```
anything-llm [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 启动服务 |
| `setup` | 初始化 |

## 示例

### 示例 1: 启动 AnythingLLM

```bash
yarn anything-llm start
```

### 示例 2: Docker 启动

```bash
docker pull mintplexlabs/anythingllm && docker run -d -p 3001:3001 mintplexlabs/anythingllm
```

## 关联命令

- [[ollama]]
- [[docling]]

## 风险提示

> ⚠️ **MEDIUM**: 上传文档可能包含敏感信息，请做好访问控制和数据隔离

## 所属维度

[[扩展工具-MOC|AI基础设施/扩展工具]]
