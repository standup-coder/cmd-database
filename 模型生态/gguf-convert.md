---
{
  "cmd_name": "gguf-convert",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install gguf",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "llama.cpp",
    "ollama"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# gguf-convert

> GGUF格式转换工具，将HuggingFace模型转换为llama.cpp兼容格式

## 安装

```bash
pip install gguf
```

## 用法

```
convert_hf_to_gguf.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | HuggingFace模型路径 |
| `--outfile` | 输出GGUF文件路径 |
| `--outtype` | 量化类型 (f32, f16, q4_0, q4_K_M, q5_K_M, q8_0) |

## 示例

### 示例 1: FP16格式转换

```bash
python convert_hf_to_gguf.py --model meta-llama/Llama-3.1-8B --outfile llama-3.1-8b.fp16.gguf --outtype f16
```

### 示例 2: Q4_K_M量化转换(推荐)

```bash
python convert_hf_to_gguf.py --model Qwen/Qwen2-7B --outfile qwen2-7b.Q4_K_M.gguf --outtype q4_K_M
```

## 关联命令

- [[llama.cpp]]
- [[ollama]]

## 风险提示

> ⚠️ **LOW**: 格式转换不改变模型行为

## 参考链接

- [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
