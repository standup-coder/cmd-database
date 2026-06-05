---
cmd_name: ollama
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: curl -fsSL https://ollama.com/install.sh | sh
cmd_platforms:
- linux
- darwin
- windows
summary: "Ollama本地大模型运行管理工具，一键下载和运行各类开源模型"
cmd_level: intermediate
cmd_related:
- llama.cpp
- vllm
cmd_tags:
- inference
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# ollama

> Ollama本地大模型运行管理工具，一键下载和运行各类开源模型

## 安装

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 用法

```
ollama [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行模型 |
| `pull` | 下载模型 |
| `list` | 列出本地模型 |
| `serve` | 启动API服务 |
| `create` | 从Modelfile创建模型 |

## 示例

### 示例 1: 下载并运行LLaMA-3.1模型

```bash
ollama run llama3.1
```

### 示例 2: 运行Qwen2-72B模型

```bash
ollama run qwen2:72b
```

### 示例 3: 启动Ollama API服务(默认端口11434)

```bash
ollama serve
```

### 示例 4: 使用Modelfile创建自定义模型

```bash
ollama create my-model -f Modelfile
```

## 关联命令

- [[llama.cpp]]
- [[vllm]]

## 风险提示

> ⚠️ **LOW**: 本地运行，风险可控

## 参考链接

- [https://ollama.com/](https://ollama.com/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
