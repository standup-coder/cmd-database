---
{
  "cmd_name": "phoenix",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install arize-phoenix",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langfuse",
    "arize"
  ],
  "cmd_tags": [
    "monitoring",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# phoenix

> Arize Phoenix开源LLM可观测性和评估工具，支持追踪、评估、数据集管理

## 安装

```bash
pip install arize-phoenix
```

## 用法

```
phoenix server [OPTIONS]
```

```
python app.py (使用phoenix库)
```

## 参数

| Flag | Description |
|------|-------------|
| `server` | 启动Phoenix服务 |
| `--port` | 服务端口号 |
| `--host` | 绑定主机 |

## 示例

### 示例 1: 启动Phoenix UI服务

```bash
phoenix server --port 6006
```

### 示例 2: Python内嵌启动Phoenix

```bash
python -c "import phoenix as px; px.launch_app()"
```

## 关联命令

- [[langfuse]]
- [[arize]]

## 风险提示

> ⚠️ **LOW**: 开源可自托管

## 参考链接

- [https://github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
