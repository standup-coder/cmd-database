---
{
  "cmd_name": "auto-gptq",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install auto-gptq",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "optimum-cli",
    "autoawq"
  ],
  "cmd_tags": [
    "training",
    "deployment",
    "quantization",
    "gpu",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# auto-gptq

> GPTQ后训练量化工具，4-bit量化减少75%显存占用，适合消费级GPU部署

## 安装

```bash
pip install auto-gptq
```

## 用法

```
python quantize.py (使用auto-gptq库)
```

## 参数

| Flag | Description |
|------|-------------|
| `AutoGPTQForCausalLM.from_pretrained` | 加载模型用于量化 |
| `quantize` | 执行量化 |

## 示例

### 示例 1: 4-bit GPTQ量化模型

```bash
python quantize.py --model meta-llama/Llama-2-7b --bits 4 --group_size 128
```

### 示例 2: 大模型GPTQ量化(激活值重排)

```bash
python quantize.py --model Qwen/Qwen2-72B --bits 4 --desc_act
```

## 关联命令

- [[optimum-cli]]
- [[autoawq]]

## 风险提示

> ⚠️ **MEDIUM**: 量化可能降低模型精度，需评估

## 参考链接

- [https://github.com/PanQiWei/AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
