---
{
  "cmd_name": "sglang",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install sglang",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "vllm",
    "lmdeploy"
  ],
  "cmd_tags": [
    "inference",
    "multimodal",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# sglang

> SGLang结构化生成语言模型服务，支持RadixAttention缓存、多模态推理

## 安装

```bash
pip install sglang
```

## 用法

```
python -m sglang.launch_server [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model-path` | 模型路径 |
| `--tp-size` | 张量并行大小 |
| `--mem-fraction-static` | 静态内存分配比例 |
| `--enable-torch-compile` | 启用PyTorch编译优化 |

## 示例

### 示例 1: 2卡部署LLaMA-3.1推理服务

```bash
python -m sglang.launch_server --model-path meta-llama/Llama-3.1-8B-Instruct --tp-size 2
```

### 示例 2: 部署Qwen2-VL多模态推理服务

```bash
python -m sglang.launch_server --model-path Qwen/Qwen2-VL-7B-Instruct
```

## 关联命令

- [[vllm]]
- [[lmdeploy]]

## 风险提示

> ⚠️ **MEDIUM**: 推理服务需合理配置并发限制

## 参考链接

- [https://github.com/sgl-project/sglang](https://github.com/sgl-project/sglang)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
