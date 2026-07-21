---
{
  "cmd_name": "open-webui",
  "cmd_category": "AI基础设施/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "pip install open-webui 或 Docker 运行",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ollama",
    "llama.cpp"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-extra.yaml"
}
---

# open-webui

> 本地大模型 Web 聊天界面

## 安装

```bash
pip install open-webui 或 Docker 运行
```

## 用法

```
open-webui [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `serve` | 启动服务 |
| `--port` |  |
| `--host` |  |

## 示例

### 示例 1: 启动 Open WebUI 服务

```bash
open-webui serve
```

### 示例 2: Docker 启动并挂载 Ollama

```bash
docker run -d -p 3000:8080 --gpus all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

## 关联命令

- [[ollama]]
- [[llamacpp]]

## 风险提示

> ⚠️ **MEDIUM**: WebUI 会暴露模型接口，请配置认证和网络访问控制

## 所属维度

[[扩展工具-MOC|AI基础设施/扩展工具]]
