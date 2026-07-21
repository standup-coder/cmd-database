---
{
  "cmd_name": "autoawq",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install autoawq",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "auto-gptq",
    "optimum-cli"
  ],
  "cmd_tags": [
    "inference",
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# autoawq

> AWQ激活感知的权重量化，4-bit量化精度优于GPTQ，推理速度提升3倍

## 安装

```bash
pip install autoawq
```

## 用法

```
python quantize.py (使用autoawq库)
```

## 参数

| Flag | Description |
|------|-------------|
| `AutoAWQForCausalLM.from_quantized` | 加载已量化模型 |
| `quantize` | 执行AWQ量化 |

## 示例

### 示例 1: AWQ 4-bit量化模型

```bash
python awq_quantize.py --model_path meta-llama/Llama-2-7b --w_bit 4 --q_group_size 128
```

### 示例 2: 查看量化加载 API

```bash
python -c "from awq import AutoAWQForCausalLM; help(AutoAWQForCausalLM.from_quantized)"
```

## 关联命令

- [[auto-gptq]]
- [[optimum-cli]]

## 风险提示

> ⚠️ **MEDIUM**: 量化可能降低模型精度

## 参考链接

- [https://github.com/casper-hansen/AutoAWQ](https://github.com/casper-hansen/AutoAWQ)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
