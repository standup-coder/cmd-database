---
{
  "cmd_name": "mcp",
  "cmd_category": "AI基础设施/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://modelcontextprotocol.io/quickstart",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openai-agents",
    "langchain"
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

# mcp

> Model Context Protocol CLI/服务器

## 安装

```bash
参考 https://modelcontextprotocol.io/quickstart
```

## 用法

```
mcp [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化 |
| `run` | 运行服务器 |
| `inspect` | 检查 |

## 示例

### 示例 1: 运行官方示例 MCP 服务器

```bash
npx @anthropics/mcp-server-puppeteer
```

### 示例 2: 运行 SQLite MCP 服务器

```bash
uvx mcp-server-sqlite --db path/to/db.sqlite
```

## 关联命令

- [[openai-agents]]
- [[langchain]]

## 风险提示

> ⚠️ **MEDIUM**: MCP 服务器可能拥有文件/网络访问权限，请审查权限并隔离运行

## 所属维度

[[扩展工具-MOC|AI基础设施/扩展工具]]
