---
{
  "cmd_name": "mlc-llm",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install mlc-llm-nightly",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "llama.cpp",
    "gguf-convert"
  ],
  "cmd_tags": [
    "deployment",
    "edge",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# mlc-llm

> MLC LLM全平台大模型部署，支持手机/浏览器/边缘设备/云端

## 安装

```bash
pip install mlc-llm-nightly
```

## 用法

```
mlc_llm [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `convert_build` | 编译模型 |
| `chat` | 本地聊天 |
| `serve` | 启动REST服务 |

## 示例

### 示例 1: 编译4-bit量化模型

```bash
mlc_llm convert_build ./dist/Llama-3-8B/ --quantization q4f16_1
```

### 示例 2: 本地交互式聊天

```bash
mlc_llm chat ./dist/Llama-3-8B-q4f16_1
```

## 关联命令

- [[llamacpp]]
- [[gguf-convert]]

## 风险提示

> ⚠️ **LOW**: 编译过程安全

## 参考链接

- [https://llm.mlc.ai/](https://llm.mlc.ai/)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
