---
{
  "cmd_name": "llama.cpp",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "git clone https://github.com/ggerganov/llama.cpp && make",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ollama",
    "gguf-convert"
  ],
  "cmd_tags": [
    "inference",
    "edge",
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# llama.cpp

> llama.cpp纯C/C++实现的LLM推理，支持GGUF量化，可在CPU/边缘设备运行

## 安装

```bash
git clone https://github.com/ggerganov/llama.cpp && make
```

## 用法

```
./main [OPTIONS]
```

```
./server [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-m` | GGUF模型文件路径 |
| `-n` | 生成token数量 |
| `--temp` | 采样温度(默认0.8) |
| `-ngl` | GPU加载的层数 |
| `-c` | 上下文大小 |

## 示例

### 示例 1: CPU推理运行量化模型

```bash
./main -m models/llama-3.1-8b.Q4_K_M.gguf -n 512 --temp 0.7 -p 'What is machine learning?'
```

### 示例 2: 启动HTTP推理服务

```bash
./server -m models/llama-3.1-8b.Q4_K_M.gguf --host 0.0.0.0 --port 8080
```

### 示例 3: GPU卸载35层，8K上下文推理

```bash
./main -m model.gguf -ngl 35 -c 8192
```

## 关联命令

- [[ollama]]
- [[gguf-convert]]

## 风险提示

> ⚠️ **LOW**: 本地推理无网络风险

## 参考链接

- [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
