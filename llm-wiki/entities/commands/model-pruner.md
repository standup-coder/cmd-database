---
cmd_name: model-pruner
cmd_category: AI基础设施/模型生态
cmd_dimension: 模型生态
cmd_install: pip install torch-pruning
cmd_platforms:
- linux
- darwin
- windows
summary: "模型剪枝工具，移除不重要的权重或神经元，减小模型体积加速推理"
cmd_level: advanced
cmd_related:
- optimum-cli
- auto-gptq
cmd_tags:
- inference
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/model-hub.yaml
---


# model-pruner

> 模型剪枝工具，移除不重要的权重或神经元，减小模型体积加速推理

## 安装

```bash
pip install torch-pruning
```

## 用法

```
python prune.py (使用torch-pruning库)
```

## 参数

| Flag | Description |
|------|-------------|
| `prune` | 执行剪枝操作 |
| `importance` | 重要性评估方法 (magnitude, taylor, random) |
| `sparsity` | 目标稀疏率 |

## 示例

### 示例 1: 50%幅值剪枝

```bash
python prune.py --model resnet50 --sparsity 0.5 --importance magnitude
```

### 示例 2: 30%泰勒重要性剪枝

```bash
python prune.py --model vit-base --sparsity 0.3 --importance taylor
```

## 关联命令

- [[optimum-cli]]
- [[auto-gptq]]

## 风险提示

> ⚠️ **HIGH**: 剪枝可能显著降低模型精度，需充分评估

## 参考链接

- [https://github.com/VainF/Torch-Pruning](https://github.com/VainF/Torch-Pruning)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]
