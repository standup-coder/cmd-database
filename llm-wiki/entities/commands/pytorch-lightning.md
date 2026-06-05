---
cmd_name: pytorch-lightning
cmd_category: AI基础设施/ML框架
cmd_dimension: ML框架
cmd_install: pip install pytorch-lightning
cmd_platforms:
- linux
- darwin
- windows
summary: "PyTorch Lightning高级训练框架，简化分布式训练、混合精度、Checkpoint管理"
cmd_level: advanced
cmd_related:
- torchrun
- deepspeed
cmd_tags:
- training
- distributed
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ml-frameworks.yaml
---


# pytorch-lightning

> PyTorch Lightning高级训练框架，简化分布式训练、混合精度、Checkpoint管理

## 安装

```bash
pip install pytorch-lightning
```

## 用法

```
python train.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--devices` | 使用的设备数量，如 '4' 或 'auto' |
| `--accelerator` | 加速器类型 (gpu, cpu, tpu, mps) |
| `--strategy` | 分布式策略 (ddp, deepspeed, fsdp) |
| `--precision` | 精度模式 (16-mixed, bf16-mixed, 32) |

## 示例

### 示例 1: 4卡GPU DDP分布式训练

```bash
python train.py --devices=4 --accelerator=gpu --strategy=ddp
```

### 示例 2: 自动检测GPU并使用DeepSpeed Stage 2

```bash
python train.py --devices=auto --strategy=deepspeed_stage_2
```

## 关联命令

- [[torchrun]]
- [[deepspeed]]

## 风险提示

> ⚠️ **LOW**: 框架自动管理资源，风险较低

## 参考链接

- [https://lightning.ai/docs/pytorch/](https://lightning.ai/docs/pytorch/)

## 所属维度

[[ML框架-MOC|AI基础设施/ML框架]]
