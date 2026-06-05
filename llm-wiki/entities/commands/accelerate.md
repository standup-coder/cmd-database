---
cmd_name: accelerate
cmd_category: AI基础设施/ML框架
cmd_dimension: ML框架
cmd_install: pip install accelerate
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace Accelerate分布式训练配置工具，简化多GPU/TPU训练"
cmd_level: advanced
cmd_related:
- deepspeed
- torchrun
cmd_tags:
- training
- gpu
- distributed
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ml-frameworks.yaml
---


# accelerate

> HuggingFace Accelerate分布式训练配置工具，简化多GPU/TPU训练

## 安装

```bash
pip install accelerate
```

## 用法

```
accelerate [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `launch` | 启动分布式训练脚本 |
| `config` | 交互式配置分布式训练环境 |
| `estimate-memory` | 估算模型训练所需内存 |
| `test` | 测试分布式环境配置 |

## 示例

### 示例 1: 交互式配置分布式训练参数

```bash
accelerate config
```

### 示例 2: 使用4进程启动分布式训练

```bash
accelerate launch --num_processes=4 train.py
```

### 示例 3: 使用FP16混合精度训练

```bash
accelerate launch --mixed_precision=fp16 train.py
```

## 关联命令

- [[deepspeed]]
- [[torchrun]]

## 风险提示

> ⚠️ **LOW**: 配置不当可能导致训练效率降低

## 参考链接

- [https://huggingface.co/docs/accelerate](https://huggingface.co/docs/accelerate)

## 所属维度

[[ML框架-MOC|AI基础设施/ML框架]]
