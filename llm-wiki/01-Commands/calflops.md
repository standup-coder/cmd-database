---
{
  "cmd_name": "calflops",
  "cmd_category": "AI基础设施/模型架构",
  "cmd_dimension": "模型架构",
  "cmd_install": "pip install calflops",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "transformers-cli",
    "deepspeed"
  ],
  "cmd_tags": [
    "architecture",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-architecture.yaml"
}
---

# calflops

> CalFlops模型参数量与FLOPs计算工具，精确统计前向/反向传播计算量

## 安装

```bash
pip install calflops
```

## 用法

```
python calculate.py (使用calflops库)
```

## 参数

| Flag | Description |
|------|-------------|
| `calculate_flops` | 计算FLOPs |
| `calculate_params` | 计算参数量 |

## 示例

### 示例 1: 计算模型FLOPs和参数量

```bash
python -c "from calflops import calculate_flops; flops, macs, params = calculate_flops(model=model, input_shape=(1,3,224,224))"
```

### 示例 2: LLaMA模型推理计算量分析

```bash
python profile.py --model llama-7b --seq_len 2048 --batch_size 1
```

## 关联命令

- [[transformers-cli]]
- [[deepspeed]]

## 风险提示

> ⚠️ **LOW**: 分析工具安全

## 参考链接

- [https://github.com/MrYxJ/calculate-flops](https://github.com/MrYxJ/calculate-flops)

## 所属维度

[[模型架构-MOC|AI基础设施/模型架构]]
