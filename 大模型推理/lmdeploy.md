---
{
  "cmd_name": "lmdeploy",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install lmdeploy",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "vllm",
    "sglang"
  ],
  "cmd_tags": [
    "inference",
    "deployment",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# lmdeploy

> 上海AI Lab开源的大模型部署工具，支持TurboMind引擎和PyTorch引擎

## 安装

```bash
pip install lmdeploy
```

## 用法

```
lmdeploy [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `serve` | 启动推理服务 |
| `lite` | 轻量级本地推理 |
| `chat` | 交互式对话 |
| `convert` | 模型格式转换 |

## 示例

### 示例 1: 部署InternLM2.5 API服务

```bash
lmdeploy serve api_server internlm/internlm2_5-7b-chat
```

### 示例 2: AWQ量化模型

```bash
lmdeploy lite auto_awq internlm/internlm2_5-7b-chat --work-dir ./awq_model
```

### 示例 3: 本地交互式对话

```bash
lmdeploy chat internlm/internlm2_5-7b-chat
```

## 关联命令

- [[vllm]]
- [[sglang]]

## 风险提示

> ⚠️ **MEDIUM**: 模型转换后需验证输出一致性

## 参考链接

- [https://github.com/InternLM/lmdeploy](https://github.com/InternLM/lmdeploy)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
