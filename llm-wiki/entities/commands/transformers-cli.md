---
cmd_name: transformers-cli
cmd_category: AI基础设施/模型架构
cmd_dimension: 模型架构
cmd_install: pip install transformers
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace Transformers命令行工具，查看模型配置、下载模型、转换格式"
cmd_level: intermediate
cmd_related:
- huggingface-cli
- safetensors-convert
cmd_tags:
- architecture
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-architecture.yaml
---


# transformers-cli

> HuggingFace Transformers命令行工具，查看模型配置、下载模型、转换格式

## 安装

```bash
pip install transformers
```

## 用法

```
transformers-cli [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `env` | 查看环境信息 |
| `download` | 下载模型 |
| `convert` | 格式转换 |
| `run` | 运行示例脚本 |

## 示例

### 示例 1: 查看Transformers环境配置

```bash
transformers-cli env
```

### 示例 2: 下载LLaMA-2模型

```bash
transformers-cli download meta-llama/Llama-2-7b-hf
```

## 关联命令

- [[huggingface-cli]]
- [[safetensors-convert]]

## 风险提示

> ⚠️ **LOW**: 模型下载占用存储空间

## 参考链接

- [https://huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)

## 所属维度

[[模型架构-MOC|AI基础设施/模型架构]]
