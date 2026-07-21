---
{
  "cmd_name": "opik",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install opik",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "phoenix",
    "langsmith"
  ],
  "cmd_tags": [
    "monitoring",
    "rag",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# opik

> Comet Opik开源LLM评估与追踪平台，支持RAG评估、提示工程、实验管理

## 安装

```bash
pip install opik
```

## 用法

```
opik [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `configure` | 配置Opik |
| `--server` | 自托管模式启动 |

## 示例

### 示例 1: 配置Opik连接

```bash
opik configure
```

### 示例 2: 配置本地模式

```bash
python -c "import opik; opik.configure(use_local=True)"
```

## 关联命令

- [[phoenix]]
- [[langsmith]]

## 风险提示

> ⚠️ **LOW**: 可自托管，数据安全

## 参考链接

- [https://www.comet.com/site/products/opik/](https://www.comet.com/site/products/opik/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
