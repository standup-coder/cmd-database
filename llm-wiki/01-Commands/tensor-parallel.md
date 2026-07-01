---
{
  "cmd_name": "tensor-parallel",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install tensor_parallel",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "vllm",
    "deepspeed"
  ],
  "cmd_tags": [
    "inference",
    "distributed",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# tensor-parallel

> Tensor Parallel通用张量并行推理库，支持任意HuggingFace模型多卡推理

## 安装

```bash
pip install tensor_parallel
```

## 用法

```
python inference.py (使用tensor_parallel库)
```

## 参数

| Flag | Description |
|------|-------------|
| `tensor_parallel.TensorParallelPreTrainedModel` | 包装模型为张量并行 |
| `tensor_parallel_config` | 并行配置 |

## 示例

### 示例 1: 4卡张量并行包装模型

```bash
python -c "import tensor_parallel as tp; model = tp.TensorParallelPreTrainedModel(model, device_ids=[0,1,2,3])"
```

### 示例 2: 查看张量并行 API 帮助

```bash
python -c "import tensor_parallel as tp; help(tp.TensorParallelPreTrainedModel)"
```

## 关联命令

- [[vllm]]
- [[deepspeed]]

## 风险提示

> ⚠️ **MEDIUM**: 多卡并行需合理配置

## 参考链接

- [https://github.com/BlackSamorez/tensor_parallel](https://github.com/BlackSamorez/tensor_parallel)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
