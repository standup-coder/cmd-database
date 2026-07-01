---
{
  "cmd_name": "langfuse",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install langfuse",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langsmith",
    "promptlayer"
  ],
  "cmd_tags": [
    "monitoring",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# langfuse

> Langfuse开源LLM可观测性平台，支持自托管，追踪成本、延迟、质量指标

## 安装

```bash
pip install langfuse
```

## 用法

```
docker compose up (自托管)
```

```
python app.py (使用langfuse库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Langfuse` | 初始化追踪客户端 |
| `trace` | 创建追踪会话 |
| `span` | 记录调用跨度 |

## 示例

### 示例 1: Docker自托管Langfuse

```bash
git clone https://github.com/langfuse/langfuse.git && cd langfuse && docker compose up
```

### 示例 2: 连接自托管Langfuse

```bash
python app.py --langfuse_host http://localhost:3000 --public_key pk-xxx --secret_key sk-xxx
```

## 关联命令

- [[langsmith]]
- [[promptlayer]]

## 风险提示

> ⚠️ **LOW**: 自托管数据安全可控

## 参考链接

- [https://langfuse.com/](https://langfuse.com/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
