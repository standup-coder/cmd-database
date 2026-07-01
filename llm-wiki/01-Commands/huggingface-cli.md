---
{
  "cmd_name": "huggingface-cli",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install huggingface-hub",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "modelscope",
    "git-lfs"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# huggingface-cli

> HuggingFace Hub命令行工具，支持模型/数据集/Space的上传下载管理

## 安装

```bash
pip install huggingface-hub
```

## 用法

```
huggingface-cli [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `download` | 下载模型或数据集 |
| `upload` | 上传文件到Hub |
| `repo create` | 创建新仓库 |
| `scan-cache` | 扫描本地缓存 |
| `delete-cache` | 删除本地缓存 |

## 示例

### 示例 1: 下载LLaMA-3.1模型到本地缓存

```bash
huggingface-cli download meta-llama/Llama-3.1-8B-Instruct
```

### 示例 2: 下载模型到指定目录

```bash
huggingface-cli download --local-dir ./models Qwen/Qwen2-7B-Instruct
```

### 示例 3: 创建新模型仓库

```bash
huggingface-cli repo create my-awesome-model --type model
```

### 示例 4: 查看本地缓存占用详情

```bash
huggingface-cli scan-cache --verbose
```

## 关联命令

- [[modelscope]]
- [[git-lfs]]

## 风险提示

> ⚠️ **LOW**: 下载操作无副作用，上传需确认权限

## 参考链接

- [https://huggingface.co/docs/huggingface_hub](https://huggingface.co/docs/huggingface_hub)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
