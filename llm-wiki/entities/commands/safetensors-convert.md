---
cmd_name: safetensors-convert
cmd_category: AI基础设施/模型生态
cmd_dimension: 模型生态
cmd_install: pip install safetensors
cmd_platforms:
- linux
- darwin
- windows
summary: "Safetensors安全模型格式转换工具，替代pickle防止恶意代码执行"
cmd_level: intermediate
cmd_related:
- huggingface-cli
- optimum-cli
cmd_tags:
- safety
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-hub.yaml
---


# safetensors-convert

> Safetensors安全模型格式转换工具，替代pickle防止恶意代码执行

## 安装

```bash
pip install safetensors
```

## 用法

```
python -m safetensors.convert [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--folder` | 包含PyTorch权重的目录 |

## 示例

### 示例 1: 将PyTorch权重转换为Safetensors格式

```bash
python -m safetensors.convert --folder ./pytorch_model
```

### 示例 2: 单个文件转换

```bash
python convert.py --src model.bin --dst model.safetensors
```

## 关联命令

- [[huggingface-cli]]
- [[optimum-cli]]

## 风险提示

> ⚠️ **LOW**: 格式转换不改变模型行为

## 参考链接

- [https://github.com/huggingface/safetensors](https://github.com/huggingface/safetensors)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
