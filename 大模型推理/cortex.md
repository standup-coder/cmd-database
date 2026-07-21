---
{
  "cmd_name": "cortex",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install cortex",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ollama",
    "llama.cpp"
  ],
  "cmd_tags": [
    "inference",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# cortex

> Cortex本地LLM平台，一键运行和管理多种开源模型

## 安装

```bash
pip install cortex
```

## 用法

```
cortex [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行模型 |
| `models` | 模型管理 |
| `pull` | 拉取模型 |

## 示例

### 示例 1: 本地运行LLaMA-3.1

```bash
cortex run llama3.1
```

### 示例 2: 下载Mistral模型

```bash
cortex pull mistral
```

## 关联命令

- [[ollama]]
- [[llamacpp]]

## 风险提示

> ⚠️ **LOW**: 本地运行，风险可控

## 参考链接

- [https://cortex.so/](https://cortex.so/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
