---
{
  "cmd_name": "modelscope",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install modelscope",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "huggingface-cli",
    "git-lfs"
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

# modelscope

> 魔搭社区ModelScope命令行工具，国产开源模型仓库管理

## 安装

```bash
pip install modelscope
```

## 用法

```
modelscope [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `download` | 下载模型或数据集 |
| `upload` | 上传模型到ModelScope |
| `login` | 登录ModelScope账号 |

## 示例

### 示例 1: 下载Qwen2模型

```bash
modelscope download --model qwen/Qwen2-7B-Instruct
```

### 示例 2: 下载到指定目录

```bash
modelscope download --model damo/cv_resnet --local_dir ./models
```

## 关联命令

- [[huggingface-cli]]
- [[git-lfs]]

## 风险提示

> ⚠️ **LOW**: 下载操作无副作用

## 参考链接

- [https://www.modelscope.cn/](https://www.modelscope.cn/)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
