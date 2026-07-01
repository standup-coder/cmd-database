---
{
  "cmd_name": "prefix-caching",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install vllm",
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
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# prefix-caching

> Prefix Caching前缀缓存，复用共享系统Prompt的KV Cache，大幅降低多轮推理延迟和显存

## 安装

```bash
pip install vllm
```

## 用法

```
python -m vllm.entrypoints.openai.api_server [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--enable-prefix-caching` | 启用前缀缓存 |

## 示例

### 示例 1: 启用前缀缓存服务

```bash
python -m vllm.entrypoints.openai.api_server --model llama-3-8b --enable-prefix-caching
```

### 示例 2: 多轮对话前缀缓存加速

```bash
python benchmark.py --enable-prefix-caching --shared-prompt 'You are a helpful assistant' --num-turns 100
```

## 关联命令

- [[vllm]]
- [[sglang]]

## 风险提示

> ⚠️ **LOW**: 缓存优化技术

## 参考链接

- [https://docs.vllm.ai/en/latest/automatic_prefix_caching.html](https://docs.vllm.ai/en/latest/automatic_prefix_caching.html)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
